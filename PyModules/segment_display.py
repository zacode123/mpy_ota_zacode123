from machine import Pin

D0 = Pin(16, Pin.OUT)
D1 = Pin(5, Pin.OUT)
D2 = Pin(4, Pin.OUT)
D4 = Pin(2, Pin.OUT)
D5 = Pin(14, Pin.OUT)
D6 = Pin(12, Pin.OUT)
D7 = Pin(13, Pin.OUT)
D8 = Pin(15, Pin.OUT)
P3 = Pin(3, Pin.OUT) 

def write(input):
    input = input.lower()
    D0.value(0)
    D1.value(0)
    D2.value(0)
    D4.value(0)
    D5.value(0)
    D6.value(0)
    D7.value(0)
    D8.value(0)
    P3.value(1 if input.isalpha() else 0)

    if input == '0':
        D0.value(1); D1.value(1); D5.value(1); D6.value(1); D7.value(1); D4.value(1)
    elif input == '1':
        D1.value(1); D5.value(1)
    elif input == '2':
        D0.value(1); D1.value(1); D2.value(1); D7.value(1); D6.value(1)
    elif input == '3':
        D0.value(1); D1.value(1); D2.value(1); D5.value(1); D6.value(1)
    elif input == '4':
        D4.value(1); D2.value(1); D1.value(1); D5.value(1)
    elif input == '5':
        D0.value(1); D4.value(1); D2.value(1); D5.value(1); D6.value(1)
    elif input == '6':
        D0.value(1); D4.value(1); D7.value(1); D6.value(1); D5.value(1); D2.value(1)
    elif input == '7':
        D0.value(1); D1.value(1); D5.value(1)
    elif input == '8':
        D0.value(1); D1.value(1); D2.value(1); D7.value(1); D6.value(1); D5.value(1); D4.value(1)
    elif input == '9':
        D2.value(1); D4.value(1); D0.value(1); D1.value(1); D5.value(1); D6.value(1)
    elif input == 'a':
        D2.value(1); D7.value(1); D6.value(1); D5.value(1); D1.value(1); D0.value(1); D8.value(1)
    elif input == 'b':
        D2.value(1); D5.value(1); D6.value(1); D7.value(1); D4.value(1)
    elif input == 'c':
        D0.value(1); D4.value(1); D7.value(1); D6.value(1)
    elif input == 'd':
        D2.value(1); D7.value(1); D6.value(1); D5.value(1); D1.value(1); D8.value(1)
    elif input == 'e':
        D2.value(1); D1.value(1); D0.value(1); D4.value(1); D7.value(1); D6.value(1)
    elif input == 'f':
        D0.value(1); D4.value(1); D7.value(1); D2.value(1)
    elif input == 'g':
        D0.value(1); D4.value(1); D2.value(1); D1.value(1); D5.value(1); D6.value(1)
    elif input == 'h':
        D4.value(1); D7.value(1); D2.value(1); D5.value(1)
    elif input == 'i':
        D1.value(1); D5.value(1); D8.value(1)
    elif input == 'j':
        D1.value(1); D5.value(1); D6.value(1)
    elif input == 'k':
        D4.value(1); D7.value(1); D2.value(1); D1.value(1); D5.value(1)
    elif input == 'l':
        D4.value(1); D7.value(1); D6.value(1)
    elif input == 'm':
        D6.value(1); D7.value(1); D2.value(1); D4.value(1); D0.value(1); D8.value(1)
    elif input == 'n':
        D7.value(1); D2.value(1); D5.value(1)
    elif input == 'o':
        D2.value(1); D5.value(1); D6.value(1); D7.value(1)
    elif input == 'p':
        D0.value(1); D1.value(1); D2.value(1); D4.value(1); D7.value(1)
    elif input == 'q':
        D0.value(1); D4.value(1); D2.value(1); D1.value(1); D5.value(1)
    elif input == 'r':
        D4.value(1); D7.value(1); D0.value(1); D1.value(1)
    elif input == 's':
        D0.value(1); D4.value(1); D2.value(1); D5.value(1); D6.value(1)
    elif input == 't':
        D4.value(1); D7.value(1); D6.value(1); D2.value(1)
    elif input == 'u':
        D7.value(1); D6.value(1); D5.value(1)
    elif input == 'v':
        D4.value(1); D6.value(1); D1.value(1)
    elif input == 'w':
        D6.value(1); D5.value(1); D2.value(1); D1.value(1); D0.value(1); D8.value(1)
    elif input == 'x':
        D4.value(1); D5.value(1); D2.value(1); D7.value(1)
    elif input == 'y':
        D4.value(1); D2.value(1); D1.value(1); D5.value(1); D6.value(1)
    elif input == 'z':
        D0.value(1); D1.value(1); D7.value(1); D6.value(1)
    elif input == '.':
        D8.value(1)
    else:
        D0.value(0); D1.value(0); D2.value(0); D4.value(0)
        D5.value(0); D6.value(0); D7.value(0); D8.value(0)

def show(text, speed=2000):
    for ch in text:
        write(ch)
        sleep_ms(speed)
