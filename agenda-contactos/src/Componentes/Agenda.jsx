import { useState, useEffect, useRef } from "react";
import FormularioContacto from "./FromularioContact";
import ListaContactos from "./listaConctact";
import "../Componentes/agenda.css"


function AgendaContactos() {
    const [contactos, setContactos] = useState([]);
    const [nuevoContacto , setnuevoContacto] = useState({
        nombre: "",
        email: "",
        telefono: ""
    });
    
    const isFirstRender = useRef(true);

    useEffect(() => {
        const storeContactos = JSON.parse(localStorage.getItem("contactos")) || [];
        setContactos(storeContactos);
    }, []);

    useEffect(() => {
        if (isFirstRender.current) {
            isFirstRender.current = false;
            return; 
        }
        localStorage.setItem("contactos", JSON.stringify(contactos));
    }, [contactos]);

    const [buscarContacto, setBuscarContacto] = useState("");
    const [error, setError] = useState("");




    const agregarContacto = () => {
        if (!nuevoContacto.nombre || !nuevoContacto.email || !nuevoContacto.telefono) {
            setError("Por favor, completa todos los campos.");
            return;
        }
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(nuevoContacto.email)) {
            setError("Por favor, ingresa un email válido.");
            return;
        }
        const telefonoRegex = /^\d{10}$/; // Ejemplo de validación para un número de teléfono de 10 dígitos
        if (!telefonoRegex.test(nuevoContacto.telefono)) {
            setError("Por favor, ingresa un número de teléfono válido.");
            return;
        }
        const emailExists = contactos.some(contacto => contacto.email === nuevoContacto.email);
        if (emailExists) {
            setError("El email ya está registrado.");
            return;
        }

        setContactos([...contactos, { ...nuevoContacto, id: Date.now() }]);
        setnuevoContacto({
            nombre: "",
            email: "",
            telefono: ""
        });
        setError("");
    };

    const eliminarContacto = (id) => {
        setContactos(contactos.filter(c => c.id !== id));
    };
    

return (

    <div>
        <h1>Agenda de Contactos</h1>
        <FormularioContacto
            nuevoContacto={nuevoContacto}
            setnuevoContacto={setnuevoContacto}
            agregarContacto={agregarContacto}
            error={error}

        />
        <input
           type="text"
           placeholder="Buscar contacto..."
           value={buscarContacto}
           onChange={(e) => setBuscarContacto(e.target.value)}
          style={{ marginBottom: "10px", padding: "5px", width: "100%" }}
        />
        <ListaContactos
            contactos={contactos}
            eliminarContacto={eliminarContacto}
            buscarContacto={buscarContacto}
        />
    </div>
);

}
export default AgendaContactos;

    