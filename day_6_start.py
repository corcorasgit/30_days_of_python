#!/usr/bin/env python3
import datetime
default_names = ["Justin", "John", "Emilee", "Jim", "Ron", "Sandra", "Veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """=======================================

Hi {name}!
Thank you for the purchase on {date}.
We hope you are exicted about using it. Just as a 
reminder the purcase to was ${total}
Have a great one !

Team CFE
"""

def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.datetime.today()
        text = "{today.month}/{today.day}/{today.year}".format(today=today)
        for name in names:
            new_amount = "%.2f" %(amounts[i])
            new_msg = unf_message.format(
                    name=name,
                    date=text,
                    total =new_amount
                    )
            i += 1
            print(new_msg)


make_messages(default_names, default_amounts)
