import matplotlib.pyplot as plt
import numpy as np
# Oscar Flores NC 1389
cant_productos = [100,150,200,300,500]
precio = [4000, 7000, 9000, 12000, 18000]

plt.plot(cant_productos,precio)
plt.show()
# uns manera sencilla de hacerlo

plt.plot(cant_productos, precio, color= 'blue', marker= 'o', linestyle= 'dashed', linewidth= 2, markersize= 12)
plt.title("Ventas de walmart 1389")
plt.xlabel("Cant_productos")
plt.ylabel("Precios")
plt.show()