def sierpinksi(x, y, length):
    if(length <= 20):
        triangle(x, y, x + length, y, x + int(length/2), y - length)
    else:
        sierpinski(x, y, int(length/2))
        sierpinski(x + int(length/4), y - int(length/2), int(length/2))