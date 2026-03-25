from instance import mcp


@mcp.resource("file://documents/{name}")
def read_document(name: str) -> str:
    """Read a document by name."""
    # In a real application, this would read from disk
    return f"Content of {name}"


@mcp.resource("config://settings")
def get_settings() -> str:
    """Get application settings."""
    return """{ "theme": "dark", "language": "en", "debug": false }"""
