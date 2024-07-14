# Analizando el Script de Python a través del lente de la Filosofía Unix

Este artículo examina un script de Python diseñado para mover todos los archivos PDF de un directorio fuente a un directorio de destino mientras se eliminan los duplicados. Analizaremos este script en el contexto de la Filosofía Unix, que enfatiza la simplicidad, la modularidad y la reutilización.

# Principios de la Filosofía Unix

La Filosofía de Unix se puede resumir en algunos principios claves:

Hacer que cada programa haga una cosa bien.
Esperar que la salida de cada programa se convierta en la entrada de otro.
Diseñar y construir software para probarlo temprano, idealmente dentro de semanas.
Usar herramientas en lugar de ayuda no especializada para aligerar una tarea de programación.
Escribir programas para trabajar juntos.
Escribir programas para manejar flujos de texto, porque es una interfaz universal.
Recuerda que la Filosofía Unix fomenta elecciones pragmáticas que priorizan la colaboración humana y la mantenibilidad. Al alinear tu script de Python con estos principios, crearás soluciones más robustas y elegantes.

# Script Overview

[sort.py](sort.py)

## Análisis de la Adherencia a la Filosofía Unix

### 1. Hacer que cada programa haga una cosa bien

El script se enfoca en una sola tarea: mover archivos PDF y eliminar duplicados. Cada función dentro del script tiene un propósito claro y específico, como verificar archivos duplicados (`isNotDuplicated`), comprobar extensiones PDF (`isPDF`) y manejar argumentos de la línea de comandos (`get_cli_args`).

### 2. Esperar que la salida de cada programa se convierta en la entrada de otro

Aunque este script es autónomo y no alimenta directamente su salida a otro programa, está diseñado de manera que sus funciones puedan integrarse fácilmente en flujos de trabajo más grandes. Por ejemplo, `getFiles` puede reutilizarse para filtrar archivos en otros scripts, y `movePDF` puede adaptarse para manejar diferentes tipos de archivos o destinos.

### 3. Diseñar y construir software para probarlo pronto

El script incluye una opción `--unittest` para ejecutar doctests, lo que significa que el código puede probarse inmediatamente después de realizar cambios. Esto fomenta el desarrollo iterativo y la retroalimentación inmediata, alineándose con la filosofía Unix de construir y probar software rápidamente.

### 4. Usar herramientas en lugar de ayuda no calificada

El script aprovecha varias bibliotecas potentes de Python (`argparse`, `shutil`, `pathlib` y `re`) para realizar sus tareas de manera eficiente. Este uso de bibliotecas robustas simplifica el código y reduce la probabilidad de errores, encarnando la filosofía Unix de utilizar herramientas efectivas.

### 5. Escribir programas para trabajar juntos

El diseño modular del script, con definiciones de funciones claras y un punto de entrada principal, facilita la integración con otros scripts o sistemas. Funciones como `getFiles` y `movePDF` pueden probarse y reutilizarse de manera independiente, promoviendo la interoperabilidad.

### 6. Escribir programas para manejar flujos de texto

Aunque el script trata principalmente con rutas de archivos y operaciones, sigue el principio de manejar flujos de texto al procesar argumentos de la línea de comandos y validar rutas. El uso de `argparse` asegura que el script pueda interactuar sin problemas con la entrada del usuario proporcionada como texto.

## Conclusión

Este script de Python ejemplifica varios aspectos clave de la Filosofía Unix. Su enfoque en una sola tarea, estructura modular, uso de herramientas potentes y capacidad de ser probado e integrado en flujos de trabajo más grandes reflejan los principios que han guiado el desarrollo de Unix durante décadas. Al adherirse a estos principios, el script no solo logra su objetivo de manera efectiva, sino que también mantiene simplicidad, claridad y flexibilidad.
