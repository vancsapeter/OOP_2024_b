import datetime
import random

from test.classes import *
from test.classes import BelfoldiJegyek, NemzetkoziJarat, BelfoldiJarat


def init_lt():
    _l1 = LegiTarsasag("Tesztelek")
    return _l1


def init_bf(_lt_name):
    _bf = [BelfoldiJarat(_lt_name, 123, "Budapest", 213),
           BelfoldiJarat(_lt_name, 250, "Pécs", 125)]
    return _bf


def init_nf(_lt_name):
    _nf = [NemzetkoziJarat(_lt_name, 234, "New York", 600)]
    return _nf


def init_bf_jegyek(input_bf, input_capacity):
    _bf_jegyek = []
    x: int
    y: int
    for x in range(len(input_bf)):
        temp = ""
        for y in range(input_capacity):
            temp = str(input_bf[x].get_number())
            # print(temp)
            _bf_jegyek.append(
                BelfoldiJegyek(input_bf[x].get_name(), input_bf[x].get_number(), input_bf[x].get_destination(),
                               input_bf[x].get_price(),
                               "Belfoldi", temp + "_" + str(y + x * 100), 1))
    return _bf_jegyek


def init_nf_jegyek(input_nf, input_capacity):
    _nf_jegyek = []
    x: int
    y: int
    for x in range(len(input_nf)):
        temp = ""
        for y in range(input_capacity):
            temp = str(input_nf[x].get_number())
            # print(temp)
            _nf_jegyek.append(
                NemzetkoziJegyek(input_nf[x].get_name(), input_nf[x].get_number(), input_nf[x].get_destination(),
                                 input_nf[x].get_price(),
                                 "Nemzetkozi", temp + "_" + str(y + 1000), 1))
    return _nf_jegyek


def booking_bf_jegyek(_bf_jegyek):
    x = 0

    while x < 4:
        temp1 = random.randrange(1, len(_bf_jegyek))

        if _bf_jegyek[temp1].get_available() == 1:
            _bf_jegyek[temp1].set_available(0)
            x += 1
        else:
            x = x

    return _bf_jegyek


def booking_nf_jegyek(_nf_jegyek):
    x = 0

    while x < 2:
        temp1 = random.randrange(1, len(_nf_jegyek))

        if _nf_jegyek[temp1].get_available() == 1:
            _nf_jegyek[temp1].set_available(0)
            x += 1
        else:
            x = x
    return _nf_jegyek


def menu():
    print("Kérem válasszon az alábbi menüpontokból\n")

    print("1 - Foglalás\n")
    print("2 - Foglalások megtekintése\n")
    print("3 - Foglalás törlése\n")
    print("0 - Kilépés\n")
    valasz = input("Választás:")
    return valasz


def print_booked_jegyek(_bf_jegyek, _nf_jegyek):
    for y in range(200):
        if _bf_jegyek[y].get_available() == 0:
            # print(_bf_jegyek[y].get_ticket_number(), _bf_jegyek[y].get_available())
            print(_bf_jegyek[y].get_name(), _bf_jegyek[y].get_number(), _bf_jegyek[y].get_destination(),
                  _bf_jegyek[y].get_price(), _bf_jegyek[y].get_tp(), _bf_jegyek[y].get_ticket_number(),
                  _bf_jegyek[y].get_available())
    for x in range(100):
        if _nf_jegyek[x].get_available() == 0:
            print(_nf_jegyek[x].get_name(), _nf_jegyek[x].get_number(), _nf_jegyek[x].get_destination(),
                  _nf_jegyek[x].get_price(), _nf_jegyek[x].get_tp(), _nf_jegyek[x].get_ticket_number(),
                  _nf_jegyek[x].get_available())


def date_validation(_date):
    point1 = _date.find(".")
    point2 = _date.find(".", 5)

    if len(_date) != 10:
        print("Nem megfelelő a formátum!")
        x = 0
    elif point1 != 4:
        print("Nem megfelelő a formátum!")
        x = 0
    elif point2 != 7:
        print("Nem megfelelő a formátum!")
        x = 0
    elif int(_date[5:7])>12 or int(_date[5:7])<1:
        print("Nem megfelelő a formátum!")
        x = 0
    elif int(_date[5:7])<1:
        print("Nem megfelelő a formátum!")
        x = 0
    elif int(_date[5:7])==2 and int(_date[8:10])>30:
        print("Hibás dátum!")
        x = 0
    elif int(_date[0:4]) % 4==0 and int(_date[5:7]) == 2  and int(_date[8:10])>29:
        print("Hibás dátum!")
        x = 0
    elif int(_date[0:4]) % 4>0 and int(_date[5:7]) == 2  and int(_date[8:10])>28:
        print("Hibás dátum!")
        x = 0
    elif int(_date[5:7]) not in [1,3,5,7,8,10,12] and int(_date[8:10])>30:
        print("Hibás dátum!")
        x = 0
    else:

        try:
            int(_date[0:4])
            int(_date[8:10])

            if int(_date[0:4]) < datetime.datetime.now().year:
                print("Kérem jövőbeni dátumot adjon meg!")
                x = 0
            elif int(_date[0:4]) == datetime.datetime.now().year and int(_date[5:7]) < datetime.datetime.now().month:
                print("Kérlek jövőbeni dátumot adj meg!")
                x = 0
            elif int(_date[5:7]) == datetime.datetime.now().month and int(_date[8:10]) < datetime.datetime.now().day:
                print("Kérlek jövőbeni dátumot adj meg!")
                x = 0
            else:
                x = 1
        except ValueError:
            print("Nem megfelelő formátum!")
            x = 0
    return x


def checking_ticketid(_beolvas2, _bf_jegyek, _nf_jegyek):
    for i in range(len(_bf_jegyek)):
        if _bf_jegyek[i].get_ticket_number() == _beolvas2:
            return 1
    for j in range(len(_nf_jegyek)):
        if _nf_jegyek[j].get_ticket_number() == _beolvas2:
            return 1
    return 0


def delete_bookedticket(_beolvas2, _bf_jegyek, _nf_jegyek):
    if len(_beolvas2) == 8:
        for i in range(len(_nf_jegyek)):
            if _nf_jegyek[i].get_ticket_number() == _beolvas2:
                _nf_jegyek[i].set_available(1)
        print("A" + _beolvas2 + " számú foglalása törlésre került!")
    else:
        for i in range(len(_bf_jegyek)):
            if _bf_jegyek[i].get_ticket_number() == _beolvas2:
                _bf_jegyek[i].set_available(1)
        print("A foglalása törlésre került. Száma:  " + _beolvas2)
    pass


def get_booked_bf_jegyek(_bf_jegyek):
    return_bf_jegyek = []
    for y in range(200):
        if _bf_jegyek[y].get_available() == 0:
            return_bf_jegyek.append(_bf_jegyek[y])
    return return_bf_jegyek


def get_booked_nf_jegyek(_nf_jegyek):
    return_nf_jegyek = []
    for y in range(100):
        if _nf_jegyek[y].get_available() == 0:
            return_nf_jegyek.append(_nf_jegyek[y])
    return return_nf_jegyek

def checking_flightnumber(_flightnumber,_bf,_nf):
    i = 0
    j = 0
    for i in range(len(_bf)):
        # print(_flightnumber, str(_bf[i].get_number()))
        if _flightnumber==str(_bf[i].get_number()): return 1
    for j in range(len(_nf)):
        # print(_flightnumber, str(_nf[j].get_number()))
        if _flightnumber==str(_nf[j].get_number()): return 1
    return 0

def checking_available_ticket(_flightnumber,_bf_jegyek,_nf_jegyek):
    for i in range(len(_bf_jegyek)):
        if _bf_jegyek[i].get_number()==_flightnumber and _bf_jegyek[i].get_available() == 1: return 1
    for i in range(len(_nf_jegyek)):
        if _nf_jegyek[i].get_number()==_flightnumber and _nf_jegyek[i].get_available() == 1: return 1
    return 0
def select_first_available_ticket(_flightnumber,_bf_jegyek,_nf_jegyek):
    for i in range(len(_bf_jegyek)):
        if str(_bf_jegyek[i].get_number())==_flightnumber and _bf_jegyek[i].get_available() == 1:
            return _bf_jegyek[i].get_ticket_number()
    for i in range(len(_nf_jegyek)):
        if str(_nf_jegyek[i].get_number())==_flightnumber and _nf_jegyek[i].get_available() == 1:
            return _nf_jegyek[i].get_ticket_number()
    return 0
def booking_ticket(_jegysorszam,_jegyek):
    for i in range(len(_jegyek)):
        if _jegyek[i].get_ticket_number() == _jegysorszam:
            _jegyek[i].set_available(0)
    return _jegyek