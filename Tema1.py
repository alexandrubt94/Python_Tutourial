a1 = input()
b2 = input()
c3 = input()


def tri_type(a, b, c):
    if (a + b) <= c or (a + c) <= b or (c + b) <= a:
        print 'invalid'
    else:
        if  (a != b) and  (b != c) and (c != a):
            print("triunghi oarecare")
        else:
            if (a == b) and (b == c):
                print("triunghi echilateral")
            else:
                    print("triunghi isoscel")
tri_type(a1, b2, c3)
