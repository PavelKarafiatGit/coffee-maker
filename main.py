from source_data import MENU
from source_data import resources

### Základní nastavení
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]



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

def calculate_change(user_sume_coins, price):
    refund = user_sume_coins - price
    if refund >= 0:
        print("Nápoj se připravuje")
        if refund > 0:
            print(f"Zde jsou peníze zpět: {refund} Kč")
    else:
        print(f"Nevhodili jste dostatek peněz. Ještě je potřeba vložit {price - user_sume_coins}")
    


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

