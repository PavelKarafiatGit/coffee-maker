from source_data import MENU
from source_data import resources

### Základní nastavení




### Funkce
def report(data):
    print(f"Voda: {data['water']}")
    print(f"Mléko: {data['milk']}")
    print(f"Káva: {data['coffee']}")

def coins():
    print("Prosím vložte mince 1, 2, 5, 10, 20, 50")
    kc1 = int(input("Kolik 1 Kč chcete vložit?: "))
    kc2 = int(input("Kolik 2 Kč chcete vložit?: ")) * 2
    kc5 = int(input("Kolik 5 Kč chcete vložit?: ")) * 5
    kc10 = int(input("Kolik 10 Kč chcete vložit?: ")) * 10
    kc20 = int(input("Kolik 20 Kč chcete vložit?: ")) * 20
    kc50 = int(input("Kolik 50 Kč chcete vložit?: ")) * 50
    suma = kc1 + kc2 + kc5 + kc10 + kc20 + kc50
    print(f"Celkem jste vložili?¨: {suma} Kč") 
    return suma



### Kód automatu
user_choice = input("Co si dáte? (espresso/latte/cappuccino): ")

if user_choice == "report":
    report(resources)

if user_choice == "espresso":
    sum = coins()
elif user_choice == "latte":
    sum = coins()
elif user_choice == "cappuccino":
    sum = coins()

