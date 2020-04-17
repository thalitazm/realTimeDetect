import cv2

imagem = cv2.imread("beatles.jpg")
# o opencv tem uma função que ele escreve textos, não necessita de uma lógica compexa para escrever algo em cima de uma imagem
fonte = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(imagem, "texto", (50, 50), 2, fonte, (255, 0, 0), 2, cv2.LINE_AA ) #metodo que escreve as imagens sobre o opencv


cv2.imshow("janela", imagem)
cv2.waitKey(0)

