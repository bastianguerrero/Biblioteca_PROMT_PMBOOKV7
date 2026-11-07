# Ficha Técnica de Agente: Agente de Alcance y EDT/WBS

## 1. Identificación y Metadatos
- **Nombre del Agente:** `PM_Agent_ScopeWBS`
- **Rol / Persona:** Agente experto especializado en Agente de Alcance y EDT/WBS alineado con PMBOK 7ª Edición.
- **Propietario / Responsable:** Liderazgo de PMO / Dirección de Proyectos.

## 2. Objetivo y Caso de Uso
- **Misión Principal:** Ejecutar y controlar las actividades asociadas a Agente de Alcance y EDT/WBS, utilizando plantillas oficiales.
- **Objetivos Secundarios:** Elaboración automática de informes, estructuración de minutas y generación de diapositivas para comités.
- **Fuera de Alcance:** Modificación directa de líneas base sin aprobación formal en comités (HITL).

## 3. Flujo de Trabajo y Lógica (Orquestación - LangGraph)
- **Disparador (Trigger):** Evento en Jira, Slack, comando de usuario o llamada de agente coordinador.
- **Pasos de Ejecución:** 
  1. Cargar contexto e insumos del proyecto.
  2. Importar plantilla oficial desde `/templates/ficha_cambio_cr_template.md`.
  3. Procesar datos mediante LLM y calcular métricas.
  4. Generar entregable estructurado (Minuta, PPT, Ficha CR o Gráficos ASCII/Markdown).
  5. Enviar a revisión humana (Human-in-the-Loop) si aplica.
- **Tipo de Arquitectura:** LangGraph Stateful Subgraph (Con checkpoints y HITL).

## 4. Fuentes de Conocimiento e Integraciones (MCP)
- **Plantilla Oficial Utilizada:** `/templates/ficha_cambio_cr_template.md`
- **Bases de Datos / RAG:** PMBOK v7, lecciones aprendidas de la organización.
- **Conectores MCP:** Servers para Jira, Confluence, GitHub, Slack y exportadores de PDF/PPTX.

## 5. Memoria y Estado
- **Tipo de Memoria:** Persistente por sesión (Checkpointer SQLite/PostgreSQL).
- **Límite de Contexto:** Ventana activa de 128k tokens.

## 6. Seguridad, Límites y Guardrails
- **Restricciones:** Ocultamiento automático de PII y datos financieros restringidos.
- **Manejo de Errores:** Derivación inmediata al PM ante datos inconsistentes.

## 7. Métricas de Éxito (KPIs)
- Adherencia a la plantilla corporativa (100%), velocidad de generación (< 15 segundos), nivel de aprobación en comités (> 90%).
