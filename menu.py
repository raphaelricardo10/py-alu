class MenuOption:
    def __init__(self, message=None, callback=None) -> None:
        self.message = message
        self.callback = callback


class Menu:
    def __init__(self, *options) -> None:
        self.options: list[MenuOption] = options

    def show(self):
        counter = 1
        for option in self.options:
            print(f'{counter}- {option.message}')
            counter += 1

        ans = int(input('Selecione uma opção'))
        selectedCallback = self.options[ans - 1].callback

        if isinstance(selectedCallback, Menu):
            return selectedCallback.show()

        return selectedCallback()
