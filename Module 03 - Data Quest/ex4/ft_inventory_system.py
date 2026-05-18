import sys


def stock_data(arguments: list[str]) -> dict[str, int]:
    stock: dict[str, int] = {}
    for element in arguments[1:]:
        element = element.strip()
        if element.count(":") != 1:
            print(f"Error - invalid parameter '{element}'")
            continue
        key_name, value_str = element.split(":")
        if key_name in stock:
            print(f"Redundant item '{key_name}' - discarding")
            continue
        try:
            stock[key_name] = int(value_str)
        except ValueError:
            print(f"Quantity error for '{key_name}': "
                  f"invalid literal for int() with base 10: '{value_str}'")
    return stock


def evaluate_metrics(stock_dict: dict[str, int]) -> None:
    sum_total = sum(stock_dict.values())
    max_node = ""
    min_node = ""
    for name, amount in stock_dict.items():
        percentage = (amount / sum_total) * 100
        print(f"Item {name} represents {percentage:.1f}%")
        if not max_node:
            max_node = name
        elif amount > stock_dict[max_node]:
            max_node = name
        if not min_node:
            min_node = name
        elif amount < stock_dict[min_node]:
            min_node = name
    print(f"Item most abundant: {max_node} with quantity "
          f"{stock_dict[max_node]}")
    print(f"Item least abundant: {min_node} with quantity "
          f"{stock_dict[min_node]}")


def append_bonus_item(stock_dict: dict[str, int]) -> None:
    stock_dict.update({"magic_item": 1})
    print(f"Updated inventory: {stock_dict}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("Error: No argument provided!")
    else:
        new_stock = stock_data(sys.argv)
        if not new_stock:
            return
        print(f"Got inventory: {new_stock}")
        key_collection = list(new_stock.keys())
        print(f"Item list: {key_collection}")
        print(f"Total quantity of the {len(key_collection)} "
              f"items: {sum(new_stock.values())}")
        evaluate_metrics(new_stock)
        append_bonus_item(new_stock)


if __name__ == "__main__":
    main()
