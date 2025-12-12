"""
Este archivo convierte el proyecto de Python en un paquete instalable,
distribuible y reusable. Sin él, el código seguiría siendo solo una carpeta 
con módlos; con él, se convierte en un paquete profesional reconocido por 
Python y por la comunidad.
"""

# Antes de iniciar se tiene que haber instalado "pip install setuptools" en el entorno virtual

from setuptools import setup, find_packages

setup(
    name = 'sales_application_lamk-s',
    version = '0.1.0',
    author = 'Melvin López',
    author_email = 'kunlancelot@gmail.com',
    description = 'Paquete para gestionar ventas, precios, impuestos y descuentos',
    long_description = open('README.md', encoding = 'utf-8').read(),
    long_description_content_type= 'text/markdown',
    url = 'https://github.com/Lamk-S/Python/tree/main/Intermediate/05-Modules-Packages/MP07_Sales_Application',
    packages = find_packages(),
    install_requires = [],
    classifiers = [
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires = '>=3.7'
)