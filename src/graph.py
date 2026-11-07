import os
from typing import TypedDict, Annotated, List, Dict, Any
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

class PMBOKState(TypedDict):
    project_name: str
    user_input: str
    selected_template: str
    draft_document: str
    human_approved: bool
    final_output: str
    messages: List[Dict[str, str]]

def ingest_requirements_node(state: PMBOKState) -> Dict[str, Any]:
    """Paso 1: Analiza los requerimientos iniciales del usuario."""
    project_name = state.get("project_name", "Proyecto PMO Sin Nombre")
    user_input = state.get("user_input", "")
    return {
        "project_name": project_name,
        "selected_template": "acta_constitucion_template.md",
        "messages": state.get("messages", []) + [{"role": "system", "content": f"Requerimientos ingeridos para {project_name}"}]
    }

def generate_draft_node(state: PMBOKState) -> Dict[str, Any]:
    """Paso 2: Genera el borrador del documento aplicando la plantilla PMBOK."""
    project_name = state.get("project_name", "Proyecto")
    user_input = state.get("user_input", "Descripción inicial del proyecto")
    
    draft = f"""# ACTA DE CONSTITUCIÓN DEL PROYECTO (BORRADOR GENERADO)

**Nombre del Proyecto:** {project_name}
**Estado de Aprobación:** Pendiente de revisión por Dirección / Sponsor

## 1. Propósito y Justificación
{user_input}

## 2. Objetivos Medibles
- Cumplir el alcance en tiempo y presupuesto bajo estándares PMBOK 7ª Edición.
- Garantizar la satisfacción de los interesados clave.

## 3. Gobernanza y Entregables
- Grafo de trabajo estructurado en LangGraph.
- Conexión a herramientas corporativas mediante protocolo MCP.
"""
    return {"draft_document": draft}

def human_approval_node(state: PMBOKState) -> Dict[str, Any]:
    """Paso 3: Puerta de validación humana (HITL)."""
    approved = state.get("human_approved", False)
    if approved:
        final_doc = f"=== DOCUMENTO FINAL APROBADO ===\n\n{state.get('draft_document')}"
    else:
        final_doc = f"=== RECHAZADO / REQUIERE REVISIÓN ===\n\n{state.get('draft_document')}"
    return {"final_output": final_doc}

def route_approval(state: PMBOKState) -> str:
    """Enrutador condicional basado en la aprobación humana."""
    if state.get("human_approved", False):
        return "approve"
    return "reject"

def build_pmbok_graph():
    """Construye y compila el grafo de trabajo con LangGraph."""
    workflow = StateGraph(PMBOKState)

    workflow.add_node("ingest", ingest_requirements_node)
    workflow.add_node("generate_draft", generate_draft_node)
    workflow.add_node("human_approval", human_approval_node)

    workflow.add_edge(START, "ingest")
    workflow.add_edge("ingest", "generate_draft")
    workflow.add_edge("generate_draft", "human_approval")
    workflow.add_edge("human_approval", END)

    checkpointer = MemorySaver()
    return workflow.compile(checkpointer=checkpointer)
