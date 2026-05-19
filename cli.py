import argparse
from rich import print

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import validate_order


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:

        validate_order(
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n[bold blue]Order Request Summary[/bold blue]")

        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        if args.price:
            print(f"Price: {args.price}")

        if args.type == "MARKET":

            response = place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )

        else:

            response = place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\n[bold green]Order Successful[/bold green]")

        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"\n[bold red]Error:[/bold red] {e}")


if __name__ == "__main__":
    main()