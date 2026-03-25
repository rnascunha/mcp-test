from instance import mcp
import tools
import resources
import prompt

mcp.run(transport="sse", port=8000, path="/sse")
