import os
import glob
from typing import Dict, Any, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PMBOKv7-Template-Server")

TEMPLATES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))
PROMPTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "prompts"))

@mcp.tool()
def get_pmbok_template(template_name: str) -> str:
    """Obtiene una plantilla de documentación PMBOK v7 por su nombre."""
    filepath = os.path.join(TEMPLATES_DIR, f"{template_name}.md")
    if not os.path.exists(filepath):
        filepath = os.path.join(TEMPLATES_DIR, template_name)
    
    if not os.path.exists(filepath):
        available = [os.path.basename(f) for f in glob.glob(os.path.join(TEMPLATES_DIR, "*.md"))]
        return f"Error: Plantilla '{template_name}' no encontrada. Disponibles: {available}"
    
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

@mcp.tool()
def list_pmbok_assets() -> Dict[str, List[str]]:
    """Lista todos los prompts y plantillas disponibles en la biblioteca PMBOK."""
    prompts = [os.path.basename(p) for p in glob.glob(os.path.join(PROMPTS_DIR, "*.md"))]
    templates = [os.path.basename(t) for t in glob.glob(os.path.join(TEMPLATES_DIR, "*.md"))]
    return {
        "prompts": prompts,
        "templates": templates
    }

if __name__ == "__main__":
    mcp.run()
