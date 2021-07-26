def three_args(*args,**kwargs):
    for key, value in kwargs.items():
        if value is not None:
            print(f"{key}={value}")

three_args(var1=2, var3=10)