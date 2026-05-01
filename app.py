import streamlit as st
import pandas as pd
import numpy as np
from libreria_funciones_proyecto1 import calcular_imc #importando la función calcular_imc desde el archivo libreria_funciones_proyecto1.py
from libreria_clases_proyecto1 import EstudianteCurso #importando la clas EstudianteCurso desde el archivo libreria_clases_proyecto1.py

def validar_id(id_input, max_id):  
    if id_input < 1 or id_input > max_id:
        #st.error(f"ID inválido. Ingrese un número entre 1 y {max_id}.")
        return False
    return True


def home():
    #st.title("Especialización en Python")
    
    # Usando HTML para centrar
    st.markdown("<h1 style='text-align: center;'>Especialización en Python</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Módulo 1 - Python Fundamentals</h2>", unsafe_allow_html=True)
    #st.header("Módulo 1 - Python Fundamentals")

    #Centrar imagen con streamlit
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("logo_personal.png", width=300)

   
    st.header("🏠 Bienvenido")       
    st.subheader("Autor: Lloyd Ramírez del Aguila")  

    st.markdown("""
    Hola, soy Ingeniero de sistemas egresado de la UNMSM.
    Apasionado por la programación y el desarrollo de software, asi como la gestion de tecnologías de la información.
    Me encanta aprender nuevas tecnologías y compartir mis conocimientos con la comunidad.
    """)
    st.subheader("Descripción") 
    st.markdown("""
    Esta aplicación está diseñada para mostrar diferentes ejercicios interactivos.
    Usa el menú lateral para navegar entre las secciones.
    """)

    st.subheader("Tecnologías usadas")  
    st.markdown("""
    Esta aplicación se ha desarrollado utilizando Streamlit, una biblioteca de Python que permite crear aplicaciones web interactivas de manera sencilla y rápida.
    Se utiliza Listas, funciones, clases y otras características de Python para implementar la lógica de los ejercicios.
    """)

    st.subheader("Año: 2026")  
    #Centrar imagen con streamlit
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("logo_dmc.png", width=300)
    #st.image("logo_dmc.png", width=300)

#Ejercicio 1:
def ejercicio_1():

    # Lista para almacenar los movimientos
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Descripción del ejercicio
    st.markdown("""
    ### Registro de Movimientos Financieros
    Este módulo permite registrar tus ingresos y gastos realizados, calcular total de ingresos y gastos, asi como mostrar el flujo de caja.
    """)

    # Crear formulario para agrupar inputs y botón
    with st.form("form_movimientos", clear_on_submit=True):
        concepto = st.text_input("Concepto del movimiento")
        tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
        valor = st.number_input("Valor", min_value=0.0, step=1.0)

        # Botones dentro del formulario
        col1, col2 = st.columns(2)
        with col1:
            agregar = st.form_submit_button("Agregar movimiento")
        with col2:
            limpiar = st.form_submit_button("Limpiar movimientos")

        # Lógica de los botones
        if agregar:
            if concepto :
                if valor > 0:
                    st.session_state.movimientos.append({
                        "Concepto": concepto,
                        "Tipo": tipo,
                        "Valor": valor
                    })
                    st.success("Movimiento agregado correctamente")
                else:
                    st.error("El valor debe ser mayor a 0")
            else:
                st.error("Debe ingresar un concepto a registrar")

        if limpiar:
            if st.session_state.movimientos:
                st.session_state.movimientos = []
                st.warning("Lista de movimientos eliminada")
            else:
                st.error("No hay movimientos para limpiar")

    # Mostrar tabla de movimientos
    if st.session_state.movimientos:
        df = pd.DataFrame(st.session_state.movimientos)
        df.index = range(1, len(df) + 1) #modificando el indice por defecto para que empiece desde 1
        df.index.name = "Movimiento" #Agregando nombre a la columna del indice
        st.dataframe(df)

        # Calcular totales
        total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos

        # Mostrar métricas
        st.metric("Total Ingresos", f"S/. {total_ingresos:.2f}")
        st.metric("Total Gastos", f"S/. {total_gastos:.2f}")
        st.metric("Saldo Final", f"S/. {saldo_final:.2f}")

        # Indicar flujo de caja
        if saldo_final >= 0:
            st.success("El flujo de caja está a favor ✅")
        else:
            st.error("El flujo de caja está en contra ❌")


#Ejercicio 2:
def ejercicio_2():
    # Inicializar arrays en session_state
    if "productos" not in st.session_state:
        st.session_state.productos = np.empty((0, 5), dtype=object)  # columnas: nombre, categoría, precio, cantidad, total

    st.markdown("### Registro de Productos con NumPy y DataFrame")
    st.markdown("Este módulo permite registrar productos con NumPy arrays y mostrarlos en un DataFrame.")

    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Electrónica", "Ropa", "Alimentos", "Otros"])
    precio = st.number_input("Precio", min_value=0.0, step=1.0)
    cantidad = st.number_input("Cantidad", min_value=1, step=1)
    total = 0.0
    # Calcular total dinámicamente
    if(precio > 0 and cantidad > 0):
        total = precio * cantidad

    st.metric("Total:", f"S/. {total:.2f}")

    # Formulario de ingreso de datos
    with st.form("form_productos", clear_on_submit=True):

        # Botones dentro del formulario
        col1, col2 = st.columns(2)
        with col1:
            agregar = st.form_submit_button("Agregar Productos")
        with col2:
            limpiar = st.form_submit_button("Limpiar Registros")

        if agregar:
            if nombre :
                if precio > 0:
                    st.session_state.productos = np.vstack([st.session_state.productos, np.array([[nombre, categoria, precio, cantidad, total]], dtype=object)])
                    st.success("Producto agregado correctamente")
                else:
                    st.error("El precio debe ser mayor a 0")
            else:
                st.error("Debe ingresar un nombre del producto")

        if limpiar:
            if st.session_state.productos.size > 0:
                st.session_state.productos = np.empty((0, 5), dtype=object)
                st.warning("Lista de productos eliminada")
            else:
                st.error("No hay productos para limpiar")

    # Convertir a DataFrame y mostrar
    if st.session_state.productos.shape[0] > 0:
        columnas = ["Producto", "Categoría", "Precio", "Cantidad", "Total"]
        df = pd.DataFrame(st.session_state.productos, columns=columnas)

        # Agregar índice desde 1 con nombre "Registro"
        df.index = range(1, len(df) + 1)
        df.index.name = "Item"

        st.dataframe(df)

#Ejercicio 3:
def ejercicio_3():
    
    if "imc_historico" not in st.session_state:
        st.session_state["imc_historico"] = []

    st.markdown("### Cálculo del IMC")
    st.markdown("Este módulo permite calcular el Índice de Masa Corporal (IMC) de una persona usando la función `calcular_imc`.")

    # Opcion para seleccionar función a ejecutar, se podria expandir para incluir otras funciones en el futuro
    funcion = st.selectbox("Selecciona la función", ["calcular_imc"])

    # ingresar los parámetros de la funcion
    peso = st.number_input("Peso (kg)", min_value=0.0, step=1.0)
    altura = st.number_input("Altura (m)", min_value=0.0, step=0.1)

    # Botón para ejecutar
    if st.button("Calcular"):
        if funcion == "calcular_imc":
            if peso <= 0:
                st.error("El peso debe ser mayor a 0")
                return
            else:
                if altura <= 0:
                    st.error("La altura debe ser mayor a 0")
                    return
            
            resultado = calcular_imc(peso, altura)
            
            # Mostrar resultado
            st.write("### Resultado")
            st.write(f"IMC: **{resultado['imc']}**")
            st.write(f"Clasificación: **{resultado['clasificacion']}**")
            
            # Guardar en histórico
            st.session_state["imc_historico"].append({
                "Peso (kg)": peso,
                "Altura (m)": altura,
                "IMC": resultado["imc"],
                "Clasificación": resultado["clasificacion"]
            })

    # Mostrar histórico en DataFrame
    if st.session_state["imc_historico"]:
        df = pd.DataFrame(st.session_state["imc_historico"])
        df.index = df.index + 1
        df.index.name = "Registro"
        st.write("### Histórico de resultados")
        st.dataframe(df)

def resumen_estudiante(placeholder=None):
    if st.session_state["registro_estudiantes"]:
        df = pd.DataFrame([registro["resumen"] for registro in st.session_state["registro_estudiantes"]])
        df.index = df.index + 1
        df.index.name = "ID"
        if placeholder:
            placeholder.dataframe(df)
        else:
            st.dataframe(df)
    else:
        if placeholder:
            placeholder.info("No hay registros aún.")
        else:
            st.info("No hay registros aún.")

#Ejercicio 4:
def ejercicio_4():      
    # Inicializar lista de registro de estudiantes en session_state
    if "registro_estudiantes" not in st.session_state:
        st.session_state["registro_estudiantes"] = []

    st.markdown("""
    Este módulo permite **crear, leer, actualizar y eliminar** registros de estudiantes  
    utilizando la clase `EstudianteCurso`.
    """)
    #placeholder = st.empty()

    # Crear pestañas
    tab_crear, tab_buscar, tab_resumen,tab_detalle, tab_actualizar, tab_eliminar = st.tabs(["➕ Crear", "🔍 Buscar", "📝 Resumen", "📖 Detalle", "✏️ Actualizar", "🗑️ Eliminar"])
    
    # --- CREAR ---
    with tab_crear:
        st.header("👤 Nuevo Estudiante")
        st.markdown("Ingrese los datos del estudiante para calcular su nota final y estado.")
        st.markdown("**El nombre es un campo obligatorio. Las notas deben estar entre 0 y 20. Los pesos deben estar entre 0% y 100%.")
        
        with st.form("form_crear"):
            nombre = st.text_input("Nombre del estudiante")
            actividades = st.number_input("Nota actividades", 0.0, 20.0, step=0.1)
            proyecto = st.number_input("Nota proyecto", 0.0, 20.0, step=0.1)
            examen_final = st.number_input("Nota examen final", 0.0, 20.0, step=0.1)
            peso_actividades = st.number_input("Peso actividades (%)", 0.0, 100.0, step=1.0)
            peso_proyecto = st.number_input("Peso proyecto (%)", 0.0, 100.0, step=1.0)
            peso_examen_final = st.number_input("Peso examen final (%)", 0.0, 100.0, step=1.0)
            total_clases = st.number_input("Total clases", 1, 100, step=1)
            clases_asistidas = st.number_input("Clases asistidas", 0, 100, step=1)

            submitted = st.form_submit_button("Agregar Estudiante")

            if submitted:
                try:
                    if nombre.strip() == "":
                        st.error("El nombre del estudiante no puede estar vacío.")
                    else:
                        estudiante = EstudianteCurso(
                            nombre, actividades, proyecto, examen_final,
                            peso_actividades, peso_proyecto, peso_examen_final,
                            total_clases, clases_asistidas
                        )
                        #st.session_state["registro_estudiantes"].append(estudiante.resumen())
                        st.session_state["registro_estudiantes"].append({
                            "datos_estudiante": estudiante.get_datos(),
                            "resumen": estudiante.resumen()
                        })
                        st.success(f"Estudiante {nombre} agregado correctamente.")
                        
                except Exception as e:
                    st.error(f"Error: {e}")

    # --- Buscar ---
    with tab_buscar:
        # Buscar por ID
        st.header("👤 Buscar estudiante por ID")
        st.markdown("Ingrese el ID del estudiante para ver su detalle. El ID corresponde al número de registro mostrado en la tabla de resumen.")
        st.markdown("**La nota final se obtiene de la sumatoria ponderada de las notas de actividades, proyecto y examen final. La asistencia se calcula como el porcentaje de clases asistidas sobre el total de clases. El estado se determina según la nota final y la asistencia.")
        st.markdown("**La nota minima para aprobar es 11 y la asistencia minima es 75%.")
        if st.session_state["registro_estudiantes"]:
            df = pd.DataFrame(st.session_state["registro_estudiantes"])

            id_buscar = st.number_input("Ingrese ID", 1, step=1)
            if st.button("Buscar"):
                if(validar_id(id_buscar, len(df))):
                    registro = st.session_state["registro_estudiantes"][id_buscar-1]
                    #st.write("### Detalle del registro")
                    #for clave, valor in registro.items():
                    #    st.write(f"**{clave}:** {valor}")
                    # Mostrar primero el nombre del estudiante
                    #st.write(f"### Estudiante: {registro['estudiante']}")
                    st.write(f"### Estudiante: {registro['resumen']['estudiante']}")

                    # Mostrar datos crudos
                    st.write("### Datos del estudiante")
                    for clave, valor in registro["datos_estudiante"].items():
                        st.write(f"**{clave}:** {valor}")

                    # Mostrar resumen
                    resumen = registro["resumen"]
                    st.write("### Resumen")
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Nota final", resumen["nota_final"])
                    col2.metric("Asistencia (%)", resumen["asistencia_pct"])
                    col3.metric("Estado", resumen["estado"])
                else:
                    st.error("ID no registrado.")
                        
        else:
            st.info("No hay registros aún.")


    # --- Listar resumen de los estudiantes ---
    with tab_resumen:
        st.header("👤 Resumen de Estudiantes")
        st.markdown("Se muestra un resumen de cada estudiante con su nota final, porcentaje de asistencia y estado (Aprobado/No Aprobado).")
        st.markdown("**La nota minima para aprobar es 11 y la asistencia minima es 75%.**")
        resumen_estudiante()

    # --- Detalle de todos los valores ingresados para los estudiantes ---
    with tab_detalle:
        st.header("👤 Detalle de Estudiantes")
        st.markdown("Se muestra el detalle de cada estudiante con todos sus datos, incluyendo su nota final, porcentaje de asistencia y estado (Aprobado/No Aprobado).")
        st.markdown("**La nota minima para aprobar es 11 y la asistencia minima es 75%.")
        if st.session_state["registro_estudiantes"]:
            registros_ordenados = []
            for registro in st.session_state["registro_estudiantes"]:
                resumen = registro["resumen"]
                datos = registro["datos_estudiante"]

                # Construir un diccionario ordenado
                registro_ordenado = {
                    "estudiante": resumen["estudiante"],   # primero el nombre
                    **datos,                               # luego los datos crudos
                    "nota_final": resumen["nota_final"],   # después los demás campos del resumen
                    "asistencia_pct": resumen["asistencia_pct"],
                    "estado": resumen["estado"]
                }
                registros_ordenados.append(registro_ordenado)

            # Crear el DataFrame con el orden definido
            df = pd.DataFrame(registros_ordenados)
            df.index = df.index + 1
            df.index.name = "ID"
            st.dataframe(df)
        else:
            st.info("No hay registros aún.")


    # --- ACTUALIZAR ---
    with tab_actualizar:
        st.header("👤 Actualizar Estudiante")
        st.markdown("Ingrese el ID del estudiante que desea actualizar. Luego modifique los campos necesarios y presione el botón de actualizar.")
        st.markdown("**Recuerde que el nombre es un campo obligatorio. Las notas deben estar entre 0 y 20. Los pesos deben estar entre 0% y 100%.")

        if "mensaje_actualizacion" in st.session_state:
            st.success(st.session_state["mensaje_actualizacion"])
            del st.session_state["mensaje_actualizacion"]

        if st.session_state["registro_estudiantes"]:
            id_actualizar = st.number_input("ID a actualizar", 1, step=1)

            if(validar_id(id_actualizar, len(df))):
                registro = st.session_state["registro_estudiantes"][id_actualizar-1]
                datos = registro["datos_estudiante"]

                # Formulario con valores actuales
                with st.form("form_actualizar"):
                    nombre = st.text_input("Nombre del estudiante", registro["resumen"]["estudiante"])
                    actividades = st.number_input("Nota actividades", 0.0, 20.0, step=0.1, value=datos["actividades"])
                    proyecto = st.number_input("Nota proyecto", 0.0, 20.0, step=0.1, value=datos["proyecto"])
                    examen_final = st.number_input("Nota examen final", 0.0, 20.0, step=0.1, value=datos["examen_final"])
                    peso_actividades = st.number_input("Peso actividades (%)", 0.0, 100.0, step=1.0, value=datos["peso_actividades"])
                    peso_proyecto = st.number_input("Peso proyecto (%)", 0.0, 100.0, step=1.0, value=datos["peso_proyecto"])
                    peso_examen_final = st.number_input("Peso examen final (%)", 0.0, 100.0, step=1.0, value=datos["peso_examen_final"])
                    total_clases = st.number_input("Total clases", 1, 100, step=1, value=datos["total_clases"])
                    clases_asistidas = st.number_input("Clases asistidas", 0, 100, step=1, value=datos["clases_asistidas"])

                    submitted = st.form_submit_button("Actualizar Estudiante")

                    if submitted:
                        try:
                            if nombre.strip() == "":
                                st.error("El nombre del estudiante no puede estar vacío.")
                            else:
                                estudiante = EstudianteCurso(
                                    nombre, actividades, proyecto, examen_final,
                                    peso_actividades, peso_proyecto, peso_examen_final,
                                    total_clases, clases_asistidas
                                )
                                st.session_state["registro_estudiantes"][id_actualizar-1] = {
                                    "datos_estudiante": estudiante.get_datos(),
                                    "resumen": estudiante.resumen()
                                }
                                
                                #st.success(f"Estudiante {nombre} actualizado correctamente.")
                                #st.rerun()
                                # Guardar flag de éxito
                                st.session_state["mensaje_actualizacion"] = f"Estudiante {nombre} actualizado correctamente."
                                st.rerun()
                                
                        except Exception as e:
                            #st.error(f"Error: {e}")
                            st.session_state["mensaje_actualizacion"] = f"Error: {e}"
                            st.rerun()
            else:
                st.error("ID no registrado.")
        else:
            st.info("No hay registros para actualizar.")



    # --- ELIMINAR ---
    with tab_eliminar:
        st.header("👤 Eliminar Estudiante por ID")
        st.markdown("Ingrese el ID del estudiante que desea eliminar y presione el botón de eliminar.")

        if "mensaje_eliminar" in st.session_state:
            st.success(st.session_state["mensaje_eliminar"])
            del st.session_state["mensaje_eliminar"]

        if st.session_state["registro_estudiantes"]:           
            id_eliminar = st.number_input("ID a eliminar", 1, step=1)
            btn_eliminar = st.button("Eliminar")           
            resumen_estudiante()
            if btn_eliminar:
                if(validar_id(id_eliminar, len(df))):
                    eliminado = st.session_state["registro_estudiantes"].pop(id_eliminar-1)
                    #st.success(f"Registro eliminado: {eliminado['resumen']['estudiante']}")
                    #st.rerun()
                    st.session_state["mensaje_eliminar"] = f"Registro eliminado: {eliminado['resumen']['estudiante']}"
                    st.rerun()
                else:
                    st.error("ID no registrado.")
        else:
            st.info("No hay registros para eliminar.")



#Aplicación Principal

# Configuración de la página de la aplicacion con streamlit
#st.set_page_config(page_title="Mi App en Streamlit", page_icon=":bar_chart:", layout="wide")
st.set_page_config(page_title="Mi App en Streamlit", page_icon="logo_personal.png", layout="wide")

# Menú lateral
menu = st.sidebar.selectbox(
    "Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# Contenido según la opción seleccionada
if menu == "Home":
   home()

elif menu == "Ejercicio 1":
    st.header("Ejercicio 1")
    ejercicio_1()


elif menu == "Ejercicio 2":
    st.header("Ejercicio 2")
    ejercicio_2()

elif menu == "Ejercicio 3":
    st.header("Ejercicio 3")
    ejercicio_3()

elif menu == "Ejercicio 4":
    st.header("Ejercicio 4")
    ejercicio_4()


