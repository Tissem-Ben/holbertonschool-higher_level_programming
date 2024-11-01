#!/usr/bin/env python3
"""Shebang line indicating the interpreter for the script."""


class SwimMixin:
    """Defines Mixin class"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Defines Mixin class"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Defines dragon class"""
    def roar(self):
        print("The dragon roars!")
