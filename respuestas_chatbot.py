from datetime import datetime
import random

# Obtiene la respuesta basada en la intención detectada
def ObtenerRespuesta(ListaIntentos, JsonIntentos):

    def generar_respuesta_area(nombre_area, emoji, piso, encargado, extensiones):

        pisos = {
            "0": "Planta Baja",
            "1": "Piso 1",
            "2": "Piso 2",
            "3": "Piso 3",
            "4": "Piso 4",
            "5": "Piso 5",
            "6": "Piso 6",
            "7": "Edificio Viejo",	
        }

        piso = pisos.get(piso, piso)
        
        card = (
            f'<section class="card">'
                f'<header>'
                    f'<p><b>{nombre_area} <span class="info emoji">{emoji}</span></b> <b><button class="info pisos" onclick="Mostrar(\'{piso}\')">{piso}</button></b> </p>'
                    f'<p>{encargado}</p>'
                f'</header>'
            f'</section>'
        )
        
        botones_ext = ""
        for descripcion, ext in extensiones:
            botones_ext += f'<b> </b><a href="tel:6677126606,{ext}"><button class="archivo"><b>{descripcion}: </b>{ext}</button></a>'
        
        return [card, Respuesta, TelefonoPrincipal + botones_ext]

    if not ListaIntentos or ListaIntentos[0]['Intencion'] == 'unknown':
        return ["Lo siento, no tengo información sobre ese tema. ¿Puedes preguntar algo más relacionado con el hospital?"]
    
    Ayuda = "¿En qué más te puedo ayudar?"
    InfoContacto = 'Si necesitas más información, no dudes en comunicarte a nuestros canales oficiales.\n<b>Correo: </b> <a href="mailto:alianzaestrategica@hps.org.mx"><button class="info">alianzaestrategica@hps.org.mx ✉️</button></a>\n<b>Teléfono Principal y Extensiones:\n</b> <a href="tel:6677126606"><button class="info">6677126606 📞</button></a><b> </b><a href="EXTENCIONES.pdf" target="_blank"><button class="archivo">Todas las Extensiones ➡️</button></a>'
    TelefonoPrincipal = '<b>Teléfono Principal y Extensión</b> \n<a href="tel:6677126606"><button class="info">6677126606 📞</button></a>'

    Etiqueta = ListaIntentos[0]['Intencion']    
    
    for Intento in JsonIntentos['intents']:
        if Intento['tag'] == Etiqueta:
            # Se elige una respuesta aleatoria
            Respuesta = random.choice(Intento['respuestas'])

            # Comparar directamente con el tag en lugar de la respuesta
            if Intento['tag'] == "fecha":
                FechaActual = datetime.now().strftime("%A, %d de %B del %Y")
                return [f"Hoy es {FechaActual}", Ayuda]
            elif Intento['tag'] == "hora":
                HoraActual = datetime.now().strftime("%H:%M")
                return [f"Son las {HoraActual}", Ayuda]
            elif Intento['tag'] == "logo":
                return [
                    Respuesta,
                    '<a href="https://hospitalpediatrico.org/oficial/" target="_blank"><img class="elemento_interno" decoding="async" width="100" src="https://hospitalpediatrico.org/oficial/wp-content/uploads/2022/08/icon-logo-hps.png" alt="Hospital Pediátrico de Sinaloa"></a>'
                ] 
            elif Intento['tag'] == "informacion_general":
                return [
                    Respuesta,
                    InfoContacto
                ]
            elif Intento['tag'] == "ubicacion":
                return [
                    Respuesta,
                    '<iframe class="elemento_interno" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3621.9029951692764!2d-107.40199942463111!3d24.79877497796962!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86bcd0b34e811d65%3A0x7728b9f1122455ed!2sHospital%20Pedi%C3%A1trico%20de%20Sinaloa!5e0!3m2!1ses!2smx!4v1743604900818!5m2!1ses!2smx" width="300" height="200" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
                    Ayuda
                ]
            elif Intento['tag'] == "especialidades":
                return [
                    Respuesta,
                    'Selecciona una especialidad para saber más información'
                    '\n<button class="info" onclick="Mostrar(\'Alergologia\')">Alergologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Cardiologia\')">Cardiologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Cirugia cardiovascular\')">Cirugia cardiovascular</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Cirugia general\')">Cirugia general</button><b> </b>'
                    
                    '<button class="info" onclick="Mostrar(\'Cirugia plastica\')">Cirugia plastica</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Clinica de obesidad\')">Clinica de obesidad</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Comunicacion humana\')">Comunicacion humana</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Cons. de urgencias\')">Cons. de urgencias</button><b> </b>'

                    '<button class="info" onclick="Mostrar(\'Consulta externa\')">Consulta externa</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Dermatologia\')">Dermatologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Endocrinologia\')">Endocrinologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Estomatologia\')">Estomatologia</button><b> </b>'

                    '<button class="info" onclick="Mostrar(\'Foniatria y audiologia\')">Foniatria y audiologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Gastroenterologia\')">Gastroenterologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Genetica\')">Genetica</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Hematologia\')">Hematologia</button><b> </b>'

                    '<button class="info" onclick="Mostrar(\'Infectologia\')">Infectologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Medicina fisica y rehabilitacion\')">Medicina fisica y rehabilitacion</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Medicina interna\')">Medicina interna</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Nefrologia\')">Nefrologia</button><b> </b>'

                    '<button class="info" onclick="Mostrar(\'Neonatologia\')">Neonatologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Neumologia\')">Neumologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Neurologia\')">Neurologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Neurocirugia\')">Neurocirugia</button><b> </b>'

                    '<button class="info" onclick="Mostrar(\'Nutricion\')">Nutricion</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Oftalmologia\')">Oftalmologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Oncologia\')">Oncologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Ortodoncia\')">Ortodoncia</button><b> </b>'

                    '<button class="info" onclick="Mostrar(\'Otorrinolaringologia\')">Otorrinolaringologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Psicologia\')">Psicologia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Traumatologia y ortopedia\')">Traumatologia y ortopedia</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Urologia\')">Urologia</button>',
                    InfoContacto
                ]
            elif Intento['tag'] == "pagina_web":
                return [
                    Respuesta,
                    '<button class="info" onclick="window.open(\'https://hospitalpediatrico.org/oficial/\', \'_blank\');">Pagina Web Oficial ➡️➡️🌐</button>'
                ]
            elif Intento['tag'] == "info_chatbot":
                return [
                    Respuesta,
                    "Estoy aquí para responder tus preguntas relacionadas con el hospital."
                ]
            elif Intento['tag'] == "telefono":
                return [
                    '<b>Teléfono Principal y Extensiones:</b>'
                    '\n<a href="tel:6677126606"><button class="info">667 712 66 06 📞</button></a>'
                    '<b> </b><a href="EXTENCIONES.pdf" target="_blank"><button class="archivo" style="margin-bottom: 5px;">Todas las Extensiones ➡️</button></a>'+
                    Respuesta,
                    'También puedes preguntar por el área que deseas contactar y te proporcionaremos la <b>extensión específica.</b>',
                    '<b>Otros Teléfonos:</b>'
                    '\n<a href="tel:6677139004"><button class="info">667 713 90 04 📞</button></a>'
                    '<b> </b><a href="tel:6677126607"><button class="info">667 712 66 07 📞</button></a>'
                    '\n<a href="tel:6677126608"><button class="info">667 712 66 08 📞</button></a>'
                    '<b> </b><a href="tel:6677133523"><button class="info">667 713 35 23 📞</button></a>'
                    '\n<a href="tel:6672612200"><button class="info">667 261 22 00 📞</button></a>'
                ]
            elif Intento['tag'] == "correo":
                return [
                    Respuesta + '\n<a href="mailto:alianzaestrategica@hps.org.mx"><button class="info">alianzaestrategica@hps.org.mx ✉️</button></a>'
                ]
            elif Intento['tag'] == "donaciones":
                return [
                    Respuesta,
                    InfoContacto
                ]
            elif Intento['tag'] == "redes_sociales":
                return [
                    Respuesta,
                    '<b>Redes Sociales Oficiales:</b>'
                    '\n<button class="info" style="background-color:#1877f2;" onclick="window.open(\'https://www.facebook.com/profile.php?id=100083151401330\', \'_blank\');"><i class="fab fa-facebook"></i> Facebook</button> '
                    '<b> </b><button class="info" style="background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);" onclick="window.open(\'https://www.instagram.com/hospitalpediatricodesinaloa?igsh=MTVvZmkxZ25obTMybw%3D%3D\', \'_blank\');"><i class="fab fa-instagram"></i> Instagram</button> '
                    '<b> </b><button class="info" style="background-color: black" onclick="window.open(\'https://x.com/pediatrico\', \'_blank\');"><i class="fab fa-twitter"></i> Twitter</button>'
                ]
            elif Intento['tag'] == "extensiones":
                return [
                    Respuesta +
                    '\n<a href="EXTENCIONES.pdf" target="_blank"><button class="archivo">Todas las Extensiones ➡️</button></a>',
                    'También puedes preguntar por el área que deseas contactar y te proporcionaremos la <b>extensión específica.</b>',
                    '<b>Teléfono Principal:</b>'
                    '\n<a href="tel:6677126606"><button class="info">667 712 66 06 📞</button></a>',
                    '<img class="elemento_interno" src="Img/P1.png" alt="Ext. P1">'
                ]
            elif Intento['tag'] == "mision_vision":   
                return [
                    '<img decoding="async" width="200" class="elemento_interno" src="Img/F4.jpg" alt="">',
                    Respuesta,
                    '<b>Vision:</b> Ser un hospital líder a nivel nacional en atención pediátrica, formación médica e investigación, con personal suficiente y capacitado.'                
                ]
            elif Intento['tag'] == "farmacia":
                return generar_respuesta_area(nombre_area="Farmacia ", emoji="💊", piso="0", encargado="María Conchita Calderón Romero",
                    extensiones=[("Farmacia", "7041"), ("Farmacia Oficina", "7042")]
                )
            elif Intento['tag'] == "alianza_estrategica":
                return generar_respuesta_area(nombre_area="Alianza Estratégica ", emoji="🙏", piso="6", encargado="María Conchita Calderón Romero",
                    extensiones=[("Alianza Estratégica", "7004")]
                )
            elif Intento['tag'] == "almacen_general":
                return generar_respuesta_area(nombre_area="Almacén General y Activos fijos ", emoji="💉", piso="0", encargado="C. Olga Lucero Pimental Labrada",
                    extensiones=[("Almacén General", "7005")]
                )
            elif Intento['tag'] == "sub_almacen":
                return generar_respuesta_area(nombre_area="Sub Almacén ", emoji="💉", piso="5", encargado="[Nombre del Encargado]",
                    extensiones=[("Sub Almacén", "7006")]
                )
            elif Intento['tag'] == "apoyo_nutricional":
                return generar_respuesta_area(nombre_area="Apoyo Nutricional ", emoji="🍎", piso="2", encargado="[Nombre del Encargado]",
                    extensiones=[("Apoyo Nutricional", "7007")]
                )
            elif Intento['tag'] == "archivo_clinico":
                return generar_respuesta_area(nombre_area="Archivo Clínico ", emoji="📂", piso="2", encargado="Lic. Dalia Ramírez Morales",
                    extensiones=[("Archivo Clínico", "7008")]
                )
            elif Intento['tag'] == "aula_capacitacion":
                return generar_respuesta_area(nombre_area="Aula de Capacitación ", emoji="🧑‍🏫", piso="6", encargado="Maricruz",
                    extensiones=[("Aula de Capacitación", "7010")]
                )
            elif Intento['tag'] == "biomedica_ingenieria":
                return generar_respuesta_area(nombre_area="Biomédica Ingeniería ", emoji="🔩", piso="1", encargado="Ing. Sinhue Everardo Acosta Osuna",
                    extensiones=[("Biomédica Ingeniería", "7011")]
                )
            elif Intento['tag'] == "calidad":
                return generar_respuesta_area(nombre_area="Calidad Hospitalaria ", emoji="🏥", piso="6", encargado="Enf. Fabiola Sánchez Mapula",
                    extensiones=[("Calidad Hospitalaria", "7012")]
                )
            elif Intento['tag'] == "cardiologia":
                return generar_respuesta_area(nombre_area="Cardiología ", emoji="🫀", piso="2", encargado="Dr. José Antonio Quibrera Matienzo",
                    extensiones=[("Cardiología", "7013")]
                )
            elif Intento['tag'] == "central_de_cuentas":
                return generar_respuesta_area(nombre_area="Central de Cuentas ", emoji="📋", piso="#", encargado="[Nombre del Encargado]",
                    extensiones=[("Central de Cuentas", "7014")]
                )
            elif Intento['tag'] == "centro_mezclas":
                return generar_respuesta_area(nombre_area="Centro de Mezclas ", emoji="💉", piso="#", encargado="[Nombre del Encargado]",
                    extensiones=[("Centro de Mezclas", "7015")]
                )
            elif Intento['tag'] == "ceye":
                return generar_respuesta_area(nombre_area="CEYE ", emoji="🥼", piso="5", encargado="Enf. Rosa Esthela Robles Uriarte",
                    extensiones=[("CEYE", "7016")]
                )
            elif Intento['tag'] == "cirugia":
                return generar_respuesta_area(nombre_area="Cirugía ", emoji="🩺", piso="#", encargado="Dr. Juan Manuel Zazueta Tirado",
                    extensiones=[("Cirugía", "7017"), ("Cirugía Oficina", "7018")]
                )
            elif Intento['tag'] == "clinica_heridas":
                return generar_respuesta_area(nombre_area="Clínica de Heridas ", emoji="🤕", piso="#", encargado="Enf. María Consuelo Chacón Zapién",
                    extensiones=[("Clínica de Heridas", "7019")]
                )
            elif Intento['tag'] == "cobranza":
                return generar_respuesta_area(nombre_area="Cobranza ", emoji="💸", piso="#", encargado="[Nombre del Encargado]",
                    extensiones=[("Cobranza", "7020")]
                )
            elif Intento['tag'] == "cocina":
                return generar_respuesta_area(nombre_area="Cocina ", emoji="🍽️", piso="2", encargado="[Nombre del Encargado]",
                    extensiones=[("Cocina", "7021")]
                )
            elif Intento['tag'] == "consulta_externa":
                return generar_respuesta_area(nombre_area="Consulta Externa ", emoji="🧑‍⚕️", piso="2", encargado="Dra. Aleida López Barajas",
                    extensiones=[("Consulta Externa Recepción", "7023"), ("Consulta Externa Jefe Pediátrico", "7120")]
                )
            elif Intento['tag'] == "contabilidad_oficina":
                return generar_respuesta_area(nombre_area="Contabilidad ", emoji="💰", piso="6", encargado="[Nombre del Encargado]",
                    extensiones=[("Contabilidad", "7024")]
                )
            elif Intento['tag'] == "dental":
                return generar_respuesta_area(nombre_area="Estomatología y Ortodoncia ", emoji="🦷", piso="2", encargado="Dra. Raquel Salazar Márquez",
                    extensiones=[("Estomatología y Ortodoncia", "7026")]
                )
            elif Intento['tag'] == "enfermeria_ensenanza":
                return generar_respuesta_area(nombre_area="Enfermería Enseñanza ", emoji="✏️", piso="6", encargado="Enf. Alba Berenice Madueño Madrigal ",
                    extensiones=[("Enfermería Enseñanza", "7029")]
                )
            elif Intento['tag'] == "enfermeria_jefatura":
                return generar_respuesta_area(nombre_area="Enfermería Jefatura ", emoji="👩‍⚕️", piso="6", encargado="[Nombre del Encargado]",
                    extensiones=[("Enfermería Jefatura", "7030"), ("Enfermería Jefatura Secretaria", "7031")]
                )
            elif Intento['tag'] == "enfermeria_subjefatura":
                return generar_respuesta_area(nombre_area="Enfermería Subjefatura ", emoji="👩‍⚕️", piso="6", encargado="[Nombre del Encargado]",
                    extensiones=[("Enfermería Subjefatura", "7032")]
                )
            elif Intento['tag'] == "ensenanza_dos":
                return generar_respuesta_area(nombre_area="Enseñanza Dos ", emoji="📚", piso="6", encargado="[Nombre del Encargado]",
                    extensiones=[("Enseñanza e Investigación", "7033")]
                )
            elif Intento['tag'] == "ensenanza_investigacion_medica":
                return generar_respuesta_area(nombre_area="Enseñanza e Investigación Medica ", emoji="📖", piso="4", encargado="Dr. Alberto Paez Salazar ",
                    extensiones=[("Enseñanza Investigación", "7034"), ("Enseñanza Medica Jefe", "7035"), 
                                    ("Enseñanza Medica Secretaria", "7036"), ("Enseñanza Medicina Basado en Evidencias", "7037"),]
                )
            elif Intento['tag'] == "especialidades_area":
                return generar_respuesta_area(nombre_area="Especialidades ", emoji="🔍", piso="#", encargado="[Nombre del Encargado]",
                    extensiones=[("Especialidades", "7038")]
                )
            elif Intento['tag'] == "espesialidades_enfermeria":
                return generar_respuesta_area(nombre_area="Especialidades Enfermeria ", emoji="👩‍⚕️", piso="#", encargado="[Nombre del Encargado]",
                    extensiones=[("Especialidades Enfermeria", "7039")]
                )
            elif Intento['tag'] == "epidemiologia":
                return generar_respuesta_area(nombre_area="Epidemiologia ", emoji="🦠", piso="2", encargado="Ep. Rosalino Flores Rocha",
                    extensiones=[("Epidemiologia", "7040")]
                )
            elif Intento['tag'] == "gastroenterologia":
                return generar_respuesta_area(nombre_area="Gastroenterología ", emoji="🥼", piso="2", encargado="Dra. Vianey Paola Zamudio Vázquez",
                    extensiones=[("Gastroenterología", "7044")]
                )
            elif Intento['tag'] == "gastroenterologia_oficina":
                return generar_respuesta_area(nombre_area="Gastroenterología Oficina ", emoji="🗄️", piso="2", encargado="Dra. Vianey Paola Zamudio Vázquez",
                    extensiones=[("Gastroenterología Oficina", "7044")]
                )
            elif Intento['tag'] == "quirofano_endoscopia":
                return generar_respuesta_area(nombre_area="Quirófano de endoscopia ", emoji="🩺", piso="3", encargado="Enf. Ángelica Vega Millán",
                    extensiones=[("Quirófano de endoscopia", "7043")]
                )
            elif Intento['tag'] == "genetica":
                return generar_respuesta_area(nombre_area="Genetica ", emoji="🧬", piso="1", encargado="Dr. Jesús Ernesto Dueñas Arias",
                    extensiones=[("Genetica", "7045")]
                )
            elif Intento['tag'] == "infectologia":
                return generar_respuesta_area(nombre_area="Infectología ", emoji="🦠", piso="5", encargado="Dr. Carlos Alberto Velázquez Ríos<br>Enf. Nancy Rebeca Díaz Beltrán ",
                    extensiones=[("Infectología Oficina", "7046"), ("Infectología Sala", "7047")]
                )
            elif Intento['tag'] == "informatica":
                return generar_respuesta_area(nombre_area="Informática ", emoji="💻", piso="6", encargado="Lic. Jorge Antonio Cruz Sainz",
                    extensiones=[("Informática", "7048")]
                )
            elif Intento['tag'] == "informes_recepcion":
                return generar_respuesta_area(nombre_area="Informes Recepción ", emoji="☎️", piso="0", encargado="",
                    extensiones=[("Informes Recepción", "7049")]
                )
            elif Intento['tag'] == "inhaloterapia":
                return generar_respuesta_area(nombre_area="Inhaloterapia ", emoji="👃", piso="0", encargado="Enf. Ana Guadalupe Cruz Castillo ",
                    extensiones=[("Inhaloterapia", "7050")]
                )
            elif Intento['tag'] == "terapia_respiratoria":
                return generar_respuesta_area(nombre_area="Terapia Respiratoria (Inhaloterapia) ", emoji="👃", piso="0", encargado="Dra. Ana María López Reyes",
                    extensiones=[("Inhaloterapia", "7050")]
                )
            elif Intento['tag'] == "juridico":
                return generar_respuesta_area(nombre_area="Juridico ", emoji="🏛️", piso="6", encargado="Elizabeth Gomez Olivarez",
                    extensiones=[("Juridico", "7051")]
                )
            elif Intento['tag'] == "laboratorio":
                return generar_respuesta_area(nombre_area="Laboratorio ", emoji="🔬", piso="1", encargado="QFB. Maria Leticia Félix Miranda",
                    extensiones=[("Laboratorio Recepción C.E.", "7052"), ("Laboratorio Filtro HOSP", "7030"), ("Laboratorio Jefe", "7031")]
                )
            elif Intento['tag'] == "mantenimiento":
                return generar_respuesta_area(nombre_area="Mantenimiento ", emoji="🛠️", piso="1", encargado="MII. Samuel Oswaldo Loya Acosta",
                    extensiones=[("Mantenimiento Oficina", "7053"), ("Mantenimiento", "7054")]
                )
            elif Intento['tag'] == "medicina_interna":
                return generar_respuesta_area(nombre_area="Medicina Interna ", emoji="⚕️", piso="5", encargado="Enf. María del Rosario Chamorro Chairez",
                    extensiones=[("Medicina Interna", "7055")]
                )
            elif Intento['tag'] == "medicina_legal":
                return generar_respuesta_area(nombre_area="Medicina Legal ", emoji="⚖️", piso="6", encargado="Dra. Ana Luisa Castro Medina",
                    extensiones=[("Medicina Legal", "7056")]
                )
            elif Intento['tag'] == "medicina_preventiva":
                return generar_respuesta_area(nombre_area="Medicina Preventiva ", emoji="🩺", piso="#", encargado="Enf. Silvia Viridiana Angulo Leyva",
                    extensiones=[("Medicina Preventiva", "7057")]
                )
            elif Intento['tag'] == "medicina_transfusional":
                return generar_respuesta_area(nombre_area="Medicina Transfusional ", emoji="🩸", piso="#", encargado="Enf. Favela Bernal Jessica Lizbeth",
                    extensiones=[("Medicina Transfusional", "7058")]
                )
            elif Intento['tag'] == "modulo_informacion":
                return generar_respuesta_area(nombre_area="Modulo de Información ", emoji="📒", piso="0", encargado="",
                    extensiones=[("Modulo de Información", "7059")]
                )
            elif Intento['tag'] == "neonatologia":
                return generar_respuesta_area(nombre_area="Neonatología ", emoji="👶", piso="5", encargado="Dra. Aleyda Zazueta Chávez<br>Enf. Sandra Elena Benítez López",
                    extensiones=[("Neonatología Infecto", "7060"), ("Neonatología Oficina", "7061"), ("Neonatología Sala", "7062")]
                )
            elif Intento['tag'] == "oncologia_edificio_viejo":
                return generar_respuesta_area(nombre_area="Oncología ", emoji="🏥", piso="7", encargado="Dra. Obdilia Gutiérrez Guzmán",
                    extensiones=[("Oncología Angelita", "7064"), ("Oncología Banco de Sangre", "7065"), ("Oncología Catéteres", "7066"),
                                    ("Oncología Jefatura", "7067"), ("Oncología Jefe", "7068"), ("Oncología Oficina Hematología", "7070"),
                                    ("Oncología Oficina Secretaría", "7071"), ("Oncología Quimioterapia Ambulatoria", "7072"), ("Oncología Recepción Consulta", "7073"),
                                    ("Oncología Residentes", "7074"), ("Oncología TS Hospitalización", "7076"), ("Oncología Somatometría", "7118"),
                                    ("Oncología Tumores", "7119"), ("Oncología Sala", "7122"), ("Nutrición Onco Pediátrico", "7125")
                    ]
                )
            elif Intento['tag'] == "anatomia_patologica":
                return generar_respuesta_area(nombre_area="Patológia ", emoji="🧬", piso="3", encargado="Pat. Eri Peña Martínez",
                    extensiones=[("Patológia", "7077")]
                )
            elif Intento['tag'] == "quirofano_1_2":
                return generar_respuesta_area(nombre_area="Quirófano ", emoji="🔪", piso="#", encargado="Dr. Jesús Oscar Soto Quintero",
                    extensiones=[("Quirófano 1 y 2", "7078")]
                )
            elif Intento['tag'] == "rayos_x":
                return generar_respuesta_area(nombre_area="Rayos X ", emoji="💀", piso="1", encargado="Dr. José Manuel López López",
                    extensiones=[("Rayos X Placas", "7080"), ("Rayos X Oficina Mayte", "7081"), ("Recepción Rayos X", "7115"),
                                    ("Ultrasonido Rayos X", "7116"), ("Rayos X TAC", "7117")]
                )
            elif Intento['tag'] == "recursos_financieros":
                return generar_respuesta_area(nombre_area="Recursos Financieros ", emoji="💵", piso="6", encargado="Lic. Marlenne Karime Osuna Bolado",
                    extensiones=[("Recursos Financieros", "7082")]
                )
            elif Intento['tag'] == "recursos_humanos":
                return generar_respuesta_area(nombre_area="Recursos Humanos ", emoji="👨‍⚕️", piso="6", encargado="Lic. Hermelinda Avendaño Gutiérrez",
                    extensiones=[("Recursos Humanos", "7083"), ("Recursos Humanos Jefe", "7084"), ("Recursos Humanos Contrato", "7103")]
                )
            elif Intento['tag'] == "seguro_popular":
                return generar_respuesta_area(nombre_area="Seguro Popular ", emoji="🧑‍⚕️", piso="#", encargado="Lic. María de los Ángeles López López",
                    extensiones=[("Seguro Popular Medico", "7085"), ("Seguro Popular Oficina", "7086")]
                )
            elif Intento['tag'] == "servicios_generales":
                return generar_respuesta_area(nombre_area="Servicios Generales ", emoji="🧹", piso="0", encargado="Ing. Jose Luis Ochoa Arellano",
                    extensiones=[("Servicios Generales", "7087")]
                )
            elif Intento['tag'] == "subdireccion_planeacion":
                return generar_respuesta_area(nombre_area="Subdirección de Planeación ", emoji="📋", piso="#", encargado="M. Iván Rafael Mendoza Zuñiga",
                    extensiones=[("Subdirección de Planeación", "7088")]
                )
            elif Intento['tag'] == "subdireccion_servicios_auxiliares":
                return generar_respuesta_area(nombre_area="Subdirección Servicios Auxiliares ", emoji="🖼️", piso="#", encargado=" Dra. Cynthia Gabriela  Torres Galicia",
                    extensiones=[("Subdirección Servicios Auxiliares", "7089")]
                )
            elif Intento['tag'] == "subdireccion_medica":
                return generar_respuesta_area(nombre_area="Subdirección Medica ", emoji="🥼", piso="6", encargado="Dr. Fernando de Jesús  Bodart Román<br>Dra. Laura Elena Salazar Castro",
                    extensiones=[("Subdirección Medica", "7090")]
                )
            elif Intento['tag'] == "subdireccion_secretaria":
                return generar_respuesta_area(nombre_area="Subdirección Secretaria ", emoji="✒️", piso="6", encargado="",
                    extensiones=[("Subdirección Secretaria", "7091")]
                )
            elif Intento['tag'] == "terapia_intensiva":
                return generar_respuesta_area(nombre_area="Terapia Intensiva ", emoji="❤️‍🩹", piso="4", encargado="Dra. Vianey Melchor García<br>Enf. Soledad Ibarra Yáñez ",
                    extensiones=[("Terapia Intensiva Oficina", "7092"), ("Terapia Intensiva Sala", "7093")]
                )
            elif Intento['tag'] == "trabajo_social":
                return [
                    Respuesta,
                    '<b>Diferentes áreas de trabajo social</b>'
                    '\n<button class="info" onclick="Mostrar(\'Trabajo Social Infectología\')">Infectología</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Neonatología\')">Neonatología</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Oficina\')">Oficina</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Qx Ambulatorio\')">QX Ambulatorio</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Terapia Intensiva\')">Terapia Intensiva</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Urgencias\')">Urgencias</button><b> </b>'
                    '<button class="info" onclick="Mostrar(\'Trabajo Social Jefatura\')">Jefatura</button>',
                    'Selecciona un área para saber más información'
                ]
            elif Intento['tag'] == "trabajo_social_infectologia":
                return generar_respuesta_area(nombre_area="Trabajo Social Infectología ", emoji="🦠", piso="5", encargado="Lic. Maria de la Cruz Olguín Mendoza",
                    extensiones=[("Trabajo Social Infectología", "7094")]
                )
            elif Intento['tag'] == "trabajo_social_neonatologia":
                return generar_respuesta_area(nombre_area="Trabajo Social Neonatología ", emoji="👶", piso="5", encargado="Lic. Maria de la Cruz Olguín Mendoza ",
                    extensiones=[("Trabajo Social Neonatología", "7095")]
                )
            elif Intento['tag'] == "trabajo_social_oficina":
                return generar_respuesta_area(nombre_area="Trabajo Social Oficina ", emoji="🏢", piso="0", encargado="Lic. Maria de la Cruz Olguín Mendoza ",
                    extensiones=[("Trabajo Social Oficina", "7096")]
                )
            elif Intento['tag'] == "trabajo_social_qx_ambulatorio":
                return generar_respuesta_area(nombre_area="Trabajo Social QX Ambulatorio ", emoji="🚑", piso="3", encargado="Lic. Maria de la Cruz Olguín Mendoza",
                    extensiones=[("Trabajo Social QX Ambulatorio", "7097")]
                )
            elif Intento['tag'] == "trabajo_social_terapia_intensiva":
                return generar_respuesta_area(nombre_area="Trabajo Social Terapia Intensiva ", emoji="💪", piso="4", encargado="Lic. Maria de la Cruz Olguín Mendoza",
                    extensiones=[("Trabajo Social Terapia Intensiva", "7098")]
                )
            elif Intento['tag'] == "trabajo_social_urgencias":
                return generar_respuesta_area(nombre_area="Trabajo Social Urgencias ", emoji="⏰", piso="0", encargado="Lic. Maria de la Cruz Olguín Mendoza",
                    extensiones=[("Trabajo Social Urgencias", "7099")]
                )
            elif Intento['tag'] == "trabajo_social_jefatura":
                return generar_respuesta_area(nombre_area="Trabajo Social Jefatura ", emoji="👩‍⚕️", piso="0", encargado="Lic. Maria de la Cruz Olguín Mendoza",
                    extensiones=[("Trabajo Social Jefatura", "7114")]
                )
            return [Respuesta]
    return ["Lo siento, no entendí tu pregunta."]