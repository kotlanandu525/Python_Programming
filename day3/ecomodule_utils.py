def apply_discount(price,dpercent):
    return (dpercent*price)/100
def add_gst(price,gstp=18):
    gstamt=(gstp*price)/100
    return price+gstamt
def generate_invoice(cart,dpercent=0,gstp=18):
    print("---invoice---")
    for k,v in cart.items():
        print(k,v)
    subtotal=sum(cart.values())
    afterdis=apply_discount(subtotal,dpercent)
    discount=subtotal-afterdis
    print("after",dpercent,"discount=", subtotal-afterdis)
    aftergst=add_gst(discount,gstp)
    print("after",gstp,"GST=",aftergst)
    print("thank youn for shopping")

 