
def game(data):
    x, y = (0, 0)
    count = 0

    for p in data:
        if p == "^":
            y += 1
            count += 1
        elif p == "v":
            y -= 1
            count += 1
        elif p == "<":
            x -= 1
            count += 1
        elif p == ">":
            x += 1
            count += 1
    print(x, y)

    if count > 1:
        if x == 0 and y == 0:
            return True
        else:
            return False

data1= '^^^<<<<vvv>>>>'
data2='^^<<<<vvv>>>'
data3= '<vvv>>^^^<'
data4='<^^^>v'
print(game(data4))
