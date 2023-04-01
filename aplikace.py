import os
from database import session, Insurance

starter = True
evidenc = []


class Aplikace:

    while starter:
        os.system("cls")
        print("----------------------------\nEvidence "
              "pojištěných\n----------------------------\n")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěnce")
        print("2 - Vymazat pojištěnce")
        print("3 - Vypsat všechny pojištěné")
        print("4 - Vyhledat pojištěného")
        print("5 - Konec")

        option = int(input("Zadejte číslo operace: "))
        print()

        if option == 1:
            name_input = input("Zadejte jméno: ")
            lastname_input = input("Zadejte příjmení: ")
            age_input = int(input("Zadejte věk: "))
            telephone_input = input("Zadejte telefoní číslo: ")
            session.add(Insurance(name=name_input, lastname=lastname_input,
                                  age=age_input, telephone=telephone_input))
            session.commit()
            print("\nData byla uložena.\n")

        if option == 2:
            print('Vyberte "ID" uživatele, kterého chcete vymazat:')
            all_insured = session.query(Insurance).all()
            for insured in all_insured:
                print(insured)

            item_to_delete = input("Vyberte položku k vymazání: ")
            insurance = session.query(Insurance).filter_by(id=item_to_delete).first()
            if insurance:
                session.delete(insurance)
                session.commit()
                print("Data byla odstraněna!")
            else:
                print("Toto ID nebylo nalezelo")
        if option == 3:
            all_insured = session.query(Insurance).all()
            for insured in all_insured:
                print(insured)
            print("\nToto jsou všichni evidovaní pojištěnci\n")

        if option == 4:
            name_input = input("Zadejte jméno hledaného pojištěnce: ")
            lastname_input = input("Zadejte příjmenení hledaného pojištěnce: ")
            wanted = session.query(Insurance). \
                filter(Insurance.name == name_input,
                       Insurance.lastname == lastname_input).all()
            if not wanted:
                wanted = "\nPojištěnec tohoto jména nebyl nalezen"
            print(f"\n{wanted}\n")

        if option == 5:
            starter = False
            print("děkujeme vám za využití aplikace a brzy nashledanou\n")

        input('Pokračjete libovolnou klávesou...')
        os.system("cls")