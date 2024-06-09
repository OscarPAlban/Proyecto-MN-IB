
#                       PROYECTO ARQUITECTURA - METODOS NUMERICOS

# Paquetes necesarios
from scipy.optimize import bisect

# Funcion que calcula la raiz
def root(x1, x2, h):
    # Funcion que calcula W
    def w(w):
        return (h*w) / (x2**2 - w**2)**0.5 + (h*w) / (x1**2 - w**2)**0.5 - w
    
    # Estimación de intervalo
    a = 0.01
    b = min(x1, x2) - 0.01
    
    try:
        root = bisect(w, a = a, b = b)
        return root
    
    except:
        return None

# INICIO DEL PROGRAMA

# Control de entrada de enteros usando excepciones
while True:
    x1 = input("Ingrese el valor de la longitud de la escalera 1 en metros (m): ")
    x2 = input("Ingrese el valor de la longitud de la escalera 2 en metros (m): ")
    h = input("Ingrese la altura en metros desde el suelo hacia la intersección entre las escaleras: ")
    
    try:
        x1 = float(x1)
        x2 = float(x2)
        h = float(h)
        
    except:
        print("Ingrese números por favor")
        
    else:
        break

root = root(x1, x2, h)

if root:
    print(f"El valor en metros de la distancia o ancho del pasillo para las escaleras y su altura es: {root}")

else:
    print("No hay solucion para las longitudes dadas")