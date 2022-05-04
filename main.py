from ula import ULA
from menu import Menu, MenuOption


def print_hello():
    n1 = input("Insira um numero")
    n2 = input("Insira outro numero")
    print(n1 + n2)


menu = Menu(
    MenuOption('Somar dois números', print_hello),
    MenuOption('Outro menu',
               Menu(
                   MenuOption('Somar tres numeros', print_hello)
               ),
               ),
)

#menu.show()

ula = ULA(2, 1, 1)
print(ula.registers.A, ula.registers.B)

ula.execute_instruction()
print(ula.registers.A, ula.registers.flags.zero)
