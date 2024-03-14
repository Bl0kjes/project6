import datetime
import math
 
class Evenement:
    def __init__(self, naam, datum, locatie, kosten_per_deelnemer):
        self.naam = naam
        self.datum = datum
        self.locatie = locatie
        self.deelnemers = []
        self.kosten_per_deelnemer = kosten_per_deelnemer
 
    def voeg_deelnemer_toe(self, deelnemer):
        self.deelnemers.append(deelnemer)
 
    def toon_deelnemers(self):
        for deelnemer in self.deelnemers:
            print(deelnemer)
 
    def totale_kosten(self):
        return len(self.deelnemers) * self.kosten_per_deelnemer
 
    def __iter__(self):
        return iter(self.deelnemers)
 
 
class Conferentie(Evenement):
    def __init__(self, naam, datum, locatie, spreker):
        super().__init__(naam, datum, locatie, kosten_per_deelnemer=100)
        self.spreker = spreker
 
 
class Workshop(Evenement):
    def __init__(self, naam, datum, locatie, docent):
        super().__init__(naam, datum, locatie, kosten_per_deelnemer=50)
        self.docent = docent
 
 
class SocialeBijeenkomst(Evenement):
    def __init__(self, naam, datum, locatie, activiteit):
        super().__init__(naam, datum, locatie, kosten_per_deelnemer=20)
        self.activiteit = activiteit
 
 
def main():
    evenementen = []
 
    conferentie = Conferentie("Python Conference", datetime.datetime(2023, 12, 31), "Amsterdam", "Guido van Rossum")
    workshop = Workshop("Python Workshop", datetime.datetime(2023, 12, 15), "Rotterdam", "John Doe")
    sociale_bijeenkomst = SocialeBijeenkomst("Python Meetup", datetime.datetime(2023, 12, 20), "Utrecht", "Networking")
 
    evenementen.extend([conferentie, workshop, sociale_bijeenkomst])
 
    while True:
        print("\nMenu:")
        print("1. Toon deelnemers aan een evenement")
        print("2. Toon totale kosten voor alle evenementen")
        print("3. Exit")
 
        keuze = input("Selecteer een optie: ")
 
        if keuze == "1":
            print("\nBeschikbare evenementen:")
            for i, evenement in enumerate(evenementen):
                print(f"{i + 1}. {evenement.naam}")
 
            evenement_index = int(input("Selecteer een evenement: ")) - 1
            evenement = evenementen[evenement_index]
 
            print(f"\nDeelnemers aan {evenement.naam}:")
            evenement.toon_deelnemers()
 
        elif keuze == "2":
            totale_kosten = sum(evenement.totale_kosten() for evenement in evenementen)
            print(f"\nTotale kosten voor alle evenementen: ${totale_kosten}")
 
        elif keuze == "3":
            print("Bedankt voor het gebruik van het programma!")
            break
 
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
 
 
if __name__ == "__main__":
    main()