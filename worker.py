import multiprocessing
import time

def worker(name):
    print(f"{name} starting")
    time.sleep(2)
    print(f"{name} finished")

if __name__ == "__main__":
     p1=multiprocessing.Process(target=worker,args=("process 1",))
     p2=multiprocessing.Process(target=worker,args=("process 2",))

     p1.start()
     p2.start()

     p1.join()
     p2.join()

     print("Both processes finished!")



