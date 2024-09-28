import random
import sys
from time import sleep

from test.classes import *
from test.methods import init_lt, init_bf, init_bf_jegyek, init_nf, booking_bf_jegyek, init_nf_jegyek, \
    booking_nf_jegyek, print_booked_jegyek, checking_ticketid, get_booked_nf_jegyek, \
    get_booked_bf_jegyek, delete_bookedticket, menu, date_validation, checking_flightnumber, checking_available_ticket, \
    select_first_available_ticket, booking_ticket

# Inícializálás # egy légitársaság, 3 járat és 6 foglalás

l1 = init_lt()
lt_name = l1.get_name()
# járatok feltöltése
bf = init_bf(lt_name)
# print(bf[0].get_name(), bf[0].get_number, bf[0].get_destination, bf[0].get_price)
nf = init_nf(lt_name)
# jegy kapacitás/járat
capacity = 100
# Jegyek feltöltése
bf_jegyek = init_bf_jegyek(bf, capacity)
nf_jegyek = init_nf_jegyek(nf, capacity)

# Jegyek lefoglalása
bf_jegyek = booking_bf_jegyek(bf_jegyek)
nf_jegyek = booking_nf_jegyek(nf_jegyek)
tst = 0
while tst != 1:
    try:
        select = int(menu())
        match select:
           case 1:  # Foglalás
               # Dátum megadása
                chk = 0
                while chk != 1:
                    date = input("Kérem adja meg az indulás időpontját! (Elvárt formátum ÉÉÉÉ.HH.NN)\n")
                    # dátum ellenőrzés
                    if date_validation(date):
                        chk = 1

                # A járatok kiírása
                        chk2 = 0
                        while chk2 != 1:
                            print("Belföldi járatok:")

                            for i in range(len(bf)):
                                print("Légitársaság: " + bf[i].get_name() + " Járatszám: " + str(
                                    bf[i].get_number()) + " Célállomás: " + bf[i].get_destination() + " Ár: " + str(
                                    bf[i].get_price()) + "€\n")
                            print("Nemzetközi járatok:")

                            for j in range(len(nf)):
                                print("Légitársaság: " + nf[j].get_name() + " Járatszám: " + str(
                                    nf[j].get_number()) + " Célállomás: " + nf[j].get_destination() + " Ár: " + str(
                                    nf[j].get_price()) + "€\n")
                            # A kiírt járatokból választás
                            flightnumber = input("\nKérem adja meg a kívánt járat számát: ")

                            if checking_flightnumber(flightnumber, bf, nf) == 1:
                                # if checking_available_ticket(flightnumber, bf_jegyek, nf_jegyek)==1:
                                # A választott járathoz jegyszám hozzárendelés
                                jegysorszam = select_first_available_ticket(flightnumber, bf_jegyek, nf_jegyek)
                                print("\nA foglalás sikeres!\nAz ön jegyének a sorszáma: " + str(jegysorszam))
                                if len(str(jegysorszam)) != 8:
                                    bf_jegyek = booking_ticket(jegysorszam, bf_jegyek)
                                elif len(str(jegysorszam)) == 8:
                                    nf_jegyek = booking_ticket(jegysorszam, nf_jegyek)
                                chk2 = 1
                            else:
                                print("Kérem a megadott listából válasszon!\n")

                        # Ellenőrizni kell, hogy van-e elérhető jegy


           case 2:  # Foglalások megtekintése
                print_booked_jegyek(bf_jegyek, nf_jegyek)
           case 3:  # Foglalás törlése
                beolvas2 = input("Kérem adja meg a jegyének a számát! \n")
                if checking_ticketid(beolvas2, get_booked_bf_jegyek(bf_jegyek), get_booked_nf_jegyek(nf_jegyek)):
                    delete_bookedticket(beolvas2, bf_jegyek, nf_jegyek)
                else:
                    print("Nincs ilyen számú jegy!")
                # print_booked_jegyek(bf_jegyek, nf_jegyek)

           case 0:
                 print("Legyen szép napod!\n")
                 sleep(5)
                 sys.exit()
           case _:
                 print("Hibás válasz, a program kilép!\n")
                 sys.exit()

    except ValueError:
        "1Kérem csak a megadott menüpontokból válasszon!"
    sleep(5)

# Foglalások kiírása
# print_booked_jegyek(bf_jegyek, nf_jegyek)

# Foglalás törlése
# print_booked_jegyek(bf_jegyek, nf_jegyek)
# beolvas2 = input("Kérem adja meg a jegyének a számát! \n")
# if checking_ticketid(beolvas2, get_booked_bf_jegyek(bf_jegyek), get_booked_nf_jegyek(nf_jegyek)):
#     delete_bookedticket(beolvas2, bf_jegyek, nf_jegyek)
# else:
#     print("Nincs ilyen számú jegy!")
# print_booked_jegyek(bf_jegyek, nf_jegyek)
# #
#


# for y in range(200):
#     print(bf_jegyek[y].get_ticket_number(), bf_jegyek[y].get_available())

#
#
# for yy in range(100):
#      if nf_jegyek[yy].get_available()==0:
#         print(nf_jegyek[yy].get_ticket_number(),nf_jegyek[yy].get_available())

# print(bf[0].get_price())
#
# print(nf[0].get_destination())

# Jegy foglalása
# Kérje be az indulási időpontot és a célállomást

#
# x = 0
# while x != 1:
#
#     beolvas1 = input("Kérem adja meg az indulás időpontját! (Elvárt formátum ÉÉÉÉ.HH.NN)\n")
#     if date_validation(beolvas1)==1:
#         print("OK")
#         x=1


# Foglalás lemondása
# Foglalások listázása
sys.exit()
