import pandas as pd
from fastmcp import FastMCP
from mcp_pyproject_pkg.utils import UTILITY

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
