from fifo_animal_shelter.stacks_and_queues import Stack, Queue

class AnimalShelter:
    def __init__(self, shelter_name):
        self.name = shelter_name
        self.dog_queue = Queue()
        self.cat_queue = Queue()
        self.count = 0


    def enqueue(self, animal):
        animal["arrival"] = self.count
        self.count += 1
        if animal.type == "dog":
            self.dog_queue.enqueue(animal)
            return "success"
        elif animal.type == "cat":
            self.cat_queue.enqueue(animal)
            return "success"
        
        else:
            return None
        
    def dequeue(self, pref = None):
        if pref == "dog":
            return self.dog_queue.dequeue()
        elif pref == "cat":
            return self.cat_queue.dequeue()
        else:
            if self.dog_queue.is_empty():
                return self.cat_queue.dequeue()
            elif self.cat_queue.is_empty():
                return self.dog_queue.dequeue()
                
            oldest_cat_arrival = self.cat_queue.peek().arrival
            oldest_dog_arrival = self.dog_queue.peek().arrival
            if oldest_cat_arrival < oldest_dog_arrival:
                return self.cat_queue.dequeue()
            else:
                return self.dog_queue.dequeue()


class Dog:
    def __init__(self, dog_name):
        self.name = dog_name
        self.type = "dog"
        self.arrival = 0

    def __setitem__(self, key, value):
       print(key, value)

class Cat:
    def __init__(self, cat_name):
        self.name = cat_name
        self.type = "cat"
        self.arrival = 0


    def __setitem__(self, key, value):
       print(key, value)