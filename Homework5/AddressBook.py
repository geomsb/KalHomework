from Address import Address

class AddressBook:
    def __init__(self):
        self.__addressBook = []
        self.__counter = -1

    def add(self, name, street, city, state, zipCode):
        a = Address(name, street, city, state, zipCode)
        self.__addressBook.append(a)
        self.__counter +=1

    def first(self):
        self.__counter = 0
        if len(self.__addressBook) > 0:
            return self.__addressBook[0]

    def nextAddress(self):
        if self.__counter == -1:
            return None
        if self.__counter >= len(self.__addressBook)-1:
            return self.__addressBook[self.__counter]
        else:
            self.__counter += 1
            return self.__addressBook[self.__counter]

    def previous(self):
        if self.__counter == -1:
            return None
        if self.__counter <= 0:
            return self.__addressBook[self.__counter]
        else:
            self.__counter -= 1
            return self.__addressBook[self.__counter]

    def last(self):
        self.__counter = len(self.__addressBook)-1
        if len(self.__addressBook) > 0:
            return self.__addressBook[-1]
