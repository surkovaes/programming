import random
import os
import segno

def create_qrcode(text: str):
    qrcode = segno.make(text, version=2, error='h')
    qrcode.show()


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = '#%02x%02x%02x' % (r, g, b)
    return color


def create_colored_qrcode(text: str):
    qrcode = segno.make(text, version=2, error='h')
    qrcode.save('qrcode.png', scale=10,
                dark=get_random_color(),
                data_dark=get_random_color(),
                finder_dark=get_random_color(),
                timing_dark=get_random_color())
    os.system('qrcode.png')


if __name__ == '__main__':
    create_qrcode('Python')
    create_colored_qrcode('Python')
