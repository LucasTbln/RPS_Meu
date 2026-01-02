## Rúbrica para la Práctica RPS

**Aspectos a evaluar:**

*   **Especificación del entorno de tareas (25%):**
    *   **Excelente (25 puntos):** El alumno especifica correctamente todas las características del entorno de tareas del RPS, justificando cada una con precisión según la sección "2.3.2 Properties of task environments" del libro "IA: A Modern Approach" de Russell & Norvig.
    *   **Bueno (18 puntos):** El alumno especifica la mayoría de las características correctamente, con algunas justificaciones incompletas o con errores menores.
    *   **Suficiente (12 puntos):** El alumno identifica algunas características correctamente, pero comete errores o imprecisiones en las justificaciones o en la clasificación.
    *   **Insuficiente (6 puntos):** El alumno no comprende las características del entorno de tareas o las clasifica incorrectamente.

*   **Identificación del tipo de agente y estructura (25%):**
    *   **Excelente (25 puntos):** El alumno selecciona un tipo de agente adecuado para el RPS y dibuja un modelo preciso de la estructura del agente, incluyendo los componentes específicos del tipo elegido, basándose en los conceptos del capítulo 2 "Intelligent Agents".
    *   **Bueno (18 puntos):** El alumno selecciona un tipo de agente adecuado, pero el modelo de la estructura del agente presenta algunas imprecisiones o falta de detalle en los componentes.
    *   **Suficiente (12 puntos):** El alumno selecciona un tipo de agente, pero este no es el más adecuado para el RPS, o el modelo de la estructura del agente es incompleto o confuso.
    *   **Insuficiente (6 puntos):** El alumno no identifica un tipo de agente o dibuja un modelo de la estructura del agente incorrecto o sin relación con el RPS.

*   **Implementación en Python (30%):**
    *   **Excelente (30 puntos):** El alumno implementa en Python todos los componentes de la estructura del agente de forma correcta y eficiente, creando una función agente que juega al RPS siguiendo la lógica del tipo de agente seleccionado.  El código cumple con los principios SOLID, especialmente SRP y OCP, permitiendo extender la lógica a otras versiones del juego. La estrategia implementada en `get_computer_action()` es creativa y busca maximizar el rendimiento del agente.
    *   **Bueno (22 puntos):** El alumno implementa la mayoría de los componentes correctamente, pero el código presenta algunos errores menores o falta de eficiencia. La implementación de los principios SOLID es parcial o presenta algunas dificultades. La estrategia implementada en `get_computer_action()` es funcional pero no busca activamente maximizar el rendimiento.
    *   **Suficiente (15 puntos):** El alumno implementa algunos componentes, pero el código presenta errores significativos o la función agente no funciona correctamente. La implementación de los principios SOLID es deficiente. La estrategia implementada en `get_computer_action()` es básica o aleatoria.
    *   **Insuficiente (7 puntos):** El alumno no implementa los componentes o la función agente no se relaciona con el RPS. El código no cumple con los principios SOLID.

*   **Extensión y documentación (20%):**
    *   **Excelente (20 puntos):** El alumno extiende la lógica del agente para jugar a la versión "piedra, papel, tijeras, lagarto, Spock" correctamente, manteniendo la calidad del código y la coherencia con el tipo de agente seleccionado. La documentación en el README del proyecto en GitHub/GitLab es completa y clara, explicando el problema, el entorno de tareas, la estructura del agente, la implementación y la extensión, con un formato Markdown adecuado.
    *   **Bueno (14 puntos):** El alumno extiende la lógica del agente, pero la implementación presenta algunas limitaciones o no es del todo coherente con el tipo de agente. La documentación es completa pero con algunas imprecisiones o falta de claridad en el formato.
    *   **Suficiente (8 puntos):** El alumno intenta extender la lógica del agente, pero la implementación es incorrecta o incompleta. La documentación es incompleta o poco clara.
    *   **Insuficiente (4 puntos):** El alumno no extiende la lógica del agente o la extensión no funciona. La documentación es inexistente o muy deficiente. 
