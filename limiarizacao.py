############################## Limiarização ##############################
# limiarização: torna uma imagem binária
# técnica para visualizar elemntos na imagem impossível de visualizar na imagem original

import cv2
import matplotlib.pyplot as plt

foo = cv2.imread("foofighters.jpg")
#foo é a variável declarada para a leitura da imagem jpg

for i in range(0, foo.shape[0]):
    for j in range(0, foo.shape[1]):
        foo[i][j] = (0, 0, 0) # define que toda a imagem é preta

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(foo, '255', (15, 65), font, 2, (255, 255, 255), 2) #cv2.LINE_AA é para a letra não ficar serrilhada
cv2.putText(foo, '70', (125, 65), font, 2, (70, 70, 70), 2)
cv2.putText(foo, '100', (255, 65), font, 2, (100, 100, 100), 2)
cv2.putText(foo, '1', (405, 65), font, 2, (1, 1, 1), 2)
# o 1 é impossível enxergar a olho nu na imagem porque se aproxima muito do preto e por isso é necessário fazer algusn tratamentos,
# como a limiarização

for i in range(0, foo.shape[0]):
    for j in range(0, foo.shape[1]):
        #if foo [i][j][0] == 0: # ex: se a imagem na posição i, j e 0 é igual a zero, não precisa de um and, mas se fossem valores diferentes precisaria, ou seja, as duas condições deveriam ser iguais
        # if imagem[i][j][0] == 0 and imagem [i][j][1] => and para a posição 2
        if foo[i][j][0] != 0: # deixar diferente de zero porque se não some o 255 e aí seria somente inversão do fundo
            foo[i][j] = (255, 255, 255) # tudo que não for fundo da imagem recebe branco completo




cv2.imshow("janela", foo)
cv2.waitKey(0)