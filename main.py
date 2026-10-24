import os
from flask import Flask, jsonify
import httpx

app = Flask(__name__)

@app.route('/group/<int:group_id>')
async def get_group(group_id):
    url = f"https://roblox.com{group_id}"
    async with httpx.AsyncClient() as client:
        # Render networks handle this flawlessly without blocks!
        response = await client.get(url, timeout=5.0)
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"error": "Failed to fetch data"}), response.status_code

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
