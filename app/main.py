import json
import os

from app.car import Car
from app.customer import Customers
from app.shop import Shops


def shop_trip() -> None:
    config_path = os.path.join(
        os.path.dirname(__file__), "..", "app", "config.json"
    )
    config_path = os.path.abspath(config_path)

    with open(config_path, "r") as config_file:
        data_from_json = json.load(config_file)
        fuel_price = data_from_json["FUEL_PRICE"]
        customers_data = data_from_json["customers"]
        shops_data = data_from_json["shops"]

        customers = []
        for data in customers_data:
            car = Car(
                brand=data["car"]["brand"],
                fuel_consumption=data["car"]["fuel_consumption"]
            )
            customer = Customers(
                name=data["name"],
                product_cart=data["product_cart"],
                location=data["location"],
                money=data["money"],
                car=car
            )
            customers.append(customer)

        shops = []
        for data in shops_data:
            shop = Shops(
                name=data["name"],
                location=data["location"],
                products=data["products"]
            )
            shops.append(shop)

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            best_shop, total_price = customer.chose_shop(shops, fuel_price)

            if best_shop:
                if total_price <= customer.money:
                    print(f"{customer.name} rides to {best_shop.name}\n")
                    best_shop.get_bill(customer)
                    print(f"{customer.name} rides home")
                    print(f"{customer.name} now has "
                          f"{customer.money - total_price} dollars\n")
                else:
                    print(f"{customer.name} doesn't "
                          f"have enough money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
