import random
import sys
from time import sleep

from pythonProject.test.classes import *
from pythonProject.test.methods import init_lt, init_bf, init_bf_jegyek, init_nf, booking_bf_jegyek, init_nf_jegyek, \
    booking_nf_jegyek, print_booked_jegyek, checking_ticketid, get_booked_nf_jegyek, \
    get_booked_bf_jegyek, delete_bookedticket, menu, date_validation, checking_flightnumber, checking_available_ticket, \
    select_first_available_ticket, booking_ticket

# Inícializálás # egy légitársaság, 3 járat és 6 foglalás

l1 = init_lt()
lt_name = l1.get_name()
# járatok feltöltése
bf = init_bf(lt_name)
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
                           print_flight(bf, nf)
                           flightnumber = input("\nKérem adja meg a kívánt járat számát: ")

                           if checking_flightnumber(flightnumber, bf, nf) == 1:
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
                retry=0
                retry1=0
                while retry !=1:
                    beolvas2 = input("Kérem adja meg a jegyének a számát! \n")
                    if checking_ticketid(beolvas2, get_booked_bf_jegyek(bf_jegyek), get_booked_nf_jegyek(nf_jegyek)):
                        delete_bookedticket(beolvas2, bf_jegyek, nf_jegyek)
                        retry=1
                    else:
                        print("Nincs ilyen számú jegy!")
                        retry = 0
                        retry1=retry1+1
                        if retry1 == 5:
                            print("Túl sok hibás válasz miatt a program kilép!")
                            sys.exit()
                # print_booked_jegyek(bf_jegyek, nf_jegyek)

           case 0:
                 print("Legyen szép napod!\n")
                 sleep(5)
                 sys.exit()
           case _:
                 print("Hibás válasz, a program kilép!\n")
                 sys.exit()

    except ValueError:
        "Kérem csak a megadott menüpontokból válasszon!"
    sleep(5)
sys.exit()
