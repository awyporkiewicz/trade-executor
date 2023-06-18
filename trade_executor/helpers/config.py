from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-q", "--quantity", type=float, required=True)
parser.add_argument("-p", "--price", type=float, required=True)
parser.add_argument(
    "-s",
    "--symbol",
    type=str,
    default="bnbusdt",
    choices=["bnbusdt", "ethusdt", "btcusdt", "ethbtc"],
)
parser.add_argument("-e", "--exchange", type=str, default="bid", choices=["bid", "ask"])
args = parser.parse_args()
