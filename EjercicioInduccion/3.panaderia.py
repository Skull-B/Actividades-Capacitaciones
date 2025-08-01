inventario = {
    "Leche": {"precio": 1.50, "cantidad": 10},
    "Cafe": {"precio": 2.00, "cantidad": 5},
    "Panela": {"precio": 1.75, "cantidad": 8}
}

while True:
    print("\n1) Consultar precio y cantidad de un producto")
    print("2) Registrar venta")
    print("3) Agregar nuevo producto")
    print("4) Mostrar inventario completo")
    print("5) Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ").strip()
        if producto in inventario:
            datos = inventario[producto]
            print(f"{producto} - Precio: ${datos['precio']:.2f}, Cantidad: {datos['cantidad']}")
        else:
            print("Producto no encontrado.")

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto a vender: ").strip()
        if producto in inventario:
            datos = inventario[producto]
            if datos['cantidad'] > 0:
                cantidad_vendida = int(input("Ingrese la cantidad a vender: "))
                if cantidad_vendida <= datos['cantidad']:
                    datos['cantidad'] -= cantidad_vendida
                    print(f"Venta registrada: {cantidad_vendida} unidades de {producto}")
                else:
                    print("Cantidad insuficiente en inventario.")
            else:
                print("Producto agotado.")
        else:
            print("Producto no encontrado.")

    elif opcion == "3":
        nuevo_producto = input("Ingrese el nombre del nuevo producto: ").strip()
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        inventario[nuevo_producto] = {"precio": precio, "cantidad": cantidad}
        print(f"Producto {nuevo_producto} agregado al inventario.")

    elif opcion == "4":
        print("\nInventario completo:")
        for producto, datos in inventario.items():
            print(f"{producto} - Precio: ${datos['precio']:.2f}, Cantidad: {datos['cantidad']}")

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida.")
