import cv2
import numpy as np

# definir o intervalo de cor a ser rastreado tanto em azul como em uma escala de cinza
azulEscuro = np.array([100, 67, 0], dtype = 'uint8') #cria vetor
azulClaro = np.array([255, 128, 50], dtype = "uint8") #dtype => tipo de dado

camera = cv2.VideoCapture(0)
# importante!!!! como é um video tem que estar dentro de um while verdadeiro (laço infinito) porque não se sabe quando a camera vai parar de gravar

while True:
    # metodo que pega o próximo frame => retorna duas coisas: valores da imagem e o frame em si
    (sucesso, frame) = camera.read()
    if not sucesso:
        break

#próximo passo: tratamento da imagem com limiarização
    objeto = cv2.inRange(frame, azulEscuro, azulClaro) # passa como parâmetro o frame e tudo que está entre o espaço de cor declarado: azul claro  e azul escuro, ou seja, tudo que está nesse intervalo fica branco e o resto fica preto // cria uma máscara

# próximo passo: identificação dos contornos:
    (cnts, _) = cv2.findContours(objeto.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # cv2.RETR_TRE => pega contornos em uma determinada hierarquia // cv2.CHAIN_APPROX_SIMPLE => deixa o algoritmo otimizado

    # cnts já foi declarada como variável no comando acima
    if len(cnts) > 0:
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        # próximo passo: determinar dois pontos para traçar um retângulo e é preciso identificar esses dois pontos
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))

        cv2.drawContours(frame, [rect], -1, (0, 255, 255), 2) # -1 para passar todos os contornos

    cv2.imshow("Captura", frame)
    cv2.imshow("Mascara", objeto)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()

