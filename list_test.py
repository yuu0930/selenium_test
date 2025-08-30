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