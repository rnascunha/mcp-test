from instance import mcp
import tools
import resources
import prompt
from args import args

mcp.run(transport=args.transport, port=args.port, path=args.path)
