from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

from models.recommender import OptimizedBeatRecommendationModel

model = OptimizedBeatRecommendationModel()


def load():
    model.load_model("model.json")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/recommend"):
            params = parse_qs(urlparse(self.path).query)
            user_id = int(params.get("user_id", ["0"])[0])
            n = int(params.get("n", ["10"])[0])
            recs = model.get_fast_recommendations(user_id, n)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(recs).encode())
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=Handler, port=8000):
    load()
    server = server_class(("0.0.0.0", port), handler_class)
    print(f"Serving on port {port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
