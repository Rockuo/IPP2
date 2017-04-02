from typing import List
from .Constants import CommandTemplate


class Command:
    def __init__(self, type: str = "", value: str = "") -> None:
        self._type = type
        self._value = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get_start(self) -> str:
        return CommandTemplate[self.type]['start'] + self.value + '>'

    def get_end(self) -> str:
        return CommandTemplate[self.type]['end']


class Commands:
    def __init__(self) -> None:
        self._commands: List[Command] = []

    def push(self, command: Command):
        self._commands.append(command)

    def get_start(self) -> str:
        out: str = ""
        for command in self._commands:
            out += command.get_start()
        return out

    def get_end(self) -> str:
        out: str = ""
        for command in reversed(self._commands):
            out += command.get_end()
        return out
