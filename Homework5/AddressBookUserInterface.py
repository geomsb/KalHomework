from tkinter import *
from AddressBook import AddressBook, Address

class AddressBookUserInterface:
    def __init__(self):
        self.__addressBook = AddressBook()
        window = Tk()
        window.title("AddressBook")

        Label(window, text = "Name").grid(row = 1, column = 1)
        Label(window, text = "Street").grid(row = 2, column = 1)
        Label(window, text = "City").grid(row = 3, column = 1)
        Label(window, text = "State").grid(row = 3, column = 3)
        Label(window, text = "ZIP").grid(row = 3, column = 5)

        self.name = StringVar()
        Entry(window, textvariable = self.name, justify = RIGHT).grid(row = 1, column = 2)
        self.street = StringVar()
        Entry(window, textvariable = self.street, justify = RIGHT).grid(row = 2, column = 2)
        self.city = StringVar()
        Entry(window, textvariable = self.city, justify = RIGHT).grid(row = 3, column = 2)
        self.state = StringVar()
        Entry(window, textvariable = self.state, justify = RIGHT).grid(row = 3, column = 4)
        self.zipCode = StringVar()
        Entry(window, textvariable = self.zipCode, justify = RIGHT).grid(row = 3, column = 6)

        Button(window, text = "Add", command = self.__addFromUserInterface).grid(row = 4, column = 2)
        Button(window, text = "First", command = self.__firstFromUserInterface).grid(row = 4, column = 3)
        Button(window, text = "Next", command = self.__nextFromUserInterface).grid(row = 4, column = 4)
        Button(window, text = "Previous", command = self.__previousFromUserInterface).grid(row = 4, column = 5)
        Button(window, text = "Last", command = self.__lastFromUserInterface).grid(row = 4, column = 6)
        window.mainloop()
    
    def __addFromUserInterface(self):
        self.__addressBook.add(self.name.get(), self.street.get(), self.city.get(), self.state.get(), self.zipCode.get())

    def __setAddressInUserInterface(self, address):
        if address:
            self.name.set(address.getName())
            self.street.set(address.getStreet())
            self.city.set(address.getCity())
            self.state.set(address.getState())
            self.zipCode.set(address.getZipCode())
        else:
            self.name.set("")
            self.street.set("")
            self.city.set("")
            self.state.set("")
            self.zipCode.set("")

    def __firstFromUserInterface(self):
        first = self.__addressBook.first()
        self.__setAddressInUserInterface(first)

    def __nextFromUserInterface(self):
        nextAddress = self.__addressBook.nextAddress()
        self.__setAddressInUserInterface(nextAddress)

    def __previousFromUserInterface(self):
        previous = self.__addressBook.previous()
        self.__setAddressInUserInterface(previous)

    def __lastFromUserInterface(self):
        last = self.__addressBook.last()
        self.__setAddressInUserInterface(last)

AddressBookUserInterface()
