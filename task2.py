import sqlite3


def add_data_to_db(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    while True:
        cursor.execute(
            "INSERT INTO costs_and_profits(purpose, amount, payment_date) VALUES (?, ?, ?)",
            ((input("Payment purpose: ")), (input("Payment amount: ")), (input("Payment date: ")))
        )
        choice = input("Add more?(y/n): ").strip().lower()
        if choice == "y":
            continue
        elif choice == "n":
            break
        else:
            print("Invalid input! Try again!")

    conn.commit()
    conn.close()


def display_all_data(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    result = cursor.execute("SELECT * FROM costs_and_profits").fetchall()
    for row in result:
        print(row)

    conn.close()


if __name__ == "__main__":
    add_data_to_db('my_sqlite3.db')
    display_all_data('my_sqlite3.db')
