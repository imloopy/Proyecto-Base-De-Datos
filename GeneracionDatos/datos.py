import random
import datetime

comunas = [
    "Arica", "Camarones", "Putre", "General Lagos", "Iquique",
    "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara",
    "Pica", "Antofagasta", "Mejillones", "Sierra Gorda", "Taltal",
    "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena",
    "Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro",
    "Vallenar", "Alto del Carmen", "Freirina", "Huasco", "La Serena",
    "Coquimbo", "Andacollo", "La Higuera", "Paihuano", "Vicuña",
    "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle",
    "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado", "Valparaíso",
    "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero",
    "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada",
    "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca",
    "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz",
    "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco",
    "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay",
    "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache",
    "Olmué", "Villa Alemana", "Rancagua", "Codegua", "Coinco",
    "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí",
    "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua",
    "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu",
    "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones",
    "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua",
    "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz",
    "Talca", "Constitución", "Curepto", "Empedrado", "Maule",
    "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael",
    "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualaén",
    "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia",
    "Teno", "Vichuquén", "Linares", "Colbún", "Longaví",
    "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas",
    "Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui",
    "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano",
    "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete",
    "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles",
    "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento",
    "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara",
    "Tucapel", "Yumbel", "Alto Biobío", "Chillán", "Bulnes",
    "Cobquecura", "Coelemu", "Coihueco", "Chillán Viejo", "El Carmen",
    "Ninhue", "Ñiquén", "Pemuco", "Pinto", "Portezuelo",
    "Quillón", "Quirihue", "Ránquil", "San Carlos", "San Fabián",
    "San Ignacio", "San Nicolás", "Treguaco", "Yungay", "Temuco",
    "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino",
    "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial",
    "Padre Las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra",
    "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol",
    "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay",
    "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén",
    "Victoria", "Valdivia", "Corral", "Lanco", "Los Lagos",
    "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión",
    "Futrono", "Lago Ranco", "Río Bueno", "Puerto Montt", "Calbuco",
    "Cochamó", "Fresia", "Frutillar", "Los Muermos", "Llanquihue",
    "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi",
    "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón",
    "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque",
    "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo",
    "Chaitén", "Futaleufú", "Hualaihué", "Palena", "Coyhaique",
    "Lago Verde","Aysén", "Cisnes", "Guaitecas", "Cochrane", "Niebla",
    "Tortel", "Chile Chico", "Río Ibáñez", "Punta Arenas", "Laguna Blanca",
    "Río Verde", "San Gregorio", "Cabo de Hornos", "Antártica", "Porvenir",
    "Primavera", "Timaukel", "Natales", "Torres del Paine"
]

ruts = []
for _ in range(500):
    rut = f"{random.randint(1000000, 29999999)}-{random.randint(0, 9)}"
    while rut in ruts:
        rut = f"{random.randint(1000000, 29999999)}-{random.randint(0, 9)}"
    ruts.append(rut)

tipos_de_energia = ["solar", "eólica", "hidráulica", "geotérmica", "biomasa", "nuclear", "fósil"]

nombres_de_calle = [
    "Av. Principal", "Calle Falsa", "Av. Libertador", "Calle 123", 
    "Boulevard de los Sueños", "Calle de la Amistad", "Av. Siempre Viva", 
    "Callejón del Beso", "Av. Los Robles", "Calle de la Luna",
    "Calle del Sol", "Paseo de las Rosas", "Avenida del Mar", "Calle del Recuerdo",
    "Calle de los Pájaros", "Avenida de los Suspiros", "Calle de la Esperanza",
    "Calle del Bosque", "Avenida del Río", "Calle de las Flores",
    "Calle de los Recuerdos", "Avenida del Sol Naciente", "Calle de la Brisa",
    "Avenida de los Ángeles", "Calle de los Sueños", "Calle del Arcoíris",
    "Avenida de la Victoria", "Calle de la Ilusión", "Calle del Paraíso",
    "Avenida de la Felicidad", "Calle de la Fortuna", "Calle del Ocaso",
    "Avenida de la Paz", "Calle de la Aventura", "Calle del Destino",
    "Avenida de la Libertad", "Calle de la Fantasía", "Calle del Misterio",
    "Avenida de la Alegría", "Calle de la Pasión", "Calle del Tesoro",
    "Avenida de la Inspiración", "Calle de la Travesía", "Calle del Sueño",
    "Avenida de la Imaginación", "Calle de la Emoción", "Calle del Deseo"
]

numeros_de_calle = range(1, 1001)

nombres = [
    "Juan", "María", "Pedro", "Ana", "Luis", "Carolina", "Diego",
    "Valentina", "Andrés", "Camila", "José", "Sofía", "Miguel", "Laura",
    "Carlos", "Isabella", "Fernando", "Gabriela", "Pablo", "Valeria",
    "Alejandro", "Javier", "Daniel", "Verónica", "Ricardo", "Elena",
    "Roberto", "Patricia", "Héctor", "Natalia", "Gabriel", "Marcela",
    "Rafael", "Lucía", "Martín", "Catalina", "Eduardo", "Constanza",
    "Francisco", "Bárbara", "Antonio", "Jessica", "Mario", "Jennifer",
    "Gustavo", "Paula", "Sebastián", "Fabiola", "Arturo", "Francisca",
    "Alberto", "Carla", "Esteban", "Romina", "Ignacio", "Vanessa",
    "Hugo", "Elizabeth", "Mauricio", "Daniela", "Manuel", "Yanet",
    "Oscar", "Marisol", "César", "Karina", "Juan Pablo", "Gloria",
    "Federico", "Adriana", "Rogelio", "Carmen", "Victor", "Angélica",
    "Rodrigo", "Pamela", "Jorge", "Mayra", "Guillermo", "Silvia",
    "Enrique", "Rosa", "Alfredo", "Alejandra", "Leonardo", "Martha",
    "Erick", "Nancy", "Milton", "Karen", "Emilio", "Ana María"
]

apellidos = [
    "González", "Rodríguez", "Gómez", "Fernández", "López", "Díaz", "Martínez",
    "Pérez", "García", "Sánchez", "Romero", "Suárez", "Torres", "Rivera",
    "Ramírez", "Acosta", "Alvarez", "Benítez", "Cabrera", "Cruz",
    "Mendoza", "Castillo", "Vargas", "Rojas", "Reyes", "Jiménez", "Aguilar",
    "Hernández", "Muñoz", "Dominguez", "Guerrero", "Ortiz", "Silva", "Navarro",
    "Luna", "Juárez", "Valenzuela", "Gutiérrez", "Zamora", "Soto", "Sosa",
    "Medina", "Castro", "Chávez", "Ríos", "Fuentes", "Román", "Orozco",
    "Núñez", "Escobar", "Miranda", "Estrada", "Carrillo", "Álvarez", "Bautista",
    "Gallardo", "Paz", "Herrera", "Cortés", "Vega", "Guzmán", "Cáceres",
    "Aguirre", "Lara", "Morales", "Salazar", "Arias", "Aguirre", "Montoya",
    "Villalobos", "Olivares", "Campos", "Montes", "Leon", "Molina", "Baez",
    "Figueroa", "Rosales", "Padilla", "Serrano", "Navarro", "Correa", "Coronado",
    "Zúñiga", "Escobar", "Leyva", "Tovar", "Villanueva", "Abarca", "Zavala",
    "Medellín", "Bravo", "Pizarro", "Zapata", "Salinas", "Godoy", "Rentería",
    "Medrano", "Osorio", "Beltrán", "Salgado", "Villegas", "Belmonte", "Castañeda"
]

start_date = datetime.datetime(2014, 1, 1)
end_date = datetime.datetime(2024, 12, 31)
