from ula import ULA
from menu import Menu, MenuOption


def handle_read_a(ula: ULA):
    print(ula.read_register('A'))


def handle_read_b(ula: ULA):
    print(ula.read_register('B'))


def handle_write_a(ula: ULA):
    value = input("Insira o valor do registrador A: ")
    ula.write_register('A', value)


def handle_write_b(ula: ULA):
    value = input("Insira o valor do registrador B: ")
    ula.write_register('B', value)


def handle_write_op(ula: ULA):
    ula.print_operations()
    value = input("Insira a operação: ")
    ula.write_op(value)


def handle_exec_op(ula: ULA):
    ula.execute_operation()


menu = Menu(
    MenuOption(
        message='Definir o registrador A',
        callback=handle_write_a
    ),
    MenuOption(
        message='Definir o registrador B',
        callback=handle_write_b
    ),
    MenuOption(
        message='Ler o registrador A',
        callback=handle_read_a
    ),
    MenuOption(
        message='Ler o registrador B',
        callback=handle_read_b
    ),
    MenuOption(
        message='Definir operação',
        callback=handle_write_op
    ),
    MenuOption(
        message='Executar operação',
        callback=handle_exec_op
    ),
    loop=True,
)

menu.show()
