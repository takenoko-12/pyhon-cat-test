def test(file1,file2):
    with open('file1',mode='r',encofing='UTF-8')as fl1 ,open('file1',mode='r',encofing='UTF-8')as fl2:#複数のファイルを読み込む
        for line in fl2: 
            i = int(line.strip())
            i += 1 # 1を足すだけの処理
            data=fl2.read(str(i) + '\n')
            print(type(line))
            fl2.close(str()+'\n')
。
