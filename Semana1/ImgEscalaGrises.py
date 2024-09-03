# Importar la biblioteca necesarios
import cv2;
import matplotlib.pyplot as plt


# Especificar ruta de la imágen
dirArchivo = 'img/3.jpg'

# Leer la imágen usando OpenCV
image = cv2.imread(dirArchivo)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Imagen con escala de grises')
plt.imshow(image_gray, cmap='gray')
plt.axis('off')

plt.show();

# Leer la imagen usando OpenCV (esto lee la imagen en formato BGR por defecto)
image = cv2.imread(dirArchivo, cv2.IMREAD_UNCHANGED)  # IMREAD_UNCHANGED para leer todas las capas

# Determinar el número de capas (canales)
if len(image.shape) == 2:
    channels = 1  # Imagen en escala de grises
elif len(image.shape) == 3:
    channels = image.shape[2]  # Número de canales para una imagen a color o con canal alfa

# Imprimir información sobre el número de capas
print(f'Número de capas (canales): {channels}')
if channels == 1:
    print('La imagen es en escala de grises.')
elif channels == 3:
    print('La imagen es a color (RGB).')
elif channels == 4:
    print('La imagen es a color con canal alfa (RGBA).')
else:
    print('La imagen tiene un número de capas inesperado.')

# Mostrar la imagen si es en RGB o RGBA
if channels == 3 or channels == 4:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title(f'Imagen con {channels} canales')
    plt.axis('off')
    # plt.show()
elif channels == 1:
    # Mostrar la imagen si es en escala de grises
    plt.imshow(image, cmap='gray')
    plt.title('Imagen en escala de grises')
    plt.axis('off')
    plt.show()

