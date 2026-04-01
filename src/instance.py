from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier
from args import args

verifier = (
    StaticTokenVerifier(
        tokens={
            f"{args.auth}": {"client_id": "guest-user", "scopes": ["read:data"]},
        }
    )
    if args.auth is not None
    else None
)

# Initialize the server with a name
mcp = FastMCP(name=args.name, auth=verifier)

print(args)
