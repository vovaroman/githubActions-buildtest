import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Flask instance, not the module
from app import app as flask_app

def test_home():
    with flask_app.test_client() as client:
        resp = client.get("/")
        assert resp.status_code == 200
        assert resp.data == b"Hello, DevOps!"
