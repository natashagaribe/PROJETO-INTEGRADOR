AULA 03 - LINGUAGENS DE PROGRAMAÇÃO
Python: Linguagem de alto nível, interpretada, dinamicamente tipada e multi-paradigmam, ou seja, mais fácil de aprender e escrever, não precisa ser compilada antes de ser executada, permite alterar o tipo das variáveis em tempo de execução e que suporta vários estilos de programação, como orientada a objetos, funcional, imperativa e procedural. É conhecida por sua simplicidade, legibilidade e expressividade, além de ter uma grande comunidade e uma vasta biblioteca de módulos e pacotes para diversas finalidades.
C++: Linguagem de médio nível, compilada, estaticamente tipada e orientada a objetos, ou seja, mais próxima da linguagem de máquina, precisa ser traduzida para código executável antes de ser executada, exige a declaração do tipo das variáveis antes de usá-las e se baseia no conceito de classes, objetos, herança e polimorfismo. É uma extensão da linguagem C, que adiciona recursos de programação orientada a objetos e genérica. Conhecida por sua eficiência, desempenho e flexibilidade, além de ser amplamente usada em sistemas operacionais, jogos, aplicativos gráficos e de rede.
C#: Linguagem de alto nível, compilada, estaticamente tipada e multi-paradigma, ou seja, mais fácil de ler e escrever, precisa ser compilada antes de ser executada, exige a declaração do tipo das variáveis antes de usá-las e suporta vários estilos de programação, como orientada a objetos, funcional, imperativa e declarativa. É uma linguagem desenvolvida pela Microsoft, faz parte da plataforma .NET, oferece um ambiente de execução e uma biblioteca de classes para diversas finalidades. É conhecida por sua elegância, consistência e produtividade, além de ser amplamente usada em aplicações web, móveis, desktop e de nuvem.

CÓDIGOS
Python: 
# Solicita o nome do usuário
nome = input("Qual é o seu nome? ")
# Imprime uma saudação
print(f"Olá {nome}, esse é o meu programa em Python.")

![image](https://github.com/user-attachments/assets/00d18b3c-65de-487c-a7fd-19f961cd5423)
![image](https://github.com/user-attachments/assets/0f5190f2-712b-4694-aca8-759eb9003476)
![image](https://github.com/user-attachments/assets/852accca-f9cb-4e54-ab07-3908d828decf)

C++:
#include <iostream>
#include <string>

int main() {
    // Cria uma variável para armazenar o nome do usuário
    std::string nome;

    // Solicita que o usuário insira seu nome
    std::cout << "Digite seu nome: ";
    std::getline(std::cin, nome);

    // Exibe a mensagem de saudação com o nome do usuário
    std::cout << "Olá " << nome << ", esse é o meu programa em C++" << std::endl;

    return 0;
}

![image](https://github.com/user-attachments/assets/8f0bbfc0-bdc4-4e7a-ae79-5bda09c7c076)
![image](https://github.com/user-attachments/assets/d608e8ac-4911-4a6d-b848-eda4b21a4a80)
![image](https://github.com/user-attachments/assets/ac81e581-b5fa-4846-9d2f-7088e81bf89d)

C#:
using System;

class Program
{
    static void Main()
    {
        // Solicita que o usuário insira seu nome
        Console.Write("Digite seu nome: ");
        string nome = Console.ReadLine();

        // Exibe a mensagem de saudação com o nome do usuário
        Console.WriteLine("Olá " + nome + ", esse é o meu programa em C#");
    }
}

![image](https://github.com/user-attachments/assets/2b886410-5b0f-496b-9bd4-291167395c28)
![image](https://github.com/user-attachments/assets/25f8ef05-7a43-4418-b549-f760bdba9fd1)
![image](https://github.com/user-attachments/assets/f616a8eb-8bfb-464e-b6cb-39f5b0839b0d)
