import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(5, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.setup(13, gpio.OUT)


#fazer um programa para piscar led x vezes
for x in range (1,10): #in range: numa determinada faixa, no caso,10x
    #configura saida // 2 parametros: a porta e se esta ligada ou desligada
    
    gpio.output(5, gpio.HIGH) #high = tempo fica ligado // pino 5 ligado
    gpio.output(6, gpio.LOW) #desligado
    gpio.output(13, gpio.LOW) #desligado
    time.sleep(0.5) 

    gpio.output(5, gpio.LOW)
    gpio.output(6, gpio.HIGH) #pino 6 ligado
    gpio.output(13, gpio.LOW)
    time.sleep(0.5) #low = tempo fica desligado

    gpio.output(5, gpio.LOW)
    gpio.output(6, gpio.LOW)
    gpio.output(13, gpio.LOW) #pino 6 ligado
    time.sleep(0.5)
    
#desliga programa gpio
gpio.cleanup()
