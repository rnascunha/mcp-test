from instance import mcp
import tools
import resources
import prompt

mcp.run(transport="http", port=8000, path="/mcp")
# mcp.run(transport="sse", port=8000, path="/sse")
