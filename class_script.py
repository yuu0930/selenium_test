"""クラスの作成"""
class User:                                          # クラス名は先頭の文字だけを大文字
    def __init__(self, name, mail_address, point):   # イニシャライザ,第一引数はselfとする
        self.name = name                             # self.変数名＝インスタンス変数
        self.mail_address = mail_address             # 引数で受け取った値をインスタンス変数に代入する
        self.point = point                           # selfはクラス定義のメソッドの中でだけ使える
        
    def add_point(self, point):                      # 第一引数はself selfは特殊な引数でオブジェクト自身のこと
        self.point += point                          # インスタンスが持つインスタンス変数pointに引数で受けとった値を加算

user_1 = User("山田太郎", "taro@example.com", 1000) # インスタンスの生成＝クラス名(イニシャライザの引数に渡す値)
user_2 = User("鈴木一郎", "ichiro@test.com", 500)

x = user_1.name                                      # 値を取得＝インスタンス.インスタンス変数名
y = user_2.name
print(x, y)

user_1.add_point(1000)                                   # メソッドの呼び出し＝オブジェクト名.メソッド名(引数に渡す値)
print(user_1.point)