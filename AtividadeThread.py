# Importa o módulo threading, que é essencial para criar e gerenciar threads
import threading

# Importa o módulo time,que permite usar funções relacionadas a tempo,
# como o time.sleep() para pausar a execução
import time

# Importa o módulo math para funções matemáticas.
# Neste código específico, o módulo math e importado mas não é utilizado
import math

# Define uma função chamada estrutura que será executada por cada thread
# Esta função é genérica e pode imprimir qualquer sequência numérica
#   nome:O nome da thread para identificação na saída
#   inicio:O número inicial da sequência
#   fim:O número final da sequência
def estrutura(nome, inicio, fim):
    
    # Inicia um laço de repetição loop que vai do número inicio até o fim
    # O + 1 é necessário porque a função range() para um número antes do final
    for i in range(inicio, fim + 1):
        
        # Imprime na tela uma string formatada mostrando qual thread está
        # trabalhando e qual número ela está processando no momento
        print(f"{nome} -> {i}")

# Pausa a execução do SCRIPT PRINCIPAL a thread principal por 5 segundo
# Isso acontece antes da criação ou início das outras threads
# Neste código,não tem muito efeito prático,apenas atrasa o início de tudo
time.sleep(5)

# Cria o objeto da primeira thread
#   target=estrutura: Define que a função a ser executada por esta thread é a estrutura
#   args=("Thread-1", 1, 10): Passa os argumentos para a função estrutura
#   É importante que os argumentos sejam passados dentro de uma tupla ()
thread1 = threading.Thread(target=estrutura, args=("Thread-1", 1, 10))

# Cria o objeto da segunda thread, que executará a mesma função estrutura
# mas com argumentos diferentes para imprimir outra sequência
thread2 = threading.Thread(target=estrutura, args=("Thread-2", 50, 60))

# Inicia a execução da thread1. A partir deste ponto, a função estrutura
# com os argumentos de thread1 começa a rodar em paralelo
# O script principal não espera a thread terminar,ele continua imediatamente
thread1.start()

# Inicia a execução da thread2, que também rodará em paralelo com o
# script principal e com a thread1
thread2.start()

# O método .join() bloqueia a execução do script principal
# O programa vai parar nesta linha e só continuará depois que a thread1
# tiver terminado completamente sua tarefa (imprimir de 1 a 10)
thread1.join()

# Após a thread1 terminar,o programa principal chega a esta linha
# Agora, ele vai esperar a thread2 terminar sua tarefa por completo
# (imprimir de 50 a 60).
thread2.join()

# Somente após as duas threads finalizarem, o script chegaria ao fim e seria encerrado.
# Isso garante que o programa não termine prematuramente.
