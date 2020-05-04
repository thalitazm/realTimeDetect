import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.output(11, GPIO.HIGH) #GPIO.output => número do pino, estado do pino)
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
# aqui foram usadas as numerações: 11, 13,15 e 16
# exemplo de estado do pino: [HIGH/1], [LOW/0]
# 1 = nível lógico alto // 0 = nível lógico baixo

# Entradas PonteH[Pino GPIO] => Para o robô girar para a frente:
#IN 1 [Pino 11]: HIGH = '1'
#IN 2 [Pino 15]: HIGH = '0'
#IN 3 [Pino 13]: HIGH = '0'
#IN 4 [Pino 16]: HIGH = '1'

# Entradas PonteH[Pino GPIO] => Para o robô girar para trás:
#IN 1 [Pino 11]: HIGH = '0'
#IN 2 [Pino 13]: HIGH = '1'
#IN 3 [Pino 15]: HIGH = '1'
#IN 4 [Pino 16]: HIGH = '0'

# Entradas PonteH[Pino GPIO] => Para o robô mover sentido horário:
#IN 1 [Pino 11]: LOW = '0'
#IN 2 [Pino 13]: HIGH = '1'
#IN 3 [Pino 15]: LOW = '0'
#IN 4 [Pino 16]: HIGH = '0'

# Entradas PonteH[Pino GPIO] => Para o robô mover sentido anti-horário:
#IN 1 [Pino 11]: HIGH = '1'
#IN 2 [Pino 13]: LOW = '0'
#IN 3 [Pino 15]: HIGH = '1'
#IN 4 [Pino 16]: LOW = '0'