class FlagGroup:
    def __init__(self) -> None:
        self.clear()

    def clear(self):
        self.carry = 0
        self.borrow = 0
        self.overflow = 0
        self.zero = 0

class RegisterGroup:
    def __init__(self, A=0, B=0, C=0,size=4) -> None:
        self.A = A
        self.B = B
        self.C = C
        self.size = size
        self.flags = FlagGroup()

    def binary_check(number):
        pass

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        self._A = value

class ULA:
    def __init__(self, A=0, B=0, op=0, size=4) -> None:
        self.registers = RegisterGroup(A, B, size)
        self.op = op

        self.operations: list[function] = [self.sum, self.sub]

    def sum(self, carry=False):
        if not carry:
            self.registers.C = self.registers.B

        if self.registers.C == 0:
            return

        self.registers.flags.carry = self.registers.A & self.registers.C

        self.registers.A = self.registers.A ^ self.registers.C
        
        self.registers.C = self.registers.flags.carry << 1

        return self.sum(carry=True)

    def sub(self, carry=False):
        if not carry:
            self.registers.flags.carry = self.registers.B

        if self.registers.flags.carry == 0:
            return

        self.registers.flags.borrow = (~self.registers.A) & self.registers.flags.carry

        # Subtraction of bits of x
        # and y where at least one
        # of the bits is not set
        self.registers.A = self.registers.A ^ self.registers.flags.carry

        # Borrow is shifted by one
        # so that subtracting it from
        # x gives the required sum
        self.registers.flags.carry = self.registers.flags.borrow << 1

        return self.sub(carry=True)

    def execute_instruction(self):
        self.registers.flags.clear()
        self.operations[self.op]()