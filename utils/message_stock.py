def message_stock(num) -> str:
    stock_message = {0: "command", 1: "capture ", 2: "invert", 3: "gamma ",
                     4: "brightness ",
                     5: "contrast ", 6: "smooth ", 7: "sharpness ",
                     8: "averaging ", 9: "close"}
    return stock_message.get(num)

