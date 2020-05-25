import threading

from queue_item import QueueItem

CASH = 500
lock = threading.Lock()
queue = []


def addMoney(username, sum):
    global CASH
    lock.acquire()
    print(username + " added " + str(sum) + " to register!")
    CASH += sum
    print("Cash in register:" + str(CASH))
    lock.release()


def withdrewMoney(username, sum):
    lock.acquire()
    handleQueue(username, sum)
    lock.release()


def handleQueue(username, sum):
    global CASH
    if len(queue) > 0:
        queueItem = queue.pop(0)  # get first in line of queue
        if CASH > queueItem.money:
            CASH -= queueItem.money
            print(username + " has withdrew a sum of " + str(queueItem.money) + " from the register!")
        else:
            print("Insufficient funds for the user withdraw!!")
    else:
        print("Adding user to the queue.")
        queue.append(QueueItem(username, sum))


while True:
    # creating threads
    t1 = threading.Thread(target=addMoney("Georgi", 1000), args=(lock,))
    t2 = threading.Thread(target=withdrewMoney("Ivan", 2500), args=(lock,))

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()
