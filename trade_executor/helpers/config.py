from argparse import ArgumentParser

schema_path, db_file = (
    "../data/schema.sql",
    "../data/trade.sqlite3",
)

parser = ArgumentParser()
parser.add_argument("-q", "--quantity", type=float, required=True)
parser.add_argument("-p", "--price", type=float, required=True)

args = parser.parse_args()
