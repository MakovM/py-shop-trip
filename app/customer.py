from dataclasses import dataclass
from math import dist

from app.car import Car


@dataclass()
class Customers:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: list[Car]

    def fuel_cost(self, shop_location: list, fuel_price: float) -> float:
        distance = dist(self.location, shop_location)
        fuel_needed = (distance / 100) * self.car.fuel_consumption
        fuel_cost = fuel_price * fuel_needed

        return fuel_cost

    def chose_shop(self, shops: list, fuel_price: float) -> float | list:
        best_shop = None
        lower_price = float("inf")

        for shop in shops:
            if not all(
                    product in shop.products
                    for product in self.product_cart
            ):
                continue
            fuel_cost = self.fuel_cost(shop.location, fuel_price)
            product_cost = sum(
                (cost * count) for product, cost in shop.products.items()
                for name, count in self.product_cart.items() if product == name
            )
            total_cost = round((product_cost + (fuel_cost * 2)), 2)
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")

            if total_cost < lower_price:
                best_shop = shop
                lower_price = total_cost

        return best_shop, lower_price
