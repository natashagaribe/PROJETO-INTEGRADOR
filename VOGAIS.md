Aqui está um código Python que implementa um algoritmo que imprime apenas as vogais de determinada palavra ou frase:

def vogais(frase):
    vogais_lista = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    for letra in frase:
        if letra in vogais_lista:
            print(letra, end="")

frase_usuario = input("Digite uma palavra ou frase: ")
vogais(frase_usuario)

![image](https://github.com/user-attachments/assets/bd930000-9260-4c61-a5a2-f413defd237b)
![image](https://github.com/user-attachments/assets/ac492fd8-e1f4-408d-b425-880d2368c2c4)
![image](https://github.com/user-attachments/assets/882a7583-d6d1-471b-a647-23febf657b54)
