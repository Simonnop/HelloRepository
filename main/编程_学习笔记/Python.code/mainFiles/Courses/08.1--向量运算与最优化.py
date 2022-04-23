# 求微分 其中 f是一个函数
from linear_algebra import dot, add, scalar_multiply


def difference_quotient(f,x,h):
    return ((f(x+h)-f(x))/h)


# 推广多元函数求偏导
def partial_difference_quotient(f,v,i,h):
    w=[v_j + (h if j == i else 0)
    for j,v_j in enumerate(v)]
    return (f(w)-f(v))/h

def estimate_gradient(f,v,h=0.0001):
    return [partial_difference_quotient(f,v,i,h) 
    for i in range (len(v))]

# 梯度下降法
def gradient_step(v,gradient,step_size):
    # 参数: 步长,梯度
    step=scalar_multiply(step_size,gradient)
    return add(v,step)