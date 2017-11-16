"""
list of g(x) functions:
0 - g(x) = ax^n+bx^(n-1)+...
"""
import math
import matplotlib.pyplot as plt

gx_label = ""
gx = 0
p_ = 3
eps = pow(10, -300)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

x_list =[10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86]
y_list=[0.1, 0.0714, 0.0556, 0.0455, 0.0385, 0.0333, 0.0294, 0.0263, 0.0238, 0.0217,
   0.02, 0.0185, 0.0172, 0.0161, 0.0152, 0.0143, 0.0135, 0.0128, 0.0122, 0.0116]


#def calc(x):
    #return 7 + 3 * math.log(x)


def calc_gx(x, arg, gx_):

    p = len(arg) - 1
    r = 0
    for i in range(len(arg)):
        r += arg[i] * pow(x, p)
        p -= 1

    return r


def create_empty_array(size):
    array = list()
    for i in range(size):
        array.append(0)
    return array


def data_input():
    c = 0
    while True:
        try:
            if 'x_list' in globals():
                print("a = ", x_list[0])
                print("b = ", x_list[len(x_list) - 1])
                a = x_list[0]
                b = x_list[len(x_list) - 1]
                c = 2
            if c == 0:
                a = float(input("a:"))
                c = c + 1
            if c == 1:
                b = float(input("b:"))
                if b == a:
                    print("Values cannot be equal.")
                else:
                    if b < a:
                        temp = a
                        a = b
                        b = temp
                    c = c + 1
            if c == 2:
                if 'x_list' in globals() or 'y_list' in globals():
                    if 'x_list' in globals():
                        n = len(x_list) - 1
                    else:
                        n = len(y_list) - 1
                    print("n= ", n)
                else:
                    n = int(input("n:"))
                if n <= 0:
                    print("n must be a positive integer.")
                else:
                    c = c + 1
            if c == 3:
                return [a, b, n]
        except ValueError:
            print("Incorrect input. Try again.")





def get_y(x):
    y = y_list()
    return y


'''def print_matrix(m, x):
    global alphabet
    print("\nMatrix:")
    for i in range(len(m)):
        print('{:^21}'.format(alphabet[i])," end=")
    print('{:^24}'.format("x"))
    for i in range(len(m)):
        for j in range(len(m)):
            print('{:<21}'.format(m[i][j]), "end= ")
        print('{:<3}'.format("="), '{:<21}'.format(x[i]))
'''

def coef(x, y, gx_):
    if gx_ == 0:
        r = m0(x, y)
    return r


def m0(x, y):
    global p_
    p = p_
    p_list = create_empty_array(2 * p + 1)
    x_vector = create_empty_array(p + 1)
    p2 = 2 * p
    for i in range(p2, -1, -1):
        for j in range(len(x)):
            p_list[i] += x[j] ** i
    for i in range(p, -1, -1):
        for j in range(len(x)):
            x_vector[i] += pow(x[j], i) * y[j]
    x_vector.reverse()
    matrix = list()
    cur_p = 2 * p
    for i in range(p + 1):
        m_row = list()
        itr = 0
        c_p = cur_p
        while itr < p + 1:
            m_row.append(p_list[c_p])
            itr += 1
            c_p -= 1
        matrix.append(m_row)
        cur_p -= 1
    #print_matrix(matrix, x_vector)
    res = [matrix, x_vector]
    return res


def m6_coefs(c):
    c[0] = math.exp(c[0])
    return c


def converge(xc, xp, n): #STOP OF THE METHOD jACOBI
    global eps
    norm = 0
    for i in range(n):
        norm += (xc[i] - xp[i]) * (xc[i] - xp[i])
    if math.sqrt(norm) >= eps:
        return False
    else:
        return True


def Jacobi(c):
    a = c[0]
    b = c[1]
    n = len(b)
    x = create_empty_array(n)
    px = create_empty_array(n)
    itr = 0
    while True:
        for i in range(n):
            px[i] = x[i]
        itr += 1
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += (a[i][j] * x[j])
            temp = ((b[i] - sum) / a[i][i])
            x[i] = temp
        if converge(x, px, n):
            break
    return x


def estimated_y(x, arg, gx_):
    y_est = list()
    for i in range(len(x)):
        value = calc_gx(x[i], arg, gx_)
        y_est.append(value)
    return y_est


def get_gx_label(x, d, gx_):
    if gx_ == 0:
        p = len(x) - 1
        r = "g(x) = "
        for i in range(len(x)):
            r += str(round(x[i], d))
            if p > 0:
                r += "x"
            if p > 1:
                r += "^" + str(p)
            if i != len(x) - 1:
                r += " + "
            p -= 1
    return r


def print_coef(x, gx_):
    global gx_label, alphabet
    print("\r")
    for i in range(len(x)):
        print(alphabet[i], "=", x[i])
    gx_label = get_gx_label(x, 5, gx_)
    print(get_gx_label(x, 100, gx_))



def chart_draw(x, y, gx_arg, gx_, gx_label_):
    g_x = list()
    g_y = list()
    step = 100
    for i in range(step * (len(x) - 1) + 1):
        g_x.append(round(x[0] + float((x[len(x) - 1] - x[0]) / (len(x) - 1)) * (i / step), 10))
    for dot in g_x:
        g_y.append(calc_gx(dot, gx_arg, gx_))
    func, = plt.plot(x, y, 'g-', label='f(x)')
    spl, = plt.plot(g_x, g_y, 'r-', label='Line 1')
    plt.legend([func, spl], ['f(x)', gx_label_])
    plt.plot(x, y, 'bo')
    plt.show()


def main():
    global x_list, y_list, gx
    x = x_list
    try:
        if 'y_list' not in globals():
            y = get_y(x)
        else:
            y = y_list
    except (ValueError, ZeroDivisionError) as e:
        print("Unable to calculate f(x).")
    if len(x) == len(y):
        try:
            c = coef(x, y, gx)
            coefs = Jacobi(c)
            if gx == 6:
                coefs = m6_coefs(coefs)
            y_est = estimated_y(x, coefs, gx)
            print_coef(coefs, gx)
            #print_result(x, y, y_est)
            chart_draw(x, y, coefs, gx, gx_label)
        except (ValueError, ZeroDivisionError) as e:
            print("Error occured with g(x).")
    else:
        print("x, y lists have different length. Unable to continue")


if __name__ == "__main__":
    main()