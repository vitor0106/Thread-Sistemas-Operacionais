import threading
import time
import math

def estrutura(nome, inicio, fim):
    for i in range(inicio, fim + 1):
        print(f"{nome} -> {i}")

time .sleep(1)

thread1 = threading.Thread(target=estrutura, args=("Thread-1", 1, 10))
thread2 = threading.Thread(target=estrutura, args=("Thread-2", 50, 60))


thread1.start()
thread2.start()

thread1.join()
thread2.join()