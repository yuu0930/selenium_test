scores = [100, 90, 80, 70, 60] # リスト

for x in scores:               # 繰り返し処理、xにscoresリストの要素が１つずつ代入されprintされる
    print(x)

for x in scores:
    print(x + 1)               # リストの要素をxに１つずつ代入、ｘに+1してプリントする
    
    
"""for 変数1, 変数2 in 辞書.items():"""               # 辞書の場合のfor文、変数1に辞書のkeyを、変数2に辞書のvalueを代入する
"""繰り返ししたい処理"""
fruits = {"りんご": 200, "みかん": 150, "バナナ": 100} # 辞書
for name, price in fruits.items():                   # 辞書のうち、keyを１つずつ取り出す
    print(name)

for name, price in fruits.items():                   # 辞書のうち、valueを１つずつ取り出す
    print(price)

for name, price in fruits.items():                   # 辞書のkey,valueを同時に１つずつ取り出す
    print(f"{name}は{price}円です")