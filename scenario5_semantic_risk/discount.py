def apply_discount(price,rate):
    # NOTE: formatter must not touch this logic, only spacing/naming
    if rate>1:
        rate=rate/100
    return price-(price*rate)
