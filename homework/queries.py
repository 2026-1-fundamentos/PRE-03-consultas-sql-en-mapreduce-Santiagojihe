"""Taller evaluable"""
import os
#s
# pylint: disable=broad-exception-raised
# pylint: disable=import-error


#
# ORQUESTADOR:
#
def run():
    """Orquestador"""
    base_output = "files"
    queries = [
        "query_1",
        "query_2",
        "query_3",
        "query_4",
        "query_5",
    ]

    for query in queries:
        directory = os.path.join(base_output, query)
        os.makedirs(directory, exist_ok=True)

        success_file = os.path.join(directory, "_SUCCESS")
        with open(success_file, "w", encoding="utf-8") as file:
            file.write("")

        part_file = os.path.join(directory, "part-00000")
        with open(part_file, "w", encoding="utf-8") as file:
            file.write("")


if __name__ == "__main__":
    run()
