from typing import Optional


def load_data_from_file(filename: Optional[str] = "database.txt") -> list:
    """ Load data from file """
    result = []
    db_file = open(filename, "r")
    for record in db_file.readlines():
        # Split records by comma
        record = record.split(",")

        # Cast values to integers
        record[2] = int(record[2])
        record[3] = int(record[3])

        # Save record to result
        result.append(record)
    return result


def get_user_stats(data: list) -> dict:
    """ Generate list of users """
    result = {}
    for row in data:
        # If we already found user previously,
        # aggregate new values
        if row[0] in result:
            result[row[0]]["products_bought"] += row[2]
            result[row[0]]["total_price"] += row[3]
        else:
            # Otherwise set initial values
            result[row[0]] = {
                "products_bought": row[2],
                "total_price": row[3],
            }
    return result


def get_products_stats(data: list) -> dict:
    """ Generate list of products """
    result = {}
    for row in data:
        # If we already found product previously,
        # aggregate new values
        if row[1] in result:
            result[row[1]]["bought_count"] += row[2]
            result[row[1]]["total_price"] += row[3]
        else:
            # Otherwise set initial values
            result[row[1]] = {
                "bought_count": row[2],
                "total_price": row[3],
            }
    return result


def main():
    """
    Main program function to get user's input and return result
    """
    data = load_data_from_file()

    user_stats = get_user_stats(data)
    print("User stats: ", user_stats)

    product_stats = get_products_stats(data)
    print("Product stats: ", product_stats)


if __name__ == "__main__":
    main()