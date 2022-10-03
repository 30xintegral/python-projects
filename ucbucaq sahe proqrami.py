import math


def sahe_heron(teref1, teref2, teref3):
    if (teref1+teref2>teref3 or teref2+teref3>teref1 or teref1+teref3>teref2):
        half_sum = (teref1+teref2+teref3)/2


        area = float(math.sqrt((half_sum*(half_sum - teref1)*(half_sum - teref2)*(half_sum - teref3))))
        return area
    else:
        return 0

def sahe_hundurluk(teref1, teref2, teref3, alpha, betta, h):
    if (h==""):
        h = teref1 * (math.sin(math.radians(alpha)))
        h = teref2 * (math.sin(math.radians(betta)))
        h = teref3 * (math.sin(math.radians(gamma)))
        area = float( 0.5 * teref3 * h)
        return area
    else:
        area = float( 0.5 * teref3 * h)
        return area

def sahe_bucaq(teref1, teref2, teref3, alpha, betta, gamma):
    area = float(0.5 * teref1 * teref3 * (math.sin(math.radians(alpha)))) or  float(0.5 * teref2 * teref3 * (math.sin(math.radians(betta)))) or float(0.5 *teref1 * teref2 * (math.sin(math.radians(gamma))))
    
    return area



teref1 = int(input("teref yan sol ?= "))
teref2 = int(input("teref yan sag ?= "))
teref3 = int(input("teref oturacaq ?= "))


response = input("bucaqlar verilib? he/yox ")
if response == "he":
    alpha = int(input("yan teref1 ile oturacaq arasindaki bucaq alpha ?= "))
    betta = int(input("yan teref1 ile yan teref2 arasindaki bucaq betta ?= "))
    gamma = int(input("yan teref2 ile oturacaq arasindaki bucaq gamma ?= "))
    h_clone = input("hundurluk ?= ")
    if h_clone == "" :
        print("hundurluk verilmeyib")
    else:
        print("hundurluk = ",h_clone)
    
    cavab_1 = float(sahe_heron(teref1, teref2, teref3))
    print("ucbucagin heronla sahesi =", cavab_1)
    cavab_2 = float(sahe_hundurluk(teref1, teref2, teref3, alpha, betta, h=h_clone))
    print("ucbucagin 1/2 a h ile sahesi =", cavab_2)
    cavab_3 = sahe_bucaq(teref1, teref2, teref3, alpha, betta, gamma)
    print("ucbucagin 1/2 a b sin(alfa) ile sahesi =", cavab_3)



else:
    print("bucaqlar verilmeyib")

    h_clone = input("hundurluk ?= ")
    if h_clone == "" :
        print("hundurluk verilmeyib")
    else:
        print("hundurluk = ",h_clone)
    cavab_1 = float(sahe_heron(teref1, teref2, teref3))
print("ucbucagin heronla sahesi =", cavab_1)



