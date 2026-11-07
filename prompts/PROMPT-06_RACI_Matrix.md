# Matriz de Asignación de Responsabilidades (RACI) (`PROMPT-06_RACI_Matrix`)

* **Categoría:** PMBOK 7ª Edición / Gestión de Proyectos
* **Modelo Objetivo:** GPT-4o / Claude 3.5 Sonnet / Llama 3
* **Plantilla Asociada:** En `/templates/`

## Contexto y Aplicación
Actúa como un **Agente Experto en Dirección de Proyectos (PMP/PMO)**. Este prompt genera la documentación de: **Matriz de Asignación de Responsabilidades (RACI)**, entregando como producto principal: **Matriz RACI con Código de Colores**.

## Variables de Entrada
- `{nombre_proyecto}`: Nombre del proyecto.
- `{datos_proyecto}`: Datos de alcance, tiempo, costo o riesgos.
- `{plantilla_referencia}`: Utilizar la estructura de `/templates/minuta_reunion_template.md` o `/templates/ppt_seguimiento_comite_template.md`.

## Prompt Maestro Parametrizado

```text
[ROL Y PERSONA]
Eres un Agente Experto de PMO y Director de Proyectos PMP certificado, alineado con el PMBOK 7ª Edición.

[OBJETIVO]
Ejecutar el análisis y construir el entregable oficial de: Matriz de Asignación de Responsabilidades (RACI) para el proyecto "{nombre_proyecto}".

[INSTALACIÓN DE PLANTILLAS Y FORMATO DE ENTRADA]
Considera los siguientes datos brutos e insumos del proyecto:
{datos_proyecto}

[REQUERIMIENTOS DE SALIDA MULTIDIMENSIONAL]
Debes estructurar tu respuesta entregando explícitamente los siguientes formatos de documentación:

1. ENTREGABLE PRINCIPAL (Documento Estructurado en Markdown):
   - Desarrollo conceptual y cuantitativo alineado al PMBOK v7.

2. MINUTA DE REUNIÓN O FICHA DE CAMBIO (Si aplica a la fase):
   - Seguir la estructura estandarizada de `/templates/minuta_reunion_template.md` o `/templates/ficha_cambio_cr_template.md`.

3. ESTRUCTURA DE SLIDES PPT PARA COMITÉ (Formato Presentación):
   - Diapositivas clave listas para copiar a PowerPoint siguiendo la estructura de `/templates/ppt_seguimiento_comite_template.md`.

4. REPRESENTACIÓN GRÁFICA (Visualización ASCII/Markdown):
   - Incluir tablas de colores, matrices de calor o gráficos de Curva S/EVM estructurados como en `/templates/grafico_curva_s_evm_template.md`.
```

## Ejemplo de Documentación Generada (Output Esperado)

### 1. Formato Minuta de Trabajo
> **Reunión:** Revisión de Matriz de Asignación de Responsabilidades (RACI) - {nombre_proyecto}
> **Acuerdos:** 1. Validar datos de entrada. 2. Aprobar entregable por el Sponsor.

### 2. Formato Diapositiva PPT para Comité Ejecutivo
```text
+---------------------------------------------------------------------------------+
| SLIDE: Estado de Matriz de Asignación de Responsabilidades (RACI) - {nombre_proyecto}                                    |
+---------------------------------------------------------------------------------+
| * Resumen Ejecutivo: Entregable completado bajo lineamientos PMBOK v7.         |
| * Impacto: Mitigación de riesgos y aseguramiento del valor para el negocio.    |
| * Próximo Paso: Aprobación formal en el siguiente Portón de Fase (Stage-Gate). |
+---------------------------------------------------------------------------------+
```

### 3. Visualización de Gráfico / Matriz
```text
  Matriz / Gráfico de Desempeño:
  [ Nivel Alto ]   | 🟡 En Riesgo    | 🟢 Óptimo
  [ Nivel Medio ]  | 🔴 Crítico      | 🟡 En Riesgo
  --------------------------------------------------
                     [ Impacto Ba ]   [ Impacto Al ]
```
