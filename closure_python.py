def make_multiplier_of(x):
    def multiply(y):
        return y * x
    return multiply

if __name__ == "__main__":
    multiplier_3 = make_multiplier_of(3)
    print(multiplier_3(5))