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
tri_type(1, 2, 3)
tri_type(3, 2, 3)
tri_type(4, 4, 4)
