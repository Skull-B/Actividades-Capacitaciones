import { useState } from "react";

function Contador() {
  const [contador, setContador] = useState(0);  
  const [nombre, setNombre] = useState("Contador");
  const [descripcion, setDescripcion] = useState("");
  const [activo, setActivo] = useState(true);
  const [opciones, setOpciones] = useState("")

return (
    <div className="Contador" style={{ textAlign: 'center' }}>
      <h1>Contador</h1>
      <p>Click : {contador} </p>
     <button onClick={() => setContador(contador + 1)}>Incrementar</button>
     <button onClick={() => setContador(contador - 1)}>Decrementar</button>
     <button onClick={() => setContador(0)}>Reiniciar</button>

    <input type="text" value={nombre} onChange={ e => setNombre(e.target.value)} />
    <textarea value={descripcion} onChange={ e => setDescripcion(e.target.value)}/>
    <input type="checkbox" checked={activo} onChange={e => setActivo(e.target.checked)} />
    <select value={opciones} onChange={e => setOpciones(e.target.value)}>
        <option value="opcion1">Opción 1</option>
        <option value="opcion2">Opción 2</option>
        <option value="opcion3">Opción 3</option>
    </select>  
    </div>

 ); 
}
export default Contador;
    