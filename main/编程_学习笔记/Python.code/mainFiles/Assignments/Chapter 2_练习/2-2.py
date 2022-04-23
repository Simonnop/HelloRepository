for i in range(1,3000,50):
    for j in range(0,60):
        if -200<j**2-i<0:
            for k in range(0,2000000):
                if -0.005<j**2-i<0.005:
                    print('the square of {:.2f} is {}'.format(j,i))
                    break
                j+=0.000005
            break



