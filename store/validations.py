def check_out_of_stock(product, qty):
    if product.quantity < 1 :
        return "I'm sorry but we are out of stock for {}".format(product.name)
    elif product.quantity < int(qty):
        return "I'm sorry but we only have {}KG of {} left".format(product.quantity, product.name)
    return False