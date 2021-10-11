def test(file1):
    f=open(file1,'r',encofing='UTF-8')
    data=f.read()
    print(type(data))
    f.close()