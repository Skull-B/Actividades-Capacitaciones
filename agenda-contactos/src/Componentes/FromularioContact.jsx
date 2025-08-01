function FormularioContacto({ nuevoContacto, setnuevoContacto, agregarContacto, error }) {
    const handleChange = (e) => {
        const { name, value } = e.target;
        setnuevoContacto({
            ...nuevoContacto,
            [name]: value
        });
    };

    // Validación de campos antes de agregar el contac


    return (
        <div>
            <h2>Agregar Nuevo Contacto</h2>
        <form>
            {error && <p style={{ color: "red", fontWeight: "bold" }}>{error}</p>}
            <input
                type="text"
                name="nombre"
                value={nuevoContacto.nombre}
                onChange={handleChange}
                placeholder="Nombre"
            />
            <input
                type="email"
                name="email"
                value={nuevoContacto.email}
                onChange={handleChange}
                placeholder="Email"
            />
            <input
                type="tel"
                name="telefono"
                value={nuevoContacto.telefono}
                onChange={handleChange}
                placeholder="Teléfono"
            />
            <button type="button" onClick={agregarContacto}>
                Agregar Contacto
            </button>
        </form>
        </div>
    );
}
        
export default FormularioContacto;