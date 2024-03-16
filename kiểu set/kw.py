def euler_method(x_min, x_max, y0, num_steps):
    h = (x_max - x_min) / num_steps
    x_values = [x_min + i * h for i in range(num_steps + 1)]
    y_values = [y0]

    for i in range(num_steps):
        f = 2 * y_values[i] - x_values[i]**3
        y_next = y_values[i] + h * f
        y_values.append(y_next)

    return x_values, y_values

# Khoảng x và điểm khởi đầu
x_min = 0
x_max = 2
y0 = 1

# Số bước nhảy
num_steps = 1000

x_values, y_values = euler_method(x_min, x_max, y0, num_steps)

# In giá trị xấp xỉ tại điểm kết thúc khoảng
print("Approximated value at x_max:", y_values[-1])
