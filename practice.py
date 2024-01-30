def is_plural(bottles):
    if bottles == 1:
        print('bottle')
    else:
        print('bottles')
       



def ninety_nine(bottles):
    bottles = 99
    while bottles <= 1:
        print(f'{bottles} {is_plural(bottles)} of beer on the wall {bottles} of beer, take one down pass it around {bottles-1}{is_plural(bottles)} of beer on the wall')
        bottles -= 1

ninety_nine(100)