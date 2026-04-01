import argparse

parser = argparse.ArgumentParser(description="MCP Server", usage="%(prog)s [options]")

parser.add_argument(
    "-n",
    "--name",
    default="MCP server",
    help="Server name",
)
parser.add_argument(
    "-t",
    "--transport",
    default="http",
    choices=["http", "sse"],
    help="Transport protocol ('http'|'sse'). Default = http",
)
parser.add_argument("-p", "--port", default=8000, type=int, help="Endpoint port")
parser.add_argument("-u", "--url", default="localhost", help="Endpoint URL")
parser.add_argument(
    "-a",
    "--auth",
    type=str,
    help="Server require authentication using token provided",
    default=None,
)
parser.add_argument(
    "-m",
    "--path",
    default="/mcp",
    help="Endpoint path (must start with '/')",
)

args = parser.parse_args()
