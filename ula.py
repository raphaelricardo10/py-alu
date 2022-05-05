class FlagGroup:
    def __init__(self) -> None:
        self.clear()

    def clear(self):
        self.carry = 0
        self.overflow = 0
        self.zero = 0


class RegisterGroup:
    def __init__(self, A=0, B=0, C=0, D=0, size=4) -> None:
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.flags = FlagGroup()


class ULA:
    def __init__(self, A=None, B=None, op=None, size=4) -> None:
        if A and B:
            self.registers = RegisterGroup(
                A=ULA.binary_parse(A, size),
                B=ULA.binary_parse(B, size),
            )
        else:
            self.registers = RegisterGroup()

        self.size = size

        if op:
            self.write_op(op)
        else:
            self.op = None

        self.operations: list[function] = [self.sum, self.sub, self.product]

    def binary_parse(number: str, size: int):
        if len(number) > size:
            raise ValueError(
                f"A entrada {number} extrapola o tamanho de {size} bits da ULA!")
        try:
            number = int(number, 2)

        except ValueError:
            raise ValueError(f"Somente os valores 0 e 1 são permitidos!")

        return number

    def read_register(self, register: str):
        if register == 'A':
            register = self.registers.A
        elif register == 'B':
            register = self.registers.B
        elif register == 'C':
            register = self.registers.C
        elif register == 'D':
            register = self.registers.D
        else:
            raise ValueError("Este registrador não existe na ULA!")

        return f"{register:0{self.size}b}"

    def write_register(self, register: str, value: bin):
        value = ULA.binary_parse(value, self.size)

        if register == 'A':
            self.registers.A = value
        elif register == 'B':
            self.registers.B = value
        elif register == 'C':
            self.registers.C = value
        elif register == 'D':
            self.registers.D = value
        else:
            raise ValueError("Este registrador não existe na ULA!")

    def write_op(self, value):
        self.op = ULA.binary_parse(value, self.size)

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
            self.registers.C = self.registers.B

        if self.registers.C == 0:
            return

        self.registers.flags.carry = (~self.registers.A) & self.registers.C

        # Subtraction of bits of x
        # and y where at least one
        # of the bits is not set
        self.registers.A = self.registers.A ^ self.registers.C

        # Borrow is shifted by one
        # so that subtracting it from
        # x gives the required sum
        self.registers.C = self.registers.flags.carry << 1

        return self.sub(carry=True)

    def product(self, carry=False):
        if not carry:
            self.registers.C = self.registers.A
            self.registers.D = self.registers.B
            self.registers.A = 0

        if self.registers.D <= 0:
            return

        if self.registers.D & 1:
            self.registers.A = self.registers.A + self.registers.C

        self.registers.C = self.registers.C << 1
        self.registers.D = self.registers.D >> 1

        self.product(carry=True)

    def print_operations(self):
        counter = 0
        options = [
            "Soma",
            "Subtração",
            "Multiplicação"
        ]
        for option in options:
            print(f"{counter:03b}- {option}")
            counter += 1

    def execute_operation(self):
        if self.op is None:
            raise ValueError("Selecione uma opção!")

        self.operations[self.op]()
        self.registers.flags.zero = self.registers.A == 0
        self.registers.flags
