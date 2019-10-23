
def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print (item)
                else:
                    print ('No Match')
            else:
                print ('Not a string')
    except GeneratorExit:
        print (count)


c = counter('california')

# using next() -> this is called priming a co-routine
next(c)

c.send('cali')
c.send('nia')
c.send('for')
c.send('delhi')
c.send(1234)
c.close()


# cali
# nia
# for
# No Match
# Not a string
# 3
