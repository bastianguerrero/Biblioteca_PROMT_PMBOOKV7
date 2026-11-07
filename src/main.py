from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.graph import build_pmbok_graph

# Inicializamos la aplicación FastAPI que Render busca automáticamente
app = FastAPI(title="PMBOK v7 Agent & Prompt Library (LangGraph + Google Gemini)")

class ProjectRequest(BaseModel):
    project_name: Optional[str] = "Sistema de Gestión PMO"
    user_input: Optional[str] = "Implementación de arquitectura LangGraph con Google Gemini."
    human_approved: Optional[bool] = True

@app.get("/")
def root():
    return {"status": "ok", "message": "El Agente PMO PMBOK v7 está en línea y conectado en Render"}

@app.post("/run-pmo")
def run_pmo_agent(data: ProjectRequest):
    """Endpoint principal para ejecutar el grafo de LangGraph en la nube."""
    try:
        app_graph = build_pmbok_graph()
        
        initial_state = {
            "project_name": data.project_name,
            "user_input": data.user_input,
            "selected_template": "",
            "draft_document": "",
            "human_approved": data.human_approved,
            "final_output": "",
            "messages": []
        }

        config = {"configurable": {"thread_id": "session-pmbok-001"}}

        # Ejecutamos el grafo con la IA de Google Gemini
        result = app_graph.invoke(initial_state, config=config)
        
        final_state = app_graph.invoke(
            {"human_approved": data.human_approved},
            config=config
        )

        return {
            "status": "success",
            "project_name": data.project_name,
            "draft_document": result.get("draft_document", ""),
            "final_output": final_state.get("final_output", "")
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
