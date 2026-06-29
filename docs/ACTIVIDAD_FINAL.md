# Actividad final: rescate en un mapa con obstáculos

## ## Producto esperado

- Tabla comparativa:

| Algoritmo | ¿Encontró camino? | Longitud del camino | Observación |
| :--- | :--- | :--- | :--- |
| **BFS** | Sí | 15 pasos | Elian Valenzuela: Encuentra de forma garantizada la ruta más corta. Sin embargo, al revisar en capas radiales (como anillos), explora muchas casillas vacías innecesarias antes de dar con la meta. |
| **DFS** | Sí | 19 pasos | Felipe Campos: No garantiza el camino más corto. Como se va de cabeza por una sola rama hasta el fondo usando una pila, dio una vuelta más larga rodeando los obstáculos superiores antes de bajar a la meta. |
| **A\*** | Sí | 15 pasos | Johan Oña: Encuentra la ruta óptima (igual de corta que BFS) pero de manera mucho más rápida y directa, ya que usa la distancia Manhattan como brújula para no desviarse hacia zonas muertas. |

---

## ## Reflexión final

Durante el desarrollo de este taller, el error más complejo de depurar fue controlar el momento exacto en el que se marcan los nodos como visitados; un retraso en este registro provocaba que la frontera repitiera elementos, generando bucles redundantes. Con respecto a las estructuras de control, aprendimos que la frontera actúa como el motor del algoritmo: en BFS funciona como una cola (FIFO) expandiendo el mapa de forma equitativa, en DFS opera como una pila (LIFO) explorando líneas profundas, mientras que el conjunto de visitados y el diccionario de padres son indispensables para evitar ciclos infinitos y reconstruir la ruta de retorno al origen. Finalmente, confirmamos que A* es drásticamente más eficiente que BFS en entornos con obstáculos debido a que no realiza una búsqueda a ciegas; al incorporar la heurística de la distancia Manhattan ($f(n) = g(n) + h(n)$), el algoritmo estima matemáticamente la cercanía real hacia la meta 'G', priorizando únicamente los caminos que avanzan en la dirección correcta y descartando rutas innecesarias.

---

## 📸 Evidencias de Ejecución Individual

### 1. BFS - Elian Valenzuela
![Evidencia BFS](evidencia_elian_bfs.png)

### 2. DFS - Felipe Campos
![Evidencia DFS](evidencia_felipe_dfs.png)

### 3. A* - Johan Oña
![Evidencia A*](evidencia_johan_astar.png)