
class A:
    pass


class B(A):
    pass

class C(A):
    pass


if __name__ == "__main__":
    b = B()
    c = C()

    i = isinstance(b, A)
    print(i)

