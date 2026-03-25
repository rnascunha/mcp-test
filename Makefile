help:
		uv run src/app.py --help

http:
		uv run src/app.py

sse:
		uv run src/app.py --transport=sse --path=/sse

http_auth:
		uv run src/app.py --auth='api-key-12345'

sse_auth:
		uv run src/app.py --transport=sse  --path=/sse --auth="api-key-12345"