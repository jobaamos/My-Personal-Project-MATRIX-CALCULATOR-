print("JOBA'S MATRIX CALCULATOR")
print('Which part of the calculator do you want to use? \n (1) Normal Calculator \n (2) Matrix')
req = input('1/2? \n ', )
if req == ('1'):
    print('Do you want to use the normal calculator?')
    users_input = input('yes/no: ').lower()
    if users_input == ('no'):
        print('Goodbye')
    elif users_input == ('yes'):
        while True:
            def add(x,y):
                return x + y
            def subtract(x,y):
                return x - y
            def multiply(x,y):
                return x * y
            def divide(x,y):
                return x / y

            print("select operation.")
            print("1.add")
            print("2.subtract")
            print("3.multiply")
            print("4.divide")

            choice = input("Enter choice(1/2/3/4): ")
            try:
                num1 = eval(input("Enter number: "))
                num2 = eval(input("Enter number: "))
            except:
                print('Inavalid input')

            try:
                if choice == '1':
                     print(num1,'+',num2,'=', add(num1,num2))
                elif choice == '2':
                     print(num1,'-',num2,'=', subtract(num1,num2))
                elif choice == '3':
                     print(num1,'*',num2,'=', multiply(num1,num2))
                elif choice == '4':
                     print(num1,'/',num2,'=', divide(num1,num2))
            except:
                print('invalid input')
            print('DO you still want to use the calculator? ')
            ans = input('Yes/No? ').lower()
            if ans == ('yes'):
                pass
            elif ans == ('no'):
                exit()
            else:
                exit()
elif req == ('2'):
    print('What order of matrix do you want to use? \n(1) 2*2 \n(2) 3*3')
    opq = input('1/2? ',)
    if opq == ('1'):
        while True:
            while True:
                print('what part of the 2*2 matrix do you want to use? \n (1)Determinant \n (2)Transpose \n (3)Other')
                pri = input('1/2/3 ',)
                if pri == ('1'):
                    print('a | b \n-----\nc | d')                
                    a = eval(input('a is ', ))
                    b = eval(input('b is ', ))
                    c = eval(input('c is ', ))
                    d = eval(input('d is ', ))
                    print('The determinant is', a*d+b*c)
                elif pri == ('2'):
                    print('a | b \n-----\nc | d')
                    a = eval(input('a is ', ))
                    b = eval(input('b is ', ))
                    c = eval(input('c is ', ))
                    d = eval(input('d is ', ))
                    print('The transpose is: ')
                    print(a ,'|', c)
                    print('-----')
                    print(b ,'|', d)
                elif pri == ('3'):
                    print('Do you want to use other calculation methods? ')
                    ads = input('Yes/No ', )
                    if ads == ('yes'):
                        break
                    elif ads == ('no'):
                        pass
                else:
                    print('invalid input')
            print('first matrix\na | b \n-----\nc | d\nsecond matrix\ne | f \n-----\ng | h')
            a = eval(input('a is ', ))
            b = eval(input('b is ', ))
            c = eval(input('c is ', ))
            d = eval(input('d is ', ))
            e = eval(input('e is ', ))
            f = eval(input('f is ', ))
            g = eval(input('g is ', ))
            h = eval(input('h is ', ))
            print('What operation do you  want to perform? \n(1) Addition \n(2) Subtraction \n(3) Multiplication ')
            awe = input('1,2,3? ')
            if awe == ('1'):
                print(a+e,'|', b+f)
                print('-----')
                print(c+g,'|', d+h)
            elif awe == ('2'):
                print(a-e,'|', b-f)
                print('-----')
                print(c-g,'|', d-h)
            elif awe == ('3'):
                print((a*e)+(b*g),'|', (a*f)+(b*h))
                print('-----')
                print((c*e)+(d*g),'|', (c*f)+(d*h))
            print('Do you still want to use the calculator?')
            sda = input('Yes/No? ').lower()
            if sda == ('yes'):
                pass
            elif sda == ('no'):
                exit()
    elif opq == ('2'):
        while True:
            while True:
                print('what part of the 3*3 matrix do you want to use? \n (1) Determinant \n (2) Transpose \n (3) Other')
                ind = input('1/2/3 ',)
                if ind == ('1'):
                    print("a | b | c \n---------\nd | e | f \n---------\ng | h | i")
                    a = eval(input('a is ', ))
                    b = eval(input('b is ', ))
                    c = eval(input('c is ', ))
                    d = eval(input('d is ', ))
                    e = eval(input('e is ', ))
                    f = eval(input('f is ', ))
                    g = eval(input('g is ', ))
                    h = eval(input('h is ', ))
                    i = eval(input('i is ', ))
                    j = ((+a)*((e*i)-(h*f)))
                    k = ((-b)*((d*i)-(g*f)))
                    l = ((+c)*((d*h)-(g*e)))
                    print('The answer is', j+k+l)
                elif ind == ('2'):
                    print("a | b | c \n---------\nd | e | f \n---------\ng | h | i")
                    a = eval(input('a is ', ))
                    b = eval(input('b is ', ))
                    c = eval(input('c is ', ))
                    d = eval(input('d is ', ))
                    e = eval(input('e is ', ))
                    f = eval(input('f is ', ))
                    g = eval(input('g is ', ))
                    h = eval(input('h is ', ))
                    i = eval(input('i is ', ))
                    print('The tanspose is: ')
                    print(a,'|', d,'|', g)
                    print('---------')
                    print(b,'|', e,'|', h)
                    print('---------')
                    print(c,'|', f,'|', i)
                elif ind == ('3'):
                    print('Do you want to use other calculation methods? ')
                    dfg = input('Yes/No ', )
                    if dfg == ('yes'):
                        break
                    elif dfg == ('no'):
                        pass
                else:
                    print('Invalid input')
            print('First matrix\na | b | c \n---------\nd | e | f \n---------\ng | h | i\nSecond matrix \nj | k | l \n---------\nm | n | o \n---------\np | q | r')
            print('For the first table')
            a = eval(input('a is ', ))
            b = eval(input('b is ', ))
            c = eval(input('c is ', ))
            d = eval(input('d is ', ))
            e = eval(input('e is ', ))
            f = eval(input('f is ', ))
            g = eval(input('g is ', ))
            h = eval(input('h is ', ))
            i = eval(input('i is ', ))
            print('For the second table')
            j = eval(input('j is ', ))
            k = eval(input('k is ', ))
            l = eval(input('l is ', ))
            m = eval(input('m is ', ))
            n = eval(input('n is ', ))
            o = eval(input('o is ', ))
            p = eval(input('p is ', ))
            q = eval(input('q is ', ))
            r = eval(input('r is ', ))
            print('What operation do you want to perform? \n(1) Addition \n(2) Subtraction \n(3) Multiplication')
            dsa = input('1/2/3? ')
            if dsa == ('1'):
                print(a+j,'|', b+k,'|', c+l)
                print(d+m,'|', e+n,'|', f+o)
                print(g+p,'|', h+q,'|', i+r)
            elif dsa == ('2'):
                print(a-j,'|', b-k,'|', c-l)
                print(d-m,'|', e-n,'|', f-o)
                print(g-p,'|', h-q,'|', i-r)
            elif dsa == ('3'):
                print(a*j+b*m+c*p,'|', a*k+b*n+c*q,'|', a*l+b*o+c*r)
                print(d*j+e*m+f*p,'|', d*k+e*n+f*q,'|', d*l+e*o+f*r)
                print(g*j+h*m+i*p,'|', g*k+h*n+i*q,'|', g*l+h*o+i*r)
            print('Do you still want to use the calculator?')
            sda = input('Yes/No? ').lower()
            if sda == ('yes'):
                pass
            elif sda == ('no'):
                exit()


    
