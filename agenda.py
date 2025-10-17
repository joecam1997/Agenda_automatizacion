import json
import os

ARCHIVO = "agenda.json"

# --- Funciones auxiliares ---
def cargar_contactos():
    """Carga los contactos desde el archivo JSON."""
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_contactos(contactos):
    """Guarda los contactos en el archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=4, ensure_ascii=False)

# --- Funciones CRUD ---
def crear_contacto(contactos):
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    
    # Verificar si ya existe
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            print("⚠️ El contacto ya existe.")
            return
    
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(contacto)
    guardar_contactos(contactos)
    print("✅ Contacto agregado correctamente.")

def mostrar_contactos(contactos):
    if not contactos:
        print("📭 No hay contactos en la agenda.")
        return
    
    print("\n--- 📒 Lista de Contactos ---")
    for i, c in enumerate(contactos, 1):
        print(f"{i}. {c['nombre']} | Tel: {c['telefono']} | Email: {c['email']}")
    print("-----------------------------\n")

def actualizar_contacto(contactos):
    mostrar_contactos(contactos)
    nombre = input("Ingrese el nombre del contacto a actualizar: ").strip()
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            print("Deja en blanco si no deseas cambiar un campo.")
            nuevo_telefono = input(f"Nuevo teléfono ({c['telefono']}): ").strip()
            nuevo_email = input(f"Nuevo email ({c['email']}): ").strip()

            if nuevo_telefono:
                c["telefono"] = nuevo_telefono
            if nuevo_email:
                c["email"] = nuevo_email

            guardar_contactos(contactos)
            print("✅ Contacto actualizado.")
            return
    print("❌ No se encontró ese contacto.")

def eliminar_contacto(contactos):
    mostrar_contactos(contactos)
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            contactos.remove(c)
            guardar_contactos(contactos)
            print("🗑️ Contacto eliminado correctamente.")
            return
    print("❌ No se encontró ese contacto.")

# --- Menú principal ---
def menu():
    contactos = cargar_contactos()
    while True:
        print("""
===== 📅 AGENDA DE CONTACTOS =====
1. Agregar contacto
2. Mostrar contactos
3. Actualizar contacto
4. Eliminar contacto
5. Salir
==================================
""")
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            crear_contacto(contactos)
        elif opcion == "2":
            mostrar_contactos(contactos)
        elif opcion == "3":
            actualizar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
