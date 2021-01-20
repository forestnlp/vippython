class Unit:
    pass

class Cpu:
    pass


class Memory:
    def __init__(self, Unit):
        self.Unit = Unit


class Computer:
    def __init__(self, Cpu, Memory):
        self.cpu = Cpu
        self.memory = Memory


cpu = Cpu()
memory = Memory(Unit())

computer = Computer(cpu, memory)

print(computer, cpu, memory, memory.Unit)

import copy

computer2 = copy.copy(computer)
print(computer2, computer2.cpu, computer2.memory, computer2.memory.Unit)

# deep copy
computer3 = copy.deepcopy(computer)
print(computer3, computer3.cpu, computer3.memory, computer3.memory.Unit)
