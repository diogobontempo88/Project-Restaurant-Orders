class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({"cliente": customer, "pedido": order, "dia": day})

    def get_most_ordered_dish_per_customer(self, customer):
        # último commit não passava no avaliador devido ao erro flake 8- c901
        # (function is too complex)
        # https://www.flake8rules.com/rules/C901.html
        # resolução em vez de usar um for com if usar uma
        # list comprehension com if (mais eficiente)
        ordered_dish = [
            base for base in self.orders if base["cliente"] == customer
        ]

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

    def get_never_ordered_per_customer(self, customer):
        total_meals = []
        for base in self.orders:
            total_meals.append(base["pedido"])

        customer_meals = []
        for base in self.orders:
            if base["cliente"] == customer:
                customer_meals.append(base["pedido"])

        return set(total_meals) - set(customer_meals)

    def get_days_never_visited_per_customer(self, customer):
        total_days = []
        for base in self.orders:
            total_days.append(base["dia"])

        customer_days = []
        for base in self.orders:
            if base["cliente"] == customer:
                customer_days.append(base["dia"])

        return set(total_days) - set(customer_days)

    def get_busiest_day(self):
        week = dict()

        most_frequent = self.orders[0]["dia"]

        for base in self.orders:
            if base["dia"] not in week:
                week[base["dia"]] = 1
            else:
                week[base["dia"]] += 1

            if week[base["dia"]] > week[most_frequent]:
                most_frequent = base["dia"]

        return most_frequent

    def get_least_busy_day(self):
        week = dict()

        less_frequent = self.orders[0]["dia"]

        for base in self.orders:
            if base["dia"] not in week:
                week[base["dia"]] = 1
            else:
                week[base["dia"]] += 1

            if week[base["dia"]] < week[less_frequent]:
                less_frequent = base["dia"]

        return less_frequent

