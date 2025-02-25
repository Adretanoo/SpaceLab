class Command:
    def execute(self):
        pass

class TurnOnCommand(Command):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.turn_on()

class TV:
    def turn_on(self):
        print("TV is on")

class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command: Command):
        self._command = command

    def press_button(self):
        self._command.execute()

tv = TV()
turn_on = TurnOnCommand(tv)
remote = RemoteControl()
remote.set_command(turn_on)
remote.press_button()
