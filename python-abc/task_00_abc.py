#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite représentant un animal."""

    @abstractmethod
    def sound(self):
        """Méthode abstraite pour produire un son."""
        pass


class Dog(Animal):
    """Sous-classe représentant un chien."""

    def sound(self):
        """Renvoie le son que fait un chien."""
        return "Bark"


class Cat(Animal):
    """Sous-classe représentant un chat."""

    def sound(self):
        """Renvoie le son que fait un chat."""
        return "Meow"
