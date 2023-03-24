from multiprocessing import Process, Queue
import time

sus = ""

# must be a global function    
def my_function(a):
    print("dwdwwd" + a)
    while True:
        print("LEWLLLE" + sus)
        time.sleep(1)

sus = "OMFG YES ඞඞ"
print("abc koad")
if __name__ == '__main__':
    p = Process(target=my_function, args=("HM ARG", ))
    p.start()
    time.sleep(5)
    p.terminate()
    print("OKE :D")