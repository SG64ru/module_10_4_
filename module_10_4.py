import random
import threading
import time
from queue import Queue
from threading import Thread


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time_servis = random.randint(3, 10)
        time.sleep(time_servis)

class Cafe:
    def __init__(self, queue, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        # self.guest =Guest()
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f"{guest.name} сел за стол номер {table.number}")
                    table.guest.start()
                    break
                else:
                    self.queue.put(guest)
                    print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while (not self.queue.empty() or not (table.guest for table in self.tables)):
            for table in self.tables:
                if not table.guest is None and table.guest.is_alive():
                    table.guest.join()
                    print(f"{table.guest.name} покушал(-а) и ушёл(-ушла)")
                    table.guest = None
                    print(f"Стол номер {table.namber} свободен")
                elif not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f"{table.guest.name} вышел из очереди и сел за стол номер {table.namber}")
                table.guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

