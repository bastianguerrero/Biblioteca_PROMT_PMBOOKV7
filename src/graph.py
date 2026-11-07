import os
from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI

# 1. Definición del Estado global que viaja por el grafo (Memoria compartida)
class PMBOKState(TypedDict):
    project_name: str
    user_input: str
    selected_template: str
    draft_document: str
    human_approved: bool
    final_output: str
    messages: List[Dict[str, str]]

# 2. Nodo 1: Ingesta y preparación de los datos iniciales
def ingest_requirements_node(state: PMBOKState) -> Dict[str, Any]:
    """Recoge el nombre del proyecto y los requerimientos ingresados."""
    project_name = state.get("project_name", "Proyecto PMO Sin Nombre")
    user_input = state.get("user_input", "")
    
    return {
        "project_name": project_name,
        "selected_template": "acta_constitucion_template.md",
        "messages": state.get("messages", []) + [{"role": "system", "content": f"Requerimientos ingeridos correctamente para: {project_name}"}]
    }

# 3. Nodo 2: Generación real del borrador usando la IA y tus archivos de la biblioteca (Prompts + Plantillas)
def generate_draft_node(state: PMBOKState) -> Dict[str, Any]:
    """Lee el prompt maestro y la plantilla oficial de la biblioteca, y llama a la API de la IA."""
    project_name = state.get("project_name", "Proyecto")
    user_input = state.get("user_input", "")
    
    # Rutas absolutas a tus carpetas de la biblioteca en el repositorio
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    prompt_path = os.path.join(base_dir, "prompts", "project_charter_prompt.md")
    template_path = os.path.join(base_dir, "templates", "acta_constitucion_template.md")
    
    # Lectura dinámica del prompt del sistema
    system_prompt = "Eres un director de proyectos experto en PMBOK 7ª Edición."
    if os.path.exists(prompt_path):
        with open(prompt_path, "r", encoding="utf-8") as f:
            system_prompt = f.read()
            
    # Lectura dinámica de la plantilla oficial
    template_structure = ""
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as f:
            template_structure = f.read()

    # Inicialización del LLM (Compatible con OpenAI, modelos alternativos o APIs compatibles)
    # Lee automáticamente la variable OPENAI_API_KEY o puedes apuntarlo a otro proveedor mediante base_url
    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME", "gpt-4o"),
        temperature=0.3
    )
    
    # Construcción del prompt final combinando la biblioteca con los datos del usuario
    final_prompt = f"""
    {system_prompt}
    
    Utiliza estrictamente la siguiente plantilla estructurada en Markdown para formatear tu respuesta:
    {template_structure}
    
    Datos de entrada proporcionados por el usuario para el proyecto:
    - Nombre del Proyecto: {project_name}
    - Requerimientos / Descripción: {user_input}
    """
    
    # Invocación real a la API de la inteligencia artificial
    response = llm.invoke(final_prompt)
    
    return {"draft_document": response.content}

# 4. Nodo 3: Puerta de validación humana (Human-in-the-Loop - HITL)
def human_approval_node(state: PMBOKState) -> Dict[str, Any]:
    """Evalúa si el borrador fue aprobado o rechazado por el revisor."""
    approved = state.get("human_approved", False)
    draft = state.get("draft_document", "")
    
    if approved:
        final_doc = f"=== DOCUMENTO FINAL APROBADO PARA PRODUCCIÓN ===\n\n{draft}"
    else:
        final_doc = f"=== RECHAZADO / DEVUELTO PARA CORRECCIÓN ===\n\n{draft}"
        
    return {"final_output": final_doc}

# 5. Función de enrutamiento condicional basada en el estado
def route_approval(state: PMBOKState) -> str:
    """Decide el flujo basándose en la aprobación humana."""
    if state.get("human_approved", False):
        return "approve"
    return "reject"

# 6. Ensamblaje y compilación del Grafo con LangGraph
def build_pmbok_graph():
    """Construye, conecta los nodos y compila el flujo con soporte de checkpoints."""
    workflow = StateGraph(PMBOKState)

    # Registro de nodos
    workflow.add_node("ingest", ingest_requirements_node)
    workflow.add_node("generate_draft", generate_draft_node)
    workflow.add_node("human_approval", human_approval_node)

    # Definición de las aristas (Flujo secuencial)
    workflow.add_edge(START, "ingest")
    workflow.add_edge("ingest", "generate_draft")
    workflow.add_edge("generate_draft", "human_approval")
    workflow.add_edge("human_approval", END)

    # Memoria persistente para pausar en el HITL y retomar sesión
    checkpointer = MemorySaver()
    
    return workflow.compile(checkpointer=checkpointer)
