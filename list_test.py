fruits = ["りんご", "バナナ", "オレンジ"]
print(f"先頭は{fruits[0]}です")
print(f"末尾は{fruits[-1]}です")

number = "03-1111-2222"
second_element = number[:2]
len_number = len(number)
print(second_element, len_number)

fourth_to_seventh = number[3:7]     # 4文字目から7文字目までを取り出す
print(fourth_to_seventh)

number_list = number.split("-")     # "対象の文字列".split("区切り文字")＝指定した文字で区切ったリストを取得できる
print(number_list)

join_number = "-".join(number_list) # リストの各要素をある区切り文字で結合して文字列を作るには文字列のjoinメソッドを使用する
print(join_number)

numbers = [3, 1, 4, 2, 5]
sorted_numbers = sorted(numbers)    # sorted関数は昇順に並び替える
print(sorted_numbers[:3])

numbers.reverse()                   # reverseはリストの要素を逆順にする
print(numbers)

sum_numbers = sum(numbers)          # リストの合計値
max_numbers = max(numbers)          # リストの最大値
min_numbers = min(numbers)          # リストの最小値
print(sum_numbers, max_numbers, min_numbers)

second_number = numbers.pop(1)      # popメソッドは指定した値を削除する,この場合2を削除し、second_numberには削除した2が代入される
print(numbers)
print(second_number)
