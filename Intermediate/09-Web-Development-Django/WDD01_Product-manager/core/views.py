from django.shortcuts import render

def index(request):
    products = [
        {
            'id': 1,
            'name': "Poke Ball",
            'description': "Herramienta básica para capturar Pokémon. Estándar, eficiente y clásica.",
            'price': 9.99,
            'image': 'img/Poke_Ball.png',
        },
        {
            'id': 2,
            'name': "Super Ball",
            'description': "Mayor tasa de captura que la versión estándar.",
            'price': 9.99,
            'image': 'img/Super_Ball.png',
        },
        {
            'id': 3,
            'name': "Ultra Ball",
            'description': "Alta efectividad para Pokémon difíciles.",
            'price': 9.99,
            'image': 'img/Ultra_Ball.png',
        },
        {
            'id': 4,
            'name': "Master Ball",
            'description': "Captura garantizada. Nivel leyenda.",
            'price': 9.99,
            'image': 'img/Master_Ball.png',
        }
    ]
    return render(request, "index.html", {'products':products})

def details(request):
    return render(request, "details.html")