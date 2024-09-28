class LegiTarsasag:  # Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name


class Jarat(LegiTarsasag):  # Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).
    def __init__(self, name, number, destination, price):
        super().__init__(name)
        self.name = name
        self._number = number
        self._destination = destination
        self._price = price

    def get_number(self):
        return self._number

    def get_destination(self):
        return self._destination

    def get_price(self):
        return self._price


class BelfoldiJarat(Jarat):  # Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek
    def __init__(self, name, number, destination, price, tp="Nemzetkozi"):
        super().__init__(name, number, destination, price)

        self._name = name
        self._tipus = tp
        self._number = number
        self._destination = destination
        self._price = price

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_destination(self):
        return self._destination

    def get_price(self):
        return self._price

    def get_tipus(self):
        return self._tipus

    def set_name(self, name):
        self._name = name
        return self

    def set_number(self, number):
        self._number = number
        return self

    def set_destination(self, destination):
        self._destination = destination
        return self

    def set_price(self, price):
        self._price = price
        return self

    def set_tipus(self, tipus):
        self._tipus = tipus
        return self


class NemzetkoziJarat(Jarat):  # Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
    def __init__(self, name, number, destination, price, tp="Nemzetkozi"):
        super().__init__(name, number, destination, price)

        self._name=name
        self._tipus = tp
        self._number = number
        self._destination = destination
        self._price = price
    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_destination(self):
        return self._destination

    def get_price(self):
        return self._price
    def get_tipus(self):
        return self._tipus


    def set_name(self, name):
       self._name=name
       return self

    def set_number(self, number):
        self._number = number
        return self

    def set_destination(self, destination):
        self._destination = destination
        return self

    def set_price(self, price):
        self._price = price
        return self
    def set_tipus(self, tipus):
        self._tipus = tipus
        return self


class NemzetkoziJegyek(NemzetkoziJarat):  # A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.
    def __init__(self, name, number, destination, price, tp, ticket_number, available):
        super().__init__(name, number, destination, price, tp)
        self._available = available
        self._number = number
        self._ticket_number = ticket_number
        self._destination = destination
        self._price = price
        self._tp = tp

    def set_price(self, price):
        self._price = price
        return self

    def set_ticket_number(self, ticket_number):
        self._ticket_number = ticket_number
        return self

    def set_available(self, available):
        self._available = available
        return self
    def set_number(self, number):
        self._number = number
        return self

    def set_destination(self, destination):
        self._destination = destination
        return self
    def set_tp(self, tp):
        self._tp = tp
        return self


    def get_ticket_number(self):
        return self._ticket_number

    def get_available(self):
        return self._available
    def get_price(self):
        return self._price
    def get_name(self):
        return self._name
    def get_destination(self):
        return self._destination
    def get_number(self):
        return self._number
    def get_tp(self):
        return self._tp

# class NemzetkoziJegyfoglalas(NemzetkoziJegyek):
#     def __init__(self, name, number, destination, price, , tp, ticket_number, available):
#         super().__init__(name, number, destination, price, tp, ticket_number, available)

class BelfoldiJegyek(BelfoldiJarat):  # A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.
    def __init__(self, name, number, destination, price,tp, ticket_number, available):
        super().__init__(name, number, destination, price,tp)
        self._available = available
        self._number = number
        self._ticket_number = ticket_number
        self._destination = destination
        self._price = price
        self._tp = tp

    def set_price(self, price):
        self._price = price
        return self

    def set_ticket_number(self, ticket_number):
        self._ticket_number = ticket_number
        return self

    def set_available(self, available):
        self._available = available
        return self

    def set_number(self, number):
        self._number = number
        return self

    def set_destination(self, destination):
        self._destination = destination
        return self

    def set_tp(self, tp):
        self._tp = tp
        return self

    def get_ticket_number(self):
        return self._ticket_number

    def get_available(self):
        return self._available

    def get_price(self):
        return self._price

    def get_name(self):
        return self._name

    def get_destination(self):
        return self._destination

    def get_number(self):
        return self._number

    def get_tp(self):
        return self._tp


# class BelfoldiJegyfoglalas(BelfoldiJegyek):
#     def __init__(self, name, number, destination, price, NumOfPieces, tp, available):
#         super().__init__(name, number, destination, price, tp, NumOfPieces)

    # def get_number(self):
    #     return self._number
    #
    # def get_available(self):
    #     return self._available
    #
    # def set_available(self, available):
    #     self._available = available
    #     return self
