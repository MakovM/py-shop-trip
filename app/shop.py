from dataclasses import dataclass
import datetime

from app.customer import Customers


@dataclass
class Shops:
    name: str
    location: list
    products: dict

    def get_bill(self, customer: Customers) -> None:
        date_today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_cost = 0

        print(
            f"Date: {date_today}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: ")

        for key, value in customer.product_cart.items():
            product_cost = value * self.products[key]

            if product_cost == int(product_cost):
                product_cost = int(product_cost)

            total_cost += product_cost
            print(f"{value} {key}s for {product_cost} dollars")

        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!\n")
