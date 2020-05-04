import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM) #modo numeração dos pinos // número fixo de cada porta

#controle led
gpio.setup(5, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.setup(13, gpio.OUT)

#configuração das outras 3 portas de entrada => botões
gpio.setup(23, gpio.IN, gpio.PUD_UP) #IN = recebe uma informação do circuito que está ligado
gpio.setup(24, gpio.IN, gpio.PUD_UP) # PUD_UP => porta forçada a ficar alta // até apertar o botão para desligar
gpio.setup(25, gpio.IN, gpio.PUD_DOWN) #PUD_DOWN => porta forçada a ficar em baixa // até apertar o botão para ligar 

#loop
while True:
    if gpio.input(23) == gpio.LOW:
        gpio.output(5, gpio.LOW)
    else:
        gpio.output(5, gpio.HIGH)

    if gpio.input(24) == gpio.LOW:
        gpio.output(6, gpio.HIGH)
    else:
        gpio.output(6, gpio.LOW)

    gpio.output(13, gpio.input(25))
    
#desliga programa gpio
gpio.cleanup()
