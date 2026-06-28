#!/usr/bin/env python3
"""Local static server for the gitignored _audio/ directory.

Serves narration mp3s for local Jekyll preview, with HTTP Range support so the
browser's <audio> element can seek. Production serves these from a CDN instead.

Usage:  python3 serve_audio.py [port]   (default 8001)
"""
import os
import sys
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_audio")


class RangeHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # allow cross-origin playback from the Jekyll dev origin
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def send_head(self):
        rng = self.headers.get("Range")
        if rng is None:
            return super().send_head()
        try:
            unit, _, rest = rng.partition("=")
            start_s, _, end_s = rest.partition("-")
            if unit.strip() != "bytes":
                return super().send_head()
        except ValueError:
            return super().send_head()

        path = self.translate_path(self.path)
        if not os.path.isfile(path):
            return super().send_head()  # let base produce 404
        size = os.path.getsize(path)
        start = int(start_s) if start_s else 0
        end = int(end_s) if end_s else size - 1
        end = min(end, size - 1)
        if start > end or start >= size:
            self.send_response(416)
            self.send_header("Content-Range", f"bytes */{size}")
            self.end_headers()
            return None

        f = open(path, "rb")
        f.seek(start)
        self._range = (start, end)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(end - start + 1))
        self.end_headers()
        return f

    def copyfile(self, source, outputfile):
        if getattr(self, "_range", None) is None:
            return super().copyfile(source, outputfile)
        start, end = self._range
        remaining = end - start + 1
        while remaining > 0:
            chunk = source.read(min(64 * 1024, remaining))
            if not chunk:
                break
            outputfile.write(chunk)
            remaining -= len(chunk)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8001
    host = sys.argv[2] if len(sys.argv) > 2 else "0.0.0.0"  # 0.0.0.0 = reachable on LAN
    if not os.path.isdir(ROOT):
        sys.exit(f"audio dir not found: {ROOT}")
    handler = partial(RangeHandler, directory=ROOT)
    print(f"serving {ROOT} at http://{host}:{port}/  (Range enabled)")
    HTTPServer((host, port), handler).serve_forever()


if __name__ == "__main__":
    main()
