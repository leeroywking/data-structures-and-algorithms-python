from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import AnimalShelter, Dog, Cat

def test_version():
    assert __version__ == '0.1.0'

def test_wiring():
    assert AnimalShelter
    assert AnimalShelter("PAWS")

def test_enqueue_dog():
    as1 = AnimalShelter("PAWS")
    dog1 = Dog("Rowdy Roddy Pawper")
    assert as1.enqueue(dog1) == "success"
    
def test_enqueue_dequeue_dog():
    as2 = AnimalShelter("RedRover")
    dog2 = Dog("Sherlock Hounds")
    as2.enqueue(dog2)
    as2.dequeue("dog").name == "Sherlock Hounds"

def test_enqueue_dequeue_dog_multiple():
    as3 = AnimalShelter("Save-a-Pet")
    dog3 = Dog("Stone Cold Steve Pawstin")
    dog4 = Dog("A dog with no name")
    as3.enqueue(dog3)
    as3.enqueue(dog4)
    assert as3.dequeue("dog").name == "Stone Cold Steve Pawstin"
    assert as3.dog_queue.peek().name == "A dog with no name"

def test_enqueue_dequeue_cat():
    as4 = AnimalShelter("Kitten Associates")
    cat1 = Cat("Senator Whiskers")
    as4.enqueue(cat1)
    assert as4.dequeue("cat").name == "Senator Whiskers"

def test_enqueue_dequeue_cat_multiple():
    as5 = AnimalShelter("The Cat Network")
    cat2 = Cat("Meow Capone")
    cat3 = Cat("Mathew Purrdrick")
    as5.enqueue(cat2)
    as5.enqueue(cat3)
    assert as5.dequeue("cat").name == "Meow Capone"
    assert as5.dequeue("cat").name == "Mathew Purrdrick"

def test_all_functions():
    as6 = AnimalShelter("Paws without Borders")
    dog5 = Dog("Tony Bark")
    dog6 = Dog("Steve Woofjers")
    dog7 = Dog("Natasha Roman-arf-a")
    cat4 = Cat("Clint Bartoffthecouch")
    cat5 = Cat("Mouse Banner")
    cat6 = Cat("Cat Danvers")
    as6.enqueue(dog5)
    as6.enqueue(cat4)
    as6.enqueue(dog6)
    as6.enqueue(cat5)
    as6.enqueue(dog7)
    as6.enqueue(cat6)
    assert as6.dequeue("cat") == cat4
    assert as6.dequeue("cat") == cat5
    assert as6.dequeue("dog") == dog5
    assert as6.dequeue("dog") == dog6
    assert as6.dequeue("cat") == cat6
    assert as6.dequeue("dog") == dog7
    
def test_stretch_goal_oldest_animal():
    as7 = AnimalShelter("Wags and Walks")
    dog8 = Dog("Anthony Walkin's")
    cat7 = Cat("Meowster Stallone")
    as7.enqueue(dog8)
    as7.enqueue(cat7)
    assert as7.dequeue().name == "Anthony Walkin's"
    assert as7.dequeue().name == "Meowster Stallone"