# MCP Test

A very small and simple MCP server for test purpose only, using FastMCP.

## Requriments

- Python
- Git
- [uv](https://docs.astral.sh/uv/)

## Install

Clone repository and install:

```bash
$ git clone https://github.com/rnascunha/mcp-test
$ cd mcp-test
$ uv install
```

## Use

You can start a HTTP streamable or SSE (legacy) MCP server, with or without authentication (`Bearer token`).

To use it:

```bash
$ uv run src/app.py --help
warning: `VIRTUAL_ENV=/home/rnascunha/dev/workspace/test/mcp-test/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
usage: app.py [options]

MCP Server

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Server name
  -t {http,sse}, --transport {http,sse}
                        Transport protocol ('http'|'sse'). Default = http
  -p PORT, --port PORT  Endpoint port
  -u URL, --url URL     Endpoint URL
  -a AUTH, --auth AUTH  Server require authentication using token provided
  -m PATH, --path PATH  Endpoint path (must start with '/')
```

Default values:
```bash
-n, --name      = MCP server
-t, --transport = http
-p, --port PORT = 8000
-u, --url URL   = http://localhost
-a, --auth AUTH = None (no authetication)
-m, --path PATH = /mcp
```
