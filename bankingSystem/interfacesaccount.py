from abc import ABC, abstractmethod

class IAccount(ABC):
    @abstractmethod
    def deposit(self, amount): pass

    @abstractmethod
    def withdraw(self, amount): pass

    @abstractmethod
    def transfer(self, amount, target_account): pass

    @abstractmethod
    def close_account(self): pass

    @abstractmethod
    def view_details(self): pass
