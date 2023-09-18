# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2

print(f"Leek is " + str(leek_price) + " euro per kilo.")

order = "leek 4"

sum_total = int(order.find(" ", 0 , len(order))) * leek_price

print(sum_total)

broccoli_price = 2.34
broccoli_order = 1.6


print(str(broccoli_order) + "kg broccoli costs " + str(round(broccoli_price *  broccoli_order, 2)) + "e")