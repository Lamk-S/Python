"""
==================================================
        EJERCICIO PRÁCTICO: CHATBOT SIMPLE
==================================================

Este ejercicio aplica conceptos de:
- Programación Orientada a Objetos
- Encapsulación de comportamiento
- Uso de diccionarios
- Lógica básica de procesamiento de texto
"""

import random

# ==================================================
#               CLASE CHATBOT
# ==================================================

class AdvancedChatBot:
    """
    Chatbot simple basado en palabras clave.
    """
    
    def __init__(self):
        self.runnig = True
        self.responses = {
            "hola": ["¡Hola! ¿Cómo estás?", "¡Hola! ¿En qué puedo ayudarte?", "¡Buenas! ¿Qué tal?"],
            "adiós": ["Adiós, ¡que tengas un buen día!", "Hasta luego, cuídate.", "Nos vemos, ¡hasta pronto!"],
            "cómo estás": ["Estoy bien, gracias por preguntar.", "¡Genial! ¿Y tú?", "¡Haciendo lo mejor posible por ayudar!"],
            "cuál es tu nombre": ["Soy un chatbot simple.", "Me llamo Bot, ¿y tú?", "No tengo un nombre específico, soy un asistente."],
            "cuál es tu función": ["Mi función es responder tus preguntas.", "Estoy aquí para ayudarte.", "¡Mi trabajo es chatear contigo!"]
        }
        self.default_response = [
            "No esoy seguro de cómo responder eso.",
            "Podrías intentar preguntarme algo más",
            "Lo siento, aún estoy aprendiendo. ¿Podrías preguntar de otra manera?"
        ]
    
    def start_chat(self):
        """
        Inicia el ciclo principal del chatbot.
        """
        print("ChatBox avanzado iniciado. Escribe 'salir' para finalizar.\n")
        while self.runnig:
            user_message = input("Usuario: ").strip().lower()
            
            if user_message == "salir":
                self.runnig = False
                print("ChatBox finalizado. Hasta luego!")
            else:
                bot_response = self.generate_response(user_message)
                print("Bot:", bot_response)
    
    def generate_response(self, user_message):
        """
        Genera una respuesta basada en palabras clave.
        """
        for keyword, response in self.responses.items():
            if keyword in user_message:
                return random.choice(response)
        # Si no se encuentra ninguna coincidencia, usa una respuesta predeterminada
        return random.choice(self.default_response)

# ==================================================
#                 EJECUCIÓN PRINCIPAL
# ==================================================

if __name__ == "__main__":
    chatbot = AdvancedChatBot()
    chatbot.start_chat()