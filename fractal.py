from PIL import Image, ImageDraw
import matplotlib as mpl
import numpy as np


def mandelbrot(z, c):
    n = 0
    MAX_ITER = 80
    while np.abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n


def getColor(n, MAX_ITER, c1, c2, c3,):
    if n == MAX_ITER:
        return c3
    else:
        a = c1
        b = c2
        t = np.power(n, 2) / MAX_ITER
        return (int((a[0] + (b[0] - a[0]) * t)), int((a[1] + (b[1] - a[1]) * t)), int((a[2] + (b[2] - a[2]) * t)))


def makeImage():
    z = np.random.uniform(.05, .95)
    c1 = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
    c2 = (np.abs(255-c1[0]), np.abs(255-c1[0]), np.abs(255-c1[0]))
    c3 = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))


    MAX_ITER = 80
    # Image size (pixels)
    WIDTH = 600
    HEIGHT = 400

    # Plot window
    RE_START = -2
    RE_END = 1
    IM_START = -1
    IM_END = 1


    palette = []

    im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            # Compute the number of iterations
            m = mandelbrot(z, c)
           # print(m)
            # The color depends on the number of iterations
            color = getColor(m, MAX_ITER, c1, c2, c3)
            # Plot the point
            draw.point([x, y], color)
    im.save('app/static/images/fractal.png', 'PNG')