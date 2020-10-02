import datetime


def main() -> None:
    today = datetime.date.today()

    if today.strftime("%A") == "Friday":
        print("Pizza Day!")
    else:
        print(":(")


if __name__ == "__main__":
    main()
