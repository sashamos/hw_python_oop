import datetime as dt

class Calculator:
    def __init__(self, limit):
    #""""что делает каждый метод"""
        self.limit = limit
        self.records = []

    def add_record(self, record):
    #""""что делает каждый метод"""
        self.records.append(record)

    def get_today_stats(self):
    #""""что делает каждый метод"""
        today_stats = 0
        date_today = dt.date.today()
        for record in self.records:
            if date_today == record.date:
                today_stats += record.amount
        return today_stats

    def get_today_remained(self):
    #""""cчитает сколько осталось"""
        rest = self.limit - self.get_today_stats()
        return rest

    def get_week_stats(self):
    #""""что делает каждый метод"""
        week_stats = 0
        today_today = dt.datetime.today()
        delta = dt.timedelta(days=6)
        diff = today_today - delta.date()
        for record in self.records:
            if  diff <=  record.date <= today_today:
                week_stats += record.amount
        return week_stats

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
             self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class сash_сalculator(Calculator):
    USD_RATE = 71.46
    EURO_RATE = 82.76

    def get_today_cash_remained(self, currency):
        rest_curr = self.get_today_cash_remained
        if rest_curr == 0:
            return "Денег нет, держись"
        currencies = {'rub': (1,'руб'),
                 'eur': (EURO_RATE,'Euro'),
                 'usd': (USD_RATE,'USD'),
                }
        if currency not in currencies:
            return f"Такой нет {currency}"
        rate, name = currencies[currency]
        result_final = rest_curr * rate
        if result_final > 0:
            return f"На сегодня осталось {result_final:.2f} {name}"
        return f"Денег нет, держись: твой долг - {result_final:.2f} {name}"

class calories_calculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.get_today_remained
        if calories_remained > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал»"
        return "Хватит есть!"
