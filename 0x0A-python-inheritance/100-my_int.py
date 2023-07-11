#!/usr/bin/python3
"""a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Overrides == opeartors with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overrides != operators with == behaviors."""
        return self.real == value
