http:
		uv run src/app_http.py

sse:
		uv run src/app_sse.py

http_auth:
		uv run src/app_http.py auth

sse_auth:
		uv run src/app_sse.py auth