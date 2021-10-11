import sys
import fileinput
from pathlib import Path

#引数をファイル名かstdinから読み込む
if Path(sys.argv[1]).exists():#第一引数がファイルだったら
    print('file input')#ファイルの内容を1行ずつprint
    print(line)
else:#第一引数がファイルではなかったら
    for i in sys.argv[1:]:
        print('args input')#引数の文字列をprint
        print(i)