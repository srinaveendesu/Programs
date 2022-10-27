# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()

"""
Given a list of packages that need to be built and the dependencies foreach package, determine a valid order in which to build the packages

Eg:
0: 5
1: 0
2: 0
3: 1, 2
4: 3
5: None

output: 5, 0- 5, 1 - 05 ,2 05 , 3 - 1052 ,4- 31052
"""


def test_invalid():
    output = Packages('invalid_value')
    assert output == "Invalid"


def test_Nodependency():
    output = Packages(5)
    assert output == [5]


def test_dependency_1():
    output = Packages(0)
    assert output == [5, 0]


def test_dependency_2():
    output = Packages(1)
    assert output == [5, 0, 1]


def test_dependency_3():
    output = Packages(2)
    assert output == [5, 0, 2]


def test_dependency_4():
    output = Packages(3)
    assert output == [5, 0, 1, 2, 3]


def test_dependency_5():
    output = Packages(4)
    assert output == [5, 0, 1, 2, 3, 4]


d = {
    0: 5,
    1: 0,
    2: 0,
    3: [1, 2],
    4: 3,
    5: None
}


def dependency(m):
    lst = []
    while m is not None:
        if isinstance(m, int):
            m1 = d.get(m, -1000)
            lst.insert(0, m)
            m = m1
    return lst


# Note: Negative number corresponds to package does not exist
# Assumption 2: Packages dependency will be in correct order
def Packages1(pkg):
    m = d.get(pkg, -1000)
    lst = []
    if m is not None and isinstance(m, int) and m < 0:
        return 'Invalid'
    if m is None:
        lst.append(pkg)
        return lst
    lst.append(pkg)
    while m is not None:
        if isinstance(m, int):
            m1 = d.get(m, -1000)

            lst.insert(0, m)
            m = m1
        if isinstance(m, list):
            for p in m:
                m1 = d.get(p, -1000)
                if isinstance(m1, int):
                    k = dependency(p)
                    for element in k:
                        if element not in lst:
                            lst.insert(len(lst) - 1, element)
            m = None

    print(lst)
    return lst

def dependency_new(m):
    lst = []
    while m is not None:
        if isinstance(m, int):
            m1 = d.get(m, -1000)
            lst.insert(0, m)
            m = m1
    return lst


def Packages(pkg):
    m = d.get(pkg, -1000)
    lst = []
    if m is not None and isinstance(m, int) and m < 0:
        return 'Invalid'
    if m is None:
        lst.append(pkg)
        return lst
    #lst.append(pkg)

    while m is not None:
        n = len(lst)
        if isinstance(m, list):
            for ele in m:
                sub_lst = Packages(ele)
                for e in sub_lst:
                    if e not in lst:
                        lst.insert(len(lst) -n, e)
            m = None
            continue
        lst.insert(0, m)
        m = d.get(m, -1000)
    lst.append(pkg)
    #print(lst)
    return lst
test_invalid()
test_Nodependency()
test_dependency_1()
test_dependency_2()
test_dependency_3()
test_dependency_4()
test_dependency_5()
