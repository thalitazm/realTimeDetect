############### Revisão Python #################

######## Estrutura de decisão  - if ########

# x = 19
x = 10
if x > 10:
    print("Olá, mundo!")
print("Não se preocupe, vai ficar tudo bem!")

######## Estrutura de repetição: while ########
#while true: => fica um loop infinito // para não cair no loop infinito, coloca-se x = x+1 que é a mesma coisa que x+=1

while x < 20:
    print("Hello, world!")
    x += 1

######## Estrutura de repetição: for ########

for i in range(0, 10): #comando importante para detecção de cor!
    print(i)

######## Listas ########
# em python não tem array, tem listas direto como no exemplo abaixo:
x = [1, 2, 3, 4, 5] # a lista não quantidade máxima de termos
x.append(10) #inclui o valor 10 na última posição
print(x)
#x.pop => apaga valores da lista

######## Importante! Usa-se bastante em processamento de imagens ########

print(x[:3]) # printa três posições da lista
print(x[::2]) # printa valores de dois em dois
print(x[::-1]) # printa de trás para frente => função inversa

# uma imagem é uma matrix: lista dentro de lista
# ex=> corte de uma imagem => print(x[2:4])



















