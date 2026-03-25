from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier
import sys


verifier = StaticTokenVerifier(
    tokens={
        "dev-alice-token": {
            "client_id": "alice@company.com",
            "scopes": ["read:data", "write:data", "admin:users"],
        },
        "api-key-12345": {"client_id": "guest-user", "scopes": ["read:data"]},
    }
)

# Initialize the server with a name
if len(sys.argv) > 1:
    print(1)
    mcp = FastMCP(name="NetworkServer", auth=verifier)
else:
    print(2)
    mcp = FastMCP(name="NetworkServer")
