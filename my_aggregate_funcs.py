import sqlite3
import add_data


class SumOfIncomes:
    """Aggregate functions for calculating the sum of incomes"""
    def __init__(self):
        """Initialize the attributes"""
        self.sum = 0

    def step(self, value):
        """Add a value to the container"""
        connection = sqlite3.connect('my_sqlite3.db')
        cursor = connection.cursor()

        cursor.execute('SELECT amount FROM costs_and_profits WHERE type == ?', ('income',))
        result = cursor.fetchall()

        if value in str(result):
            self.sum += int(value)
        connection.close()

    def finalize(self):
        """Return result"""
        return self.sum


class SumOfCosts:
    """Aggregate functions for calculating the sum of costs"""
    def __init__(self):
        """Initialize the attributes"""
        self.sum = 0

    def step(self, value):
        """Add a value to the container"""
        connection = sqlite3.connect('my_sqlite3.db')
        cursor = connection.cursor()

        cursor.execute('SELECT amount FROM costs_and_profits WHERE type == ?', ('cost',))
        result = cursor.fetchall()

        if value in str(result):
            self.sum += int(value)
        connection.close()

    def finalize(self):
        """Return result"""
        return self.sum


if __name__ == '__main__':
    add_data.display_all_data('my_sqlite3.db')
    conn = sqlite3.connect('my_sqlite3.db')

    conn.create_aggregate("sum_of_incomes", 1, SumOfIncomes)
    conn.create_aggregate("sum_of_costs", 1, SumOfCosts)
    c = conn.cursor()

    c.execute("SELECT sum_of_incomes(amount) FROM costs_and_profits")
    r = c.fetchall()
    print(r)

    c.execute("SELECT sum_of_costs(amount) FROM costs_and_profits")
    r = c.fetchall()
    print(r)
