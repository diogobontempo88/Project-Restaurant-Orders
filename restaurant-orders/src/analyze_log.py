import os
import csv

fields = ["cliente", "pedido", "dia"]


def read(path_to_file):
    with open(path_to_file, encoding="utf-8") as file:
        lista = []
        list_reader = csv.DictReader(file, fieldnames=fields, delimiter=",")
        for order in list_reader:
            lista.append(order)
    return lista


def most_ordered_dish_per_customer(orders, customer):
    # último commit não passava no avaliador devido ao erro flake 8- c901
    # (function is too complex)
    # https://www.flake8rules.com/rules/C901.html
    # resolução em vez de usar um for com if usar uma
    # list comprehension com if (mais eficiente)
    ordered_dish = [base for base in orders if base["cliente"] == customer]

    dish = dict()

    most_ordered = ordered_dish[0]["pedido"]

    for client_data in ordered_dish:
        if client_data["pedido"] not in dish:
            dish[client_data["pedido"]] = 1
        else:
            dish[client_data["pedido"]] += 1

        if dish[client_data["pedido"]] > dish[most_ordered]:
            most_ordered = client_data["pedido"]

    return most_ordered


def quantity_of_meal_were_order_by_customer(orders, customer, value):
    ordered_dish = []
    for base in orders:
        if base["cliente"] == customer:
            ordered_dish.append(base)

    dish = dict()

    for client_data in ordered_dish:

        if client_data["pedido"] not in dish:
            dish[client_data["pedido"]] = 1
        else:
            dish[client_data["pedido"]] += 1

    get_value = dish.get(value, "Não encontrado")

    return get_value


def never_ordered_dish_per_customer(orders, customer):
    total_meals = []
    for base in orders:
        total_meals.append(base["pedido"])

    customer_meals = []
    for base in orders:
        if base["cliente"] == customer:
            customer_meals.append(base["pedido"])

    set_total = set(total_meals)
    set_customer = set(customer_meals)

    return set_total - set_customer


def never_visited_days_per_customer(orders, customer):
    total_meals = []
    for base in orders:
        total_meals.append(base["dia"])

    customer_meals = []
    for base in orders:
        if base["cliente"] == customer:
            customer_meals.append(base["dia"])

    set_total = set(total_meals)
    set_customer = set(customer_meals)

    return set_total - set_customer


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):

        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    if not os.path.isfile(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    else:
        text = read(path_to_file)

        orders_by_customer = most_ordered_dish_per_customer(text, "maria")
        order_quantity_by_customer = quantity_of_meal_were_order_by_customer(
            text, "arnaldo", "hamburguer"
        )
        never_ordered_by_customer = never_ordered_dish_per_customer(
            text, "joao"
        )
        never_visited_by_customer = never_visited_days_per_customer(
            text, "joao"
        )

        with open("data/mkt_campaign.txt", "w", encoding="utf-8") as file:
            file.write(
                f"{orders_by_customer}\n"
                f"{order_quantity_by_customer}\n"
                f"{never_ordered_by_customer}\n"
                f"{never_visited_by_customer}"
            )
