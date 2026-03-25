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
$ uv install
```

## Use

You can start a HTTP streamable or SSE (legacy) MCP server, with or without authentication (`Bearer token`).

For authorization, the default token used is: `api-key-12345`. Just add the header:

```bash
Authorization: Bearer api-key-12345
```

### HTTP streamable

**Endpoint**: `http://localhost:8000/mcp`.

To initiate the server, at the project root directory:

```bash
$ uv run src/app_http.py [auth]
```

If used with the `auth` option, will be required authentication to connect.

### SSE (legacy)

**Endpoint**: `http://localhost:8000/sse`.
To initiate the server, at the project root directory:

```bash
$ uv run src/app_sse.py [auth]
```

If used with the `auth` option, will be required authentication to connect.
