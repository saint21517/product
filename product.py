product = []
while True:
    name = input('請輸入商品名: ')
    if name == 'q':
    	break
    price = input('請輸入價格: ')	
    product.append([name, price])	
print(product)    	