"""
Código conversacional a través de la API KEY provista por OpeiAI.
"""
import argparse
from openai import OpenAI #Se importan las librerias correspondientes.

# Inicialización del cliente de OpenAI
client = OpenAI(api_key="------")
# hubo cambios
#recientemente en las librerias de OpenAI,
#me basé en la última Version: 1.14.3

# Definición de variables de contexto y usuario
CONTEXT = "Eres un astrónomo profesional"
USERTASK = "aprender"
USERQUERY = "-"

# Variable para almacenar la última
# consulta realizada y las respuestas de chatGPT
ultimo_convers = []

def procesar_consulta(consulta):
    """Procesa la consulta a través del parámetro 'consulta.'"""
    try:
        if consulta.strip(): # funcion strip utilizado
            #para eliminar caracteres de principio y de final.
            print(f"You: {consulta}")
            # Invocación del modelo de OpenAI
            #con la última consulta realizada
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {
                        "role": "system",
                        "content": CONTEXT, #El context lo doy arriba,
                        #pero no sé bien cual debería ser.
                    },
                    {
                        "role": "user",
                        "content": USERTASK, #user task la dejo vacía
                        #porque no sé qué debería ir
                    },
                    {
                        "role": "user",
                        "content": consulta # consulta es
                        #la que ocupo principalmente
                    }
                ],
                temperature=1, #Estas definidas por el profesor.
                #Excepto max_tokens que lo bajé a 150
                max_tokens=150, # para limitar tokens
                #y así ahorrar en la versión que tengo paga.
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            # Obtención de respuesta
            respuesta_chatgpt = response.choices[0].message.content #Finalmente captura la respuesta
            print(f"chatGPT: {respuesta_chatgpt}") # la devuelve
            # Agregar la consulta y la respuesta al buffer
            ultimo_convers.append((consulta, respuesta_chatgpt)) #se agrega a la lista

    except Exception as e: #Excepciones solicitadas y
        #se declara en "e" para mayor facilidad
        print(f"Error en el procesamiento de la consulta: {e}") # se muestra por pantalla.

# Manejar eventos de teclas utilizando readline
def manejar_eventos_teclado():
    """Maneja los eventos del teclado. No precisa parámetros."""
    global ultimo_convers
    while True:
        entrada = input("") #Se recibe entrada
        if entrada == "\x1b[A":  # "cursor Up"
            ultima_consulta = input("Ingrese su consulta (editar la última consulta): ")
            procesar_consulta(ultima_consulta) #se llama a procesar consulta nuevamente
        else:
            ultima_consulta = entrada
            procesar_consulta(entrada)

# Función para procesar el modo de conversación
def modo_conversacion():
    """Función para modo conversacional."""
    global ultimo_convers
    parser = argparse.ArgumentParser()
    parser.add_argument("--convers", action="store_true", help="Modo de conversación")
    args = parser.parse_args()

    if args.convers:
        print("Modo de conversación activado. Presione Ctrl + C para salir.")
        manejar_eventos_teclado()
    else:
        print("El argumento '--convers' no está presente. Ignorando el modo de conversación.")

# Ejecutar el programa
try:
    modo_conversacion()
except KeyboardInterrupt: #Una excepción fácil de probar
    print("\nSe ha interrumpido la ejecución del programa.")



# Los resultados obtenibles hasta el momento:
# "comment_ratio": 34.28088938924852,
#"halstead_effort": 35340.93501117314,
#"halstead_timerequired": 1963.3852783985078,
# "halstead_bugprop": 0.620503837984434,
# Comment_ratio está por encima del recomendado (33).
# Cuando ejecuté por primera vez me dió 27, así que
#realicé algunos comentarios adicionales.
# Los valores de halstead_effort y halstead_timerequired
#no tienen en tabla valores recomendados o sugeridos,
# por lo que no estoy seguro de qué conclusiones sacar a este respecto.
# El valor de referencia (recomendado) para
#halstead_bugprop es de 0.05 por lo que cuento con un valor realmente alto.
#El código fue especialmente complicado en algunas secciones.
#tales como incorporar manejo de teclado; y la parte conversacional.
# Respecto a como disminuir el índice de MacCabe de 10%
#puede ser simplificando funciones grandes y eliminando código inutil.
    