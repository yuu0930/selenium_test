"""関数定義"""
def print_hello():         # 関数名は一見して分かる名前にする,():を最後につける
    print("こんにちは")     # 関数の処理を記述する
    
print_hello()              # 関数呼び出し,関数名(),関数定義は関数呼び出しよりも前に書く


"""関数定義（引数あり、位置引数（順序によって決定））"""
def add_sub_numbers(a, b):
    c = a + b
    d = b - a
    return c, d            # 戻り値＝関数が返す値
  
x, y = add_sub_numbers(10, 100) # 引数aに10、引数bに100が渡される、戻り値を変数x, yに代入する
print(x, y)

"""関数定義（引数あり、キーワード引数）"""
def add_sub_numbers2(a, b):
    c = a + b
    d = a - b
    return c, d
  
x = add_sub_numbers2(b=10, a=100) # 引数は順序によって決定せず、指定した値が指定した引数に渡される
print(x)                          # 戻り値が複数ある要素を1つの変数に代入する場合、戻り値はタプルとして返される