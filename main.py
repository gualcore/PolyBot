import os
import requests as req_lib
from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "https://polybotsystem.xyz")

@app.route('/api/v1/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/api/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy_api(path):
    if request.path.startswith('/api/v1/'):
        target = f"{BACKEND_URL}/api/v1/{path}"
    else:
        target = f"{BACKEND_URL}/api/{path}"

    referrer = request.headers.get('Referer', 'Direct')
    
    qs = request.query_string.decode('utf-8')
    if qs:
        target = f"{target}?{qs}"

    hop_by_hop = {'host', 'content-length', 'transfer-encoding', 'connection'}
    fwd_headers = {k: v for k, v in request.headers if k.lower() not in hop_by_hop}

    try:
        resp = req_lib.request(
            method=request.method,
            url=target,
            headers=fwd_headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            timeout=30
        )
    except Exception as e:
        print(f"[!] Connection Error: {str(e)}")
        return jsonify({"error": "Gateway Timeout"}), 504

    skip = {'content-encoding', 'content-length', 'transfer-encoding', 'connection'}
    out_headers = [(k, v) for k, v in resp.raw.headers.items() if k.lower() not in skip]
    return resp.content, resp.status_code, out_headers

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path and os.path.exists(os.path.join('static', path)):
        return send_from_directory('static', path)
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    print("="*50)
    print("           POLYBOT PROXY SYSTEM v1.0")
    print("="*50)
    print(f"[*] Master Server: {BACKEND_URL}")
    print("[*] Local Proxy  : http://localhost:5000")
    print("[*] Status       : ACTIVE / READY")
    print("="*50)
    print("[!] Logs will appear below as requests come in...")
    app.run(host='0.0.0.0', port=5000)
