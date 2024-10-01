import tkinter as tk #usamos esta libreria para crear graficos

# Creamos la ventana principal de nuestra aplicación
root = tk.Tk()
root.title("Calculadora básica con Python v.01")

# Creamos una variable de tipo StringVar para almacenar el texto que se mostrará en la entrada
entrada = tk.StringVar()

# Creamos un campo de entrada donde se mostrarán los números y el resultado
entry = tk.Entry(root, textvariable=entrada, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)  # Ubicamos el campo en la cuadrícula

# Lista de botones que se mostrarán en la calculadora
botones = ['7', '8', '9', '/',
           '4', '5', '6', '*',
           '1', '2', '3', '-',
           'C', '0', '=', '+']

# Variables para controlar la posición de los botones en la cuadrícula
row = 1
col = 0

# Variables para almacenar el resultado de las operaciones y la operación actual
resultado = 0
operacion = None

# Función que se ejecuta cuando se hace clic en un botón
def btn_click(item):
    global resultado, operacion

    # Si el botón presionado es un operador (+, -, *, /)
    if item in ['+', '-', '*', '/']:
        try:
            # Convertimos el texto en la entrada a un número flotante y lo guardamos en resultado
            resultado = float(entrada.get())
            # Guardamos el operador para usarlo en la siguiente operación
            operacion = item
            # Limpiamos la entrada para el siguiente número
            entrada.set("")
        except ValueError:  # Si no se puede convertir a número, mostramos un mensaje de error
            entrada.set("Error")

    # Si el botón presionado es el signo igual (=)
    elif item == '=':
        try:
            # Convertimos el texto en la entrada a un número flotante y lo guardamos en segundo_operando
            segundo_operando = float(entrada.get())
            # Realizamos la operación correspondiente según el operador guardado
            if operacion == '+':
                resultado = resultado + segundo_operando
            elif operacion == '-':
                resultado = resultado - segundo_operando
            elif operacion == '*':
                resultado = resultado * segundo_operando
            elif operacion == '/':
                if segundo_operando == 0:
                    entrada.set("Error: División por cero")
                else:
                    resultado = resultado / segundo_operando
            # Mostramos el resultado en la entrada
            entrada.set(str(resultado))
            # Reiniciamos la operación para la siguiente operación
            operacion = None
        except ValueError:
            entrada.set("Error")

    # Si el botón presionado es "C" (limpiar)
    elif item == 'C':
        # Limpiamos la entrada, reiniciamos el resultado y la operación
        entrada.set("")
        resultado = 0
        operacion = None

    # Si el botón presionado es un número, lo agregamos al texto de la entrada
    else:
        entrada.set(entrada.get() + item)

# Creamos los botones y los ubicamos en la cuadrícula
for button in botones:
    tk.Button(
        root, text=button, font=("Helvetica", 12),
        command=lambda item=button: btn_click(item)
    ).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Iniciamos el bucle principal de la aplicación
root.mainloop()