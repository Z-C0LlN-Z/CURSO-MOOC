import streamlit as st

st.set_page_config(
    page_title="MOOC - Jabón Artesanal",
    page_icon="🧼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "progreso" not in st.session_state:
    st.session_state.progreso = 0

if "opcion" not in st.session_state:
    st.session_state.opcion = "Inicio"

MODULOS = [
    ("Inicio", "🏠"),
    ("Introducción", "📚"),
    ("Materiales", "🧴"),
    ("Elaboración", "🎥"),
    ("Variantes", "🌿"),
    ("Seguridad", "🛡️"),
    ("Evaluación", "📝"),
    ("Finalizar", "🎓"),
]

# ----------------------------
# ESTILO GLOBAL MODERNO (dark, tipo Framer)
# ----------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    /* Oculta el sidebar nativo y el menú/footer por defecto */
    section[data-testid="stSidebar"] { display: none; }
    #MainMenu, footer { visibility: hidden; }

    .stApp {
        background-color: #0d0d0f;
        color: #f5f5f5;
    }

    /* Quita el padding superior por defecto para que la navbar quede pegada */
    .block-container {
        padding-top: 0rem;
        max-width: 1100px;
    }

    /* ---------- NAVBAR SUPERIOR ---------- */
    .navbar {
        position: sticky;
        top: 0;
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 28px;
        margin: 0 -28px 0 -28px;
        background: rgba(13, 13, 15, 0.85);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255,255,255,0.08);
    }

    .navbar-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        font-weight: 800;
        font-size: 1.1rem;
        color: #ffffff;
        letter-spacing: -0.02em;
    }

    .navbar-progress-text {
        font-size: 0.8rem;
        color: #9a9a9f;
        font-weight: 500;
    }

    /* Barra de progreso delgada bajo la navbar */
    .progress-track {
        height: 3px;
        width: 100%;
        background: rgba(255,255,255,0.08);
        margin: 0 -28px 28px -28px;
    }
    .progress-fill {
        height: 3px;
        background: linear-gradient(90deg, #a6ff4d, #4dd6ff);
        transition: width 0.4s ease;
    }

    /* ---------- BOTONES DE NAVEGACIÓN (usados dentro de columnas) ---------- */
    div[data-testid="column"] .stButton > button {
        width: 100%;
        background: transparent;
        color: #c9c9cf;
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 8px;
        padding: 8px 6px;
        font-weight: 600;
        font-size: 0.82rem;
        transition: all 0.15s ease;
    }

    div[data-testid="column"] .stButton > button:hover {
        border-color: rgba(255,255,255,0.35);
        color: #ffffff;
        background: rgba(255,255,255,0.06);
    }

    /* Botón activo (marcado vía type="primary") */
    div[data-testid="column"] .stButton > button[kind="primary"] {
        background: #ffffff;
        color: #0d0d0f;
        border: 1px solid #ffffff;
    }
    div[data-testid="column"] .stButton > button[kind="primary"]:hover {
        background: #e9e9e9;
        color: #0d0d0f;
    }

    /* ---------- TIPOGRAFÍA GENERAL ---------- */
    h1 {
        font-weight: 800 !important;
        letter-spacing: -0.03em;
        color: #ffffff !important;
    }
    h2, h3 {
        font-weight: 700 !important;
        letter-spacing: -0.02em;
        color: #ffffff !important;
    }
    p, li, span, label {
        color: #c9c9cf;
    }

    hr {
        border-color: rgba(255,255,255,0.08) !important;
    }

    /* Cajas de info/success/error con borde sutil, fondo oscuro */
    div[data-testid="stAlert"] {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 10px;
    }

    /* Expanders */
    details {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 10px;
    }

    /* Inputs */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.04);
        color: #ffffff;
        border: 1px solid rgba(255,255,255,0.12);
    }

    /* Botones normales (Comenzar Curso, Calificar, etc.) */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# NAVBAR SUPERIOR
# ----------------------------
st.markdown("""
<div class="navbar">
    <div class="navbar-brand">🧼 Curso MOOC</div>
    <div class="navbar-progress-text">Progreso: {progreso}%</div>
</div>
""".format(progreso=st.session_state.progreso), unsafe_allow_html=True)

st.markdown(f"""
<div class="progress-track">
    <div class="progress-fill" style="width:{st.session_state.progreso}%;"></div>
</div>
""", unsafe_allow_html=True)

nav_cols = st.columns(len(MODULOS))
for col, (nombre, icono) in zip(nav_cols, MODULOS):
    with col:
        es_activo = st.session_state.opcion == nombre
        if st.button(
            f"{icono}  {nombre}",
            key=f"nav_{nombre}",
            type="primary" if es_activo else "secondary",
            use_container_width=True
        ):
            st.session_state.opcion = nombre

st.write("")

opcion_nombre = st.session_state.opcion

if opcion_nombre == "Inicio":

    st.session_state.progreso = 10

    st.title("🧼 Elaboración de Jabón Artesanal de Avena y Miel")

    st.markdown("---")

    st.header("Bienvenido")

    st.write("""
Este curso tiene como finalidad enseñar el proceso para elaborar un jabón artesanal utilizando materiales fáciles de conseguir.

Durante el curso aprenderás los materiales necesarios, el procedimiento completo, distintas variantes de la receta, recomendaciones de seguridad y algunas ideas para presentar tu producto terminado.
""")

    st.header("Integrantes")

    st.write("""
- Nombre 1
- Nombre 2
- Nombre 3
""")

    col_dur, col_niv, col_mod = st.columns(3)

    with col_dur:
        st.header("Duración")
        st.success("28 minutos")

    with col_niv:
        st.header("Nivel")
        st.info("Principiante")

    with col_mod:
        st.header("Módulos")
        st.info(f"{len(MODULOS)} secciones")

    st.header("Objetivo General")

    st.info("""
Al finalizar el curso el participante será capaz de elaborar un jabón artesanal de avena y miel, conocer sus variantes y aplicar las medidas de seguridad correspondientes, utilizando jabón blanco neutro como base.
""")

    st.header("Objetivos Específicos")

    st.write("""
- Reconocer los materiales y herramientas necesarias para el proceso.

- Aplicar correctamente la técnica de fusión y vertido (melt & pour).

- Adaptar la receta base creando variantes con distintos ingredientes.

- Identificar riesgos comunes y aplicar medidas de seguridad e higiene.

- Evaluar el resultado final y presentar el producto terminado.
""")

    st.header("Competencias")

    st.write("""
✅ Identificar los materiales.

✅ Elaborar correctamente el jabón.

✅ Crear variantes personalizadas de la receta.

✅ Aplicar medidas básicas de seguridad.

✅ Presentar el producto terminado.
""")

    st.header("¿Para quién es este curso?")

    st.write("""
Este curso está diseñado para cualquier persona interesada en el mundo del DIY (hazlo tú mismo), emprendedores que buscan iniciar un pequeño negocio de cosmética natural, o simplemente quienes desean aprender una habilidad nueva y útil. No se requiere experiencia previa.
""")

    st.button("Comenzar Curso")

elif opcion_nombre == "Introducción":

    st.session_state.progreso = 20

    st.title("📚 Introducción")

    st.write("""
Los jabones artesanales son productos elaborados manualmente utilizando ingredientes naturales o comerciales que permiten personalizar su aroma, textura y propiedades.

En este curso utilizaremos un método sencillo llamado **melt & pour** (fundir y verter), que consiste en reutilizar jabón blanco neutro y enriquecerlo con avena y miel.
""")

    st.subheader("Breve historia del jabón")

    st.write("""
La elaboración de jabón se remonta a miles de años atrás, con registros de civilizaciones antiguas mezclando grasas con cenizas vegetales. Con el tiempo, la técnica evolucionó hacia procesos más controlados como la saponificación en frío y, más recientemente, hacia métodos accesibles como el melt & pour, ideal para principiantes porque no requiere manejar sosa cáustica directamente.
""")

    st.subheader("Tipos de elaboración de jabón")

    tabla_tipos = {
        "Método": ["Melt & Pour", "Saponificación en frío (Cold Process)", "Saponificación en caliente (Hot Process)"],
        "Dificultad": ["Baja", "Alta", "Media"],
        "Tiempo de curado": ["Ninguno", "4-6 semanas", "1-2 días"],
        "Ideal para": ["Principiantes", "Avanzados", "Intermedios"]
    }
    st.table(tabla_tipos)

    st.info("Este curso utiliza el método **Melt & Pour**, el más seguro y rápido para comenzar.")

    st.subheader("¿Por qué usar avena?")

    st.write("""
La avena ayuda a exfoliar suavemente la piel y aporta una sensación de limpieza natural. Además, contiene compuestos llamados avenantramidas, conocidos por su efecto calmante sobre la piel irritada.
""")

    st.subheader("¿Por qué usar miel?")

    st.write("""
La miel posee propiedades humectantes que ayudan a mantener la piel hidratada. También tiene propiedades antibacterianas naturales, lo que la convierte en un ingrediente muy apreciado en cosmética natural.
""")

    st.subheader("Beneficios de los jabones artesanales")

    col_a, col_b = st.columns(2)

    with col_a:
        st.write("""
**Para la piel:**
- Menor cantidad de químicos agresivos.
- Ingredientes personalizables según el tipo de piel.
- Glicerina natural conservada (a diferencia de muchos jabones industriales).
""")

    with col_b:
        st.write("""
**Para el medio ambiente y economía:**
- Reduce el uso de plásticos al reutilizar moldes.
- Posibilidad de emprendimiento a baja escala.
- Aprovechamiento de ingredientes locales y de temporada.
""")

    st.subheader("Lo que aprenderás")

    st.write("""
- Materiales y herramientas necesarias.

- Preparación paso a paso con el método melt & pour.

- Variantes de la receta base (chocolate, lavanda, carbón activado, entre otras).

- Medidas de seguridad e higiene durante el proceso.

- Consejos para evitar errores comunes.

- Presentación final del producto.
""")

    st.success("Cuando termines este módulo continúa con 'Materiales'.")

elif opcion_nombre == "Materiales":

    st.session_state.progreso = 35

    st.title("🧴 Materiales")

    st.markdown("---")

    st.header("Materiales base")

    materiales = [
        "2 barras de jabón blanco neutro (aprox. 300 g)",
        "2 cucharadas de avena en hojuelas",
        "1 cucharada de miel natural",
        "2 cucharadas de agua"
    ]

    for material in materiales:
        st.checkbox(material, disabled=True)

    st.header("Ingredientes opcionales")

    st.write("Puedes añadir alguno de estos para personalizar tu jabón:")

    opcionales = [
        "5-8 gotas de aceite esencial (lavanda, manzanilla, romero)",
        "1 cucharadita de aceite vegetal (coco, oliva o almendras)",
        "Colorante cosmético (opcional, en pequeña cantidad)",
        "Pétalos secos de flores comestibles para decorar"
    ]

    for opcional in opcionales:
        st.checkbox(opcional, disabled=True)

    st.header("Herramientas")

    herramientas = [
        "Rallador",
        "Cuchillo",
        "Tabla para cortar",
        "Recipiente resistente al calor",
        "Olla para baño María o microondas",
        "Cuchara o espátula",
        "Molde de silicona",
        "Báscula de cocina (opcional, para mayor precisión)",
        "Guantes de cocina o agarraderas"
    ]

    for herramienta in herramientas:
        st.checkbox(herramienta, disabled=True)

    st.header("Tabla de proporciones")

    st.write("Si quieres elaborar una cantidad distinta, usa esta tabla como referencia:")

    tabla_proporciones = {
        "Tamaño del lote": ["Pequeño (1 barra)", "Mediano (2 barras)", "Grande (4 barras)"],
        "Jabón base": ["150 g", "300 g", "600 g"],
        "Avena": ["1 cda", "2 cdas", "4 cdas"],
        "Miel": ["1/2 cda", "1 cda", "2 cdas"],
        "Agua": ["1 cda", "2 cdas", "4 cdas"]
    }
    st.table(tabla_proporciones)

    st.header("Sustitutos posibles")

    with st.expander("¿No tienes algún ingrediente? Aquí algunas alternativas"):
        st.write("""
- **Miel** → se puede sustituir por glicerina líquida o jarabe de agave.
- **Avena en hojuelas** → se puede usar avena molida (textura más suave) o cáscara de almendra molida (mayor exfoliación).
- **Jabón blanco neutro** → puede sustituirse por base de jabón glicerinada transparente.
- **Aceite esencial** → puedes omitirlo si tienes piel sensible o usar extracto de vainilla en su lugar.
""")

    st.header("Costo aproximado")

    st.info("""
Con los materiales base puedes elaborar entre 3 y 4 barras de jabón. El costo aproximado por barra suele ser muy bajo comparado con jabones artesanales comerciales, lo que lo convierte en una excelente opción tanto para uso personal como para emprendimiento.
""")

    st.header("Consejos")

    st.info("""
Trabaja siempre sobre una mesa limpia.

Lávate las manos antes de comenzar.

Utiliza utensilios únicamente para la elaboración del jabón.

No calientes el jabón directamente sobre el fuego.

Verifica que todos los materiales estén a temperatura ambiente antes de iniciar.
""")

    st.success("Ya conoces todos los materiales necesarios.")

elif opcion_nombre == "Elaboración":

    st.session_state.progreso = 50

    st.title("🎥 Elaboración del Jabón")

    st.video("video.mp4")

    st.markdown("---")

    st.write("Tiempo estimado total: **30-40 minutos activos** + 2-4 horas de reposo.")

    pasos = [
        (
            "Paso 1 · Rallar el jabón (5 min)",
            """
Ralla completamente las dos barras de jabón blanco.

Mientras más fino quede el rallado, más rápido se derretirá y más uniforme quedará la mezcla.
"""
        ),
        (
            "Paso 2 · Preparar el recipiente (2 min)",
            """
Coloca el jabón rallado dentro de un recipiente resistente al calor.

Agrega dos cucharadas de agua. El agua ayuda a que el jabón se funda de manera más homogénea.
"""
        ),
        (
            "Paso 3 · Fundir el jabón (8-10 min)",
            """
Calienta el recipiente a baño María, o en intervalos cortos de 20 segundos si usas microondas.

Mezcla constantemente hasta obtener una pasta uniforme, sin grumos.
"""
        ),
        (
            "Paso 4 · Incorporar la miel (3 min)",
            """
Retira del calor y agrega una cucharada de miel.

Mezcla lentamente para incorporarla completamente sin generar demasiadas burbujas.
"""
        ),
        (
            "Paso 5 · Añadir la avena (3 min)",
            """
Añade las dos cucharadas de avena.

Continúa mezclando hasta distribuir todos los ingredientes de manera uniforme.

Aquí también puedes agregar tus ingredientes opcionales (aceite esencial, colorante, etc.)
"""
        ),
        (
            "Paso 6 · Verter en el molde (3 min)",
            """
Vierte la mezcla en un molde de silicona mientras aún está líquida y tibia.

Golpea ligeramente el molde contra la mesa para eliminar burbujas de aire atrapadas.
"""
        ),
        (
            "Paso 7 · Reposo y desmolde (2-4 horas)",
            """
Deja reposar el molde en un lugar fresco, alejado de la luz directa, hasta que el jabón endurezca por completo.

Para acelerar el proceso puedes refrigerarlo entre 30 y 45 minutos, sin congelarlo.

Finalmente, desmolda cuidadosamente presionando los bordes del molde de silicona.
"""
        ),
        (
            "Paso 8 · Curado final (24 horas, opcional)",
            """
Aunque el jabón melt & pour se puede usar de inmediato, dejarlo reposar 24 horas al aire libre ayuda a que se endurezca aún más y dure más tiempo en uso.
"""
        )
    ]

    for titulo, descripcion in pasos:
        with st.expander(titulo):
            st.write(descripcion)

    st.header("Resultado esperado")

    st.success("""
Obtendrás un jabón artesanal de avena y miel, de textura firme, color dorado claro y aroma suave, listo para utilizarse o regalarse.
""")

    st.header("Errores comunes y cómo solucionarlos")

    tabla_errores = {
        "Problema": [
            "El jabón queda muy blando",
            "Aparecen burbujas de aire",
            "El jabón se ve grumoso",
            "El jabón suda o libera gotas"
        ],
        "Causa probable": [
            "Exceso de agua o miel",
            "Mezcla vertida demasiado rápido",
            "Jabón no se fundió por completo",
            "Exceso de humedad ambiental"
        ],
        "Solución": [
            "Reducir cantidad de líquidos en el próximo lote",
            "Verter despacio y golpear el molde antes de que enfríe",
            "Calentar más tiempo, mezclando constantemente",
            "Guardar en un lugar seco y fresco, evitar envolver de inmediato"
        ]
    }
    st.table(tabla_errores)

    st.header("Recomendaciones")

    st.write("""
• No calientes demasiado el jabón, ya que puede perder propiedades.

• Mezcla constantemente para evitar grumos.

• Utiliza moldes de silicona para facilitar el desmoldado.

• Espera el tiempo suficiente antes de desmoldar.

• Guarda el jabón en un lugar fresco y seco, alejado de la humedad directa.

• Si vas a regalarlo, envuélvelo solo cuando esté completamente seco y firme.
""")

elif opcion_nombre == "Variantes":

    st.session_state.progreso = 65

    st.title("🌿 Variantes de la Receta")

    st.write("""
Una vez que domines la receta base de avena y miel, puedes experimentar con estas variantes para crear distintos tipos de jabón.
""")

    st.markdown("---")

    variantes = [
        (
            "🍫 Jabón de chocolate y avena",
            """
**Ingredientes adicionales:** 1 cucharadita de cacao en polvo sin azúcar.

**Beneficio:** aroma intenso y propiedades antioxidantes del cacao.

**Cómo hacerlo:** agrega el cacao junto con la avena en el Paso 5 y mezcla bien para evitar grumos.
"""
        ),
        (
            "💜 Jabón de lavanda relajante",
            """
**Ingredientes adicionales:** 6-8 gotas de aceite esencial de lavanda y colorante morado opcional.

**Beneficio:** efecto relajante, ideal para usar antes de dormir.

**Cómo hacerlo:** agrega el aceite esencial justo antes de verter en el molde, para conservar mejor el aroma.
"""
        ),
        (
            "⚫ Jabón detox de carbón activado",
            """
**Ingredientes adicionales:** 1/2 cucharadita de carbón activado en polvo.

**Beneficio:** ayuda a absorber impurezas y exceso de grasa en la piel.

**Cómo hacerlo:** disuelve el carbón en una cucharadita de agua tibia antes de incorporarlo a la mezcla, para evitar grumos oscuros.
"""
        ),
        (
            "🍋 Jabón cítrico energizante",
            """
**Ingredientes adicionales:** ralladura de un limón y 5 gotas de aceite esencial de naranja.

**Beneficio:** aroma fresco y efecto energizante, ideal para las mañanas.

**Cómo hacerlo:** agrega la ralladura junto con la avena para un efecto exfoliante extra.
"""
        ),
        (
            "🌹 Jabón decorativo con pétalos",
            """
**Ingredientes adicionales:** pétalos secos de rosa o caléndula.

**Beneficio:** valor estético, ideal para regalar.

**Cómo hacerlo:** coloca algunos pétalos en el fondo del molde antes de verter la mezcla, para que queden visibles al desmoldar.
"""
        )
    ]

    for titulo, descripcion in variantes:
        with st.expander(titulo):
            st.write(descripcion)

    st.header("Tabla comparativa de variantes")

    tabla_variantes = {
        "Variante": ["Chocolate", "Lavanda", "Carbón activado", "Cítrico", "Pétalos"],
        "Tipo de piel recomendada": ["Normal a seca", "Todo tipo", "Grasa/mixta", "Normal", "Todo tipo"],
        "Dificultad extra": ["Baja", "Baja", "Media", "Baja", "Media"]
    }
    st.table(tabla_variantes)

    st.info("Te recomendamos probar primero la receta base antes de experimentar con variantes, para familiarizarte con el manejo de tiempos y temperaturas.")

elif opcion_nombre == "Seguridad":

    st.session_state.progreso = 80

    st.title("🛡️ Seguridad e Higiene")

    st.write("""
Aunque el método melt & pour es uno de los más seguros para elaborar jabón en casa, es importante seguir algunas normas básicas de seguridad.
""")

    st.markdown("---")

    st.header("Medidas de seguridad")

    seguridad = [
        "Usa siempre un recipiente resistente al calor.",
        "Evita el contacto directo con el jabón recién fundido, ya que puede quemar.",
        "Si usas microondas, calienta en intervalos cortos para evitar sobrecalentamiento.",
        "Mantén el área de trabajo alejada del alcance de niños pequeños durante el proceso de fundido.",
        "Ventila el espacio si usas aceites esenciales en cantidad.",
        "No ingieras ninguno de los ingredientes ni el producto final."
    ]

    for item in seguridad:
        st.checkbox(item, disabled=True)

    st.header("Higiene en la elaboración")

    st.info("""
Lava y desinfecta todos los utensilios antes de comenzar.

Utiliza recipientes exclusivos para la elaboración de jabón, separados de los de cocina diaria.

Guarda el producto terminado en un lugar limpio y seco, idealmente envuelto en papel encerado o film transparente.
""")

    st.header("Preguntas frecuentes (FAQ)")

    with st.expander("¿El jabón melt & pour necesita usar guantes y gafas como el cold process?"):
        st.write("No es obligatorio, ya que no se manipula sosa cáustica directamente. Aun así, se recomienda precaución al manejar el jabón caliente.")

    with st.expander("¿Cuánto tiempo dura el jabón terminado?"):
        st.write("Correctamente almacenado, puede durar entre 6 y 12 meses sin perder sus propiedades.")

    with st.expander("¿Puedo usar miel de cualquier tipo?"):
        st.write("Sí, aunque se recomienda miel natural sin procesar para conservar mejor sus propiedades humectantes.")

    with st.expander("¿Qué hago si el jabón me queda demasiado duro?"):
        st.write("Puede deberse a que se enfrió demasiado rápido. Puedes volver a fundirlo a baño María agregando un poco más de agua.")

    with st.expander("¿Es apto para todo tipo de piel?"):
        st.write("En general sí, pero se recomienda hacer una prueba en una pequeña zona de la piel antes de un uso completo, especialmente si se usan aceites esenciales o colorantes.")

    st.header("Glosario")

    glosario = {
        "Término": ["Melt & Pour", "Saponificación", "Curado", "Glicerina", "Aceite esencial"],
        "Definición": [
            "Método de fundir una base de jabón ya elaborada y verterla en moldes con ingredientes adicionales.",
            "Reacción química que transforma grasas/aceites en jabón.",
            "Tiempo de reposo que permite que el jabón termine de endurecer y estabilizarse.",
            "Subproducto natural de la saponificación con propiedades humectantes.",
            "Extracto concentrado de plantas usado para aromatizar o aportar propiedades específicas."
        ]
    }
    st.table(glosario)

    st.session_state.progreso = 90

    st.title("📝 Evaluación Final")

    st.write("Responde las siguientes preguntas.")

    aciertos = 0

    p1 = st.radio(
        "1. ¿Cuál es la base utilizada para elaborar este jabón?",
        [
            "Detergente",
            "Jabón blanco neutro",
            "Shampoo"
        ]
    )

    if p1 == "Jabón blanco neutro":
        aciertos += 1

    p2 = st.radio(
        "2. ¿Qué ingrediente ayuda a hidratar la piel?",
        [
            "Sal",
            "Azúcar",
            "Miel"
        ]
    )

    if p2 == "Miel":
        aciertos += 1

    p3 = st.radio(
        "3. ¿Cuál es la función de la avena?",
        [
            "Dar color",
            "Exfoliar la piel",
            "Aumentar la espuma"
        ]
    )

    if p3 == "Exfoliar la piel":
        aciertos += 1

    p4 = st.radio(
        "4. ¿Cómo debe calentarse el jabón?",
        [
            "Directamente sobre el fuego",
            "A baño María o en microondas",
            "En el horno"
        ]
    )

    if p4 == "A baño María o en microondas":
        aciertos += 1

    p5 = st.radio(
        "5. ¿Cuál es el último paso del procedimiento?",
        [
            "Agregar avena",
            "Derretir el jabón",
            "Dejar enfriar y desmoldar"
        ]
    )

    if p5 == "Dejar enfriar y desmoldar":
        aciertos += 1

    p6 = st.radio(
        "6. ¿Cómo se llama el método de elaboración usado en este curso?",
        [
            "Cold Process",
            "Melt & Pour",
            "Hot Process"
        ]
    )

    if p6 == "Melt & Pour":
        aciertos += 1

    p7 = st.radio(
        "7. ¿Qué ingrediente se usa para crear la variante 'detox'?",
        [
            "Carbón activado",
            "Cacao en polvo",
            "Pétalos de rosa"
        ]
    )

    if p7 == "Carbón activado":
        aciertos += 1

    p8 = st.radio(
        "8. ¿Cuánto tiempo se recomienda dejar reposar el jabón para que endurezca?",
        [
            "5 minutos",
            "2 a 4 horas",
            "1 semana"
        ]
    )

    if p8 == "2 a 4 horas":
        aciertos += 1

    total_preguntas = 8

    if st.button("Calificar examen"):

        calificacion = round((aciertos / total_preguntas) * 100)

        st.metric("Calificación", f"{calificacion}/100", f"{aciertos}/{total_preguntas} correctas")

        if calificacion >= 80:
            st.success("¡Felicidades! Has aprobado el curso.")
        else:
            st.error("No aprobaste. Revisa el contenido y vuelve a intentarlo.")

elif opcion_nombre == "Finalizar":

    st.session_state.progreso = 100

    st.title("🎓 Curso Finalizado")

    st.balloons()

    st.success("Has llegado al final del curso.")

    st.markdown("---")

    st.header("Lo que aprendiste")

    st.write("""
✅ Identificar los materiales y herramientas necesarias.

✅ Elaborar un jabón artesanal con el método melt & pour.

✅ Aplicar correctamente el procedimiento paso a paso.

✅ Crear variantes personalizadas de la receta base.

✅ Aplicar medidas de seguridad e higiene.

✅ Desmoldar y presentar el producto terminado.
""")

    st.header("Próximos pasos")

    st.write("""
- Practica la receta base hasta dominar los tiempos de fundido.

- Experimenta con al menos una variante de las vistas en el módulo correspondiente.

- Si te interesa profundizar, investiga sobre el método de saponificación en frío (Cold Process).

- Considera documentar tu proceso con fotos para construir un pequeño portafolio, útil si decides emprender.
""")

    st.header("Recursos recomendados")

    st.info("""
Busca comunidades locales o en redes sociales dedicadas a la jabonería artesanal para resolver dudas y compartir resultados.

Investiga sobre regulaciones locales si planeas vender tus jabones, ya que pueden existir requisitos sanitarios específicos según tu país o región.
""")

    st.header("Constancia")

    nombre = st.text_input("Escribe tu nombre")

    if st.button("Generar constancia"):

        st.markdown(f"""
# CONSTANCIA

Se hace constar que

## {nombre}

ha concluido satisfactoriamente el curso

# Elaboración de Jabón Artesanal de Avena y Miel

Duración: 28 minutos

Modalidad: MOOC

¡Felicidades!
""")

    st.markdown("---")

    st.write("Gracias por participar en este curso.")