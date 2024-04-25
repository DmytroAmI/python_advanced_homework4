import sqlite3
import add_data


def update_data(db, table_name, set_field, field_name, new_value, field_value):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE ' + table_name + ' SET ' + set_field + ' = ? WHERE ' + field_name + ' = ?',
        (new_value, field_value)
    )
    conn.commit()
    conn.close()


if __name__ == '__main__':
    update_data('my_sqlite3.db', 'costs_and_profits', 'type', 'id', 'cost', 1)
    update_data('my_sqlite3.db', 'costs_and_profits', 'type', 'id', 'income', 2)
    update_data('my_sqlite3.db', 'costs_and_profits', 'type', 'id', 'income', 3)

    add_data.display_all_data('my_sqlite3.db')
