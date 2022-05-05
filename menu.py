from ula import ULA


class MenuOption:
    def __init__(self, message=None, callback=None) -> None:
        self.message = message
        self.callback = callback


class Menu:
    def __init__(self, *options, loop=False, ula=None) -> None:
        self.options: list[MenuOption] = options

        self.loop = loop
        self.ula = ula if ula else ULA()

    def show(self):
        while True:
            counter = 1
            lastOption = len(self.options) + 1
            for option in self.options:
                print(f'{counter}- {option.message}')
                counter += 1
            print(f"{lastOption}- Sair")
            ans = int(input('Selecione uma opção: '))

            if ans == lastOption:
                break

            selectedCallback = self.options[ans - 1].callback

            if isinstance(selectedCallback, Menu):
                return selectedCallback.show()

            selectedCallback(self.ula)

            if not self.loop:
                break
