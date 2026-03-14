from flask import Flask, jsonify, request

app = Flask(__name__)

def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.after_request
def after_request(response):
    return add_cors(response)

# --- 1. HALAMAN UTAMA (HTML) ---
@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OmniPlay AI Agent</title>
        <style>
            body {
                background-color: #0d1117; color: #c9d1d9;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                display: flex; justify-content: center; align-items: center;
                height: 100vh; margin: 0;
            }
            .container {
                text-align: center; padding: 50px; border: 1px solid #30363d;
                border-radius: 15px; background-color: #161b22;
                box-shadow: 0 8px 24px rgba(0,0,0,0.5); max-width: 500px;
            }
            h1 { color: #58a6ff; margin-bottom: 10px; }
            p { font-size: 16px; line-height: 1.5; color: #8b949e; margin-bottom: 30px; }
            .status-badge {
                padding: 8px 16px; background-color: #238636; color: #ffffff;
                border-radius: 20px; font-size: 14px; font-weight: bold;
                display: inline-block; border: 1px solid #2ea043;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>OmniPlay AI</h1>
            <p>GameFi and Play-to-Earn (P2E) economic analysis agent. Tracks in-game token emissions, analyzes NFT asset utility, and optimizes gaming guild scholarship yields on the Base network.</p>
            <div class="status-badge">🟢 System Online & Healthy</div>
        </div>
    </body>
    </html>
    """
    return html_content

# --- 2. ENDPOINT MCP ---
@app.route('/mcp', methods=['GET', 'POST', 'OPTIONS'])
def mcp_endpoint():
    server_info = {
        "name": "OmniPlay Agent Server",
        "version": "1.0.0",
        "website": "https://omniplay-api.vercel.app",
        "description": "GameFi economy and P2E yield optimization agent"
    }
    tools = [
        {"name": "track_token_emissions", "description": "Monitor in-game token inflation rates", "inputSchema": {"type": "object","properties": {}}},
        {"name": "analyze_nft_utility", "description": "Evaluate the ROI of specific game NFT assets", "inputSchema": {"type": "object","properties": {}}},
        {"name": "optimize_guild_yield", "description": "Calculate best strategies for gaming guild scholars", "inputSchema": {"type": "object","properties": {}}}
    ]
    prompts = [
        {"name": "gamefi_economy_report", "description": "Generate health report of a Web3 game economy", "arguments": []},
        {"name": "p2e_roi_calculator", "description": "Calculate estimated time to ROI for new players", "arguments": []}
    ]
    
    if request.method == 'GET':
        return jsonify({
            "protocolVersion": "2024-11-05",
            "serverInfo": server_info,
            "tools": tools,
            "prompts": prompts,
            "resources": [] 
        })

    req_data = request.get_json(silent=True) or {}
    req_id = req_data.get("id", 1)
    method = req_data.get("method", "")

    if method == "tools/list":
        result = {"tools": tools}
    elif method == "prompts/list":
        result = {"prompts": prompts}
    else:
        result = {
            "protocolVersion": "2024-11-05",
            "serverInfo": server_info,
            "capabilities": {"tools": {},"prompts": {},"resources": {}}
        }

    return jsonify({"jsonrpc": "2.0", "id": req_id, "result": result})

# --- 3. ENDPOINT A2A (UPDATE ID AKUN 11: 22379) ---
@app.route('/.well-known/agent-card.json', methods=['GET','OPTIONS'])
def a2a_endpoint():
    return jsonify({
        "id": "omniplay",
        "name": "omniplay",
        "version": "1.0.0",
        "description": "GameFi and P2E economic analysis agent.",
        "website": "https://omniplay-api.vercel.app",
        "url": "https://omniplay-api.vercel.app",
        "documentation_url": "https://omniplay-api.vercel.app",
        "provider": {
            "organization": "OmniPlay Gaming Labs",
            "url": "https://omniplay-api.vercel.app"
        },
        "registrations": [
            {
                "agentId": 22379,
                "agentRegistry": "eip155:8453:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432"
            }
        ],
        "supportedTrust": ["reputation", "tee-attestation"],
        "skills": [
            {"name": "Economy Analysis", "description": "Track token inflation", "category": "market/economy_analysis"},
            {"name": "GameFi Data", "description": "Analyze NFT utility", "category": "data_analysis/gamefi"},
            {"name": "Yield Strategy", "description": "Optimize scholar yields", "category": "market/yield_strategy"}
        ]
    })

# --- 4. ENDPOINT OASF ---
@app.route('/oasf', methods=['GET','OPTIONS'])
def oasf_endpoint():
    return jsonify({
        "id": "omniplay",
        "name": "omniplay",
        "version": "v0.8.0",
        "description": "Main endpoint for OmniPlay AI",
        "website": "https://omniplay-api.vercel.app",
        "protocols": ["mcp","a2a"],
        "capabilities": ["track_token_emissions", "analyze_nft_utility", "optimize_guild_yield"],
        "skills": [
            {"name": "market/economy_analysis","type": "analytical"},
            {"name": "data_analysis/gamefi","type": "analytical"},
            {"name": "market/yield_strategy","type": "operational"}
        ],
        "domains": [
            "web3/gamefi",
            "market/play_to_earn",
            "technology/gaming"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
