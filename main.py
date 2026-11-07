import sys
from src.graph import build_pmbok_graph

def run_cli():
    print("==================================================")
    print(" PMBOK v7 Agent & Prompt Library (LangGraph + MCP)")
    print("==================================================\n")

    project_name = input("Nombre del Proyecto: ").strip() or "Sistema de Gestión PMO"
    user_input = input("Descripción / Requerimientos iniciales: ").strip() or "Implementación de arquitectura LangGraph con conectores MCP."

    app = build_pmbok_graph()
    
    initial_state = {
        "project_name": project_name,
        "user_input": user_input,
        "selected_template": "",
        "draft_document": "",
        "human_approved": False,
        "final_output": "",
        "messages": []
    }

    config = {"configurable": {"thread_id": "session-pmbok-001"}}

    print("\n[+] Ejecutando grafo de LangGraph...")
    result = app.invoke(initial_state, config=config)

    print("\n--- BORRADOR GENERADO ---")
    print(result["draft_document"])

    print("\n--------------------------------------------------")
    approval = input("¿Apruebas este borrador para producción? (s/n): ").strip().lower()
    
    is_approved = approval == "s"
    
    final_state = app.invoke(
        {"human_approved": is_approved},
        config=config
    )

    print("\n--- RESULTADO FINAL DEL GRAFO ---")
    print(final_state["final_output"])
    print("\n[+] Proceso finalizado con éxito.")

if __name__ == "__main__":
    run_cli()
