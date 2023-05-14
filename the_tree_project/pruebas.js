// Obtener el botón HTML
const botonEnviar = document.getElementById('enviar');
console.log(botonEnviar)
// Función para cambiar los valores de la función polygon para un triángulo específico
function changePolygon(element, x1, y1, x2, y2, x3, y3, new_color, width, height) {
    const polygonValue = `${x1}px ${y1}px, ${x2}px ${y2}px, ${x3}px ${y3}px`;
    element.style.clipPath = `polygon(${polygonValue})`;
    element.style.width = `${width}px`
    element.style.height = `${height}px`
    element.style.background = new_color
}
  
// Función para realizar la llamada GET al recurso del backend
function obtenerDatos(generated_id) {
    
    fetch(`http://127.0.0.1:8000/square/${generated_id}/` , { method: 'GET' })
        .then(function(response) {
        return response.json();
        })
        .then(function(data) {
        // Manipula los datos obtenidos del backend según tus necesidades
        console.log(data.triangles[0].coordinates);
        
        // Obtén la referencia a cada triángulo por su clase o id
        const triangle1 = document.getElementById('triangle1');

        // Extrae los valores de las coordenadas de cada triángulo del resultado
        const triangle1Coordinates = data.triangles[0].coordinates;
        const new_color = data.color;

        // Ejemplo de cambio de valores para cada triángulo
        changePolygon(triangle1, triangle1Coordinates[0].x, triangle1Coordinates[0].y, triangle1Coordinates[1].x, triangle1Coordinates[1].y, triangle1Coordinates[2].x, triangle1Coordinates[2].y, new_color);
        })
        .catch(function(error) {
        console.log('Error:', error);
        });
}

// Función para enviar datos al backend al presionar el boton 'Generate'.
function enviarDatos() {
    const color = document.getElementById('color').value;
    const height = document.getElementById('height').value;
    const width = document.getElementById('width').value;
    const triangle_height = 100 * height;
    const triangle_width = 100 * width;

    // Generar numero aleatorio.
    const min = 100;
    const max = 10000000;
    const randomNum = Math.floor(Math.random() * (max - min + 1) + min);

    const data = {
        id_custom: randomNum,
        triangles: [
            {
                coordinates: [
                    {
                        x: 0,
                        y: 0
                    },
                    {
                        x: 0,
                        y: triangle_height
                    },
                    {
                        x: triangle_width,
                        y: triangle_height
                    }
                ]
            },
            {
                coordinates: [
                    {
                        x: 0,
                        y: 0
                    },
                    {
                        x: triangle_width,
                        y: 0
                    },
                    {
                        x: triangle_width,
                        y: triangle_height
                    }
                ]
            }
        ],
        color: color,
        size: 200
    };

    fetch('http://127.0.0.1:8000/square/', { 
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'X-Requested-With': 'XMLHttpRequest'},
            body: JSON.stringify(data)
        }
        )
    console.log(data['triangles'][0]['coordinates'])
    changePolygon(
        triangle1, 
        data['triangles'][0]['coordinates'][0]['x'], 
        data['triangles'][0]['coordinates'][0]['y'], 
        data['triangles'][0]['coordinates'][1]['x'], 
        data['triangles'][0]['coordinates'][1]['y'], 
        data['triangles'][0]['coordinates'][2]['x'], 
        data['triangles'][0]['coordinates'][2]['y'], 
        color,
        triangle_width,
        triangle_height);

    changePolygon(
        triangle2, 
        data['triangles'][1]['coordinates'][0]['x'], 
        data['triangles'][1]['coordinates'][0]['y'], 
        data['triangles'][1]['coordinates'][1]['x'], 
        data['triangles'][1]['coordinates'][1]['y'], 
        data['triangles'][1]['coordinates'][2]['x'], 
        data['triangles'][1]['coordinates'][2]['y'], 
        color,
        triangle_width,
        triangle_height);
}

// Asociar la función con el evento 'click' del botón
botonEnviar.addEventListener('click', enviarDatos);