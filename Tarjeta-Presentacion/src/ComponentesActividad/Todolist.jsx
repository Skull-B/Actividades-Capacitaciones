import { useState } from "react";

function TodoList() {
  const [listaDeTareas, setListaDeTareas] = useState([
    { id: 1, tarea: "Hacer la compra", completada: false },
    { id: 2, tarea: "Lavar la ropa", completada: false },
    { id: 3, tarea: "Estudiar React", completada: false }
  ]);

  const [nuevaTarea, setNuevaTarea] = useState("");


  const agregarTarea = () => {
    if (nuevaTarea.trim() !== "") {
      const nuevaTareaObj = {
        id: Date.now(),
        tarea: nuevaTarea,
        completada: false
      };
      setListaDeTareas([...listaDeTareas, nuevaTareaObj]);
      setNuevaTarea("");
    }
  };

  const completarTarea = (id) => {
    const nuevas = listaDeTareas.map((tarea) =>
      tarea.id === id
        ? { ...tarea, completada: !tarea.completada }
        : tarea
    );
    setListaDeTareas(nuevas);
  };


  const eliminarTarea = (id) => {
    const nuevaLista = listaDeTareas.filter((tarea) => tarea.id !== id);
    setListaDeTareas(nuevaLista);
  };

  return (
    <div className="Todolist">
      <h1>Lista de Tareas</h1>

      {/* Input y botón */}
      <input
        type="text"
        value={nuevaTarea}
        onChange={(e) => setNuevaTarea(e.target.value)}
        placeholder="Añadir nueva tarea"
      />
      <button onClick={agregarTarea} disabled={!nuevaTarea.trim()}>
        Añadir Tarea
      </button>

      {/* Renderizado condicional */}
      {listaDeTareas.length === 0 ? (
        <p>No tienes tareas pendientes!</p>
      ) : (
        <ul>
          {listaDeTareas.map((tarea) => (
            <li
              key={tarea.id}
              style={{
                textDecoration: tarea.completada ? "line-through" : "none"
              }}
            >
              {tarea.tarea}
              <button onClick={() => completarTarea(tarea.id)}>
                {tarea.completada ? "Desmarcar" : "Completar"}
              </button>
              <button onClick={() => eliminarTarea(tarea.id)}>Eliminar</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default TodoList;
