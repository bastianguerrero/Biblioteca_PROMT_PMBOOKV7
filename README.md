# PMBOK v7 AI Agent & Prompt Library (LangGraph + MCP) - v2.0 Complete

Biblioteca completa de Prompts, Agentes y Plantillas de Documentación para la Gestión de Proyectos y PMO bajo el PMBOK 7ª Edición.

## Arquitectura de Orquestación: LangGraph + MCP

- **LangGraph:** Control de flujo cíclico, manejo de estado persistente y puertas de aprobación humana (HITL).
- **MCP (Model Context Protocol):** Integración estandarizada con herramientas corporativas (Jira, Confluence, Slack, GitHub, ERP, bases de datos RAG).

## Estructura del Proyecto

```
Biblioteca_PROMT_PMBOOKV7/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── agents/
│   └── pmbok_agents_config.json
├── prompts/
│   └── project_charter_prompt.md
├── templates/
│   └── acta_constitucion_template.md
└── src/
    ├── __init__.py
    ├── graph.py
    ├── main.py
    └── mcp_server.py
```

## Instalación y Ejecución

1. Clonar el repositorio y crear un entorno virtual:
   ```bash
   git clone https://github.com/bastianguerrero/Biblioteca_PROMT_PMBOOKV7.git
   cd Biblioteca_PROMT_PMBOOKV7
   python3 -m venv venv
   source venv/bin/activate  # En macOS/Linux
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar variables de entorno:
   ```bash
   cp .env.example .env
   ```

4. Ejecutar la CLI interactiva del Agente PMBOK:
   ```bash
   python -m src.main
   ```

5. Levantar el Servidor MCP:
   ```bash
   python -m src.mcp_server
   ```
