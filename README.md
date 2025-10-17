# 📅 Agenda de Contactos en Python (Consola)

Una aplicación simple de **agenda de contactos** hecha en **Python**, con funcionalidades **CRUD** (Crear, Leer, Actualizar, Eliminar) y almacenamiento en un archivo JSON.

Además, cuenta con **pruebas unitarias (pytest)**, **verificación de estilo (flake8/pylint)** y **pipeline de integración continua (GitHub Actions)**.

---

## 🚀 Características

- 🧠 CRUD completo por consola
- 💾 Persistencia de datos en `agenda.json`
- ✅ Pruebas unitarias con `pytest`
- 📊 Cobertura de código con `coverage`
- 🧹 Estilo de código validado con `flake8` o `pylint`
- ⚙️ CI/CD automatizado con **GitHub Actions**

---

## 🏗️ Instalación y ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/<TU_USUARIO>/<TU_REPO>.git
cd <TU_REPO>
2️⃣ Crear entorno virtual
bash
Copiar código
python -m venv env
3️⃣ Activar el entorno virtual
En Windows:

bash
Copiar código
.\env\Scripts\activate
En Linux / macOS:

bash
Copiar código
source env/bin/activate
4️⃣ Instalar dependencias
bash
Copiar código
pip install -r requirements.txt
5️⃣ Ejecutar la agenda
bash
Copiar código
python agenda.py
🧪 Pruebas unitarias
Ejecuta todas las pruebas con:

bash
Copiar código
pytest -v
Ver reporte de cobertura:
bash
Copiar código
coverage run -m pytest
coverage report
coverage html
Abre luego htmlcov/index.html en tu navegador.

⚙️ Verificación de estilo
bash
Copiar código
flake8 agenda.py
# o
pylint agenda.py
🧰 Estructura del proyecto
bash
Copiar código
agenda/
│
├── agenda.py                # Lógica principal (CRUD)
├── agenda.json              # Archivo de datos (se crea automáticamente)
├── requirements.txt          # Dependencias
├── tests/
│   └── test_agenda.py       # Pruebas unitarias
└── .github/
    └── workflows/
        └── tests.yml        # Workflow CI de GitHub Actions
💡 Ejemplo de uso
markdown
Copiar código
===== 📅 AGENDA DE CONTACTOS =====
1. Agregar contacto
2. Mostrar contactos
3. Actualizar contacto
4. Eliminar contacto
5. Salir
==================================
Selecciona una opción: 1
Nombre: Juan Pérez
Teléfono: 0991234567
Email: juan@mail.com
✅ Contacto agregado correctamente.
🧾 Licencia
Este proyecto está disponible bajo la licencia MIT.

Si te gustó este proyecto, ¡dale una ⭐ en GitHub!

yaml
Copiar código
