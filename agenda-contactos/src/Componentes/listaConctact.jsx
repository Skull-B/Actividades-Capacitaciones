function ListaContactos({ contactos, buscarContacto, eliminarContacto }) {
    const contactosFiltrados = contactos.filter(c =>
        (c.nombre?.toLowerCase() || "").includes(buscarContacto.toLowerCase()) ||
        (c.email?.toLowerCase() || "").includes(buscarContacto.toLowerCase())
    );

    const confimarEliminacion = (id) => {
        if (window.confirm("¿Estás seguro de eliminar este contacto?")) {
            eliminarContacto(id);
        }
    };

    return (
        <ul>
            {contactosFiltrados.length > 0 ? (
                contactosFiltrados.map((c) => (
                    <li key={c.id}>
                        {c.nombre} - {c.email} - {c.telefono}
                        <button onClick={() => confimarEliminacion(c.id)}>Eliminar</button>
                    </li>
                ))
            ) : (
                <li>No se encontraron contactos</li>
            )}
        </ul>
    );
}

export default ListaContactos;
