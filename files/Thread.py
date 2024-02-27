import time
import threading

# global_num= 10
# def func():
#     global global_num
#     time.sleep(10)
#     global_num = 11
#
# thread1 = threading.Thread(target=func)
# thread1.start()
# #thread1.join()
# print("end")

def printinto(name, max, file_name, lock):
    for i in range(max):
        lock.acquire()
        file = open(file_name, "a")
        file.write(f"{name}, {i} \n")
        file.close()
        time.sleep(0.2)
        lock.release()



lock9= threading.Lock()
# lock8 = threading.Lock()
thread3= threading.Thread(target=printinto, args=("thread3",10, "doc.txt", lock9))
thread4= threading.Thread(target=printinto, args=("thread4",10, "doc.txt", lock9))
thread3.start()
thread4.start()