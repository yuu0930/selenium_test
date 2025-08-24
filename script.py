x = [10, 20, 30, 40, 50]          # リスト
y = max(x)
z = min(x)
total_sum = sum(x)                      # 合計
sort = sorted(x)                  # ソート昇順
reverse = sorted(x, reverse=True) # ソート降順

print(y)
print(z)
print(sum)
print(sort)
print(reverse)

scores = {"国語": 92, "数学": 55, "英語": 85, "理科": 77, "社会": 95} # 辞書{key: value}
print(scores["国語"])                                                # 変数名["key"]

scores["音楽"] = 65                                                  # 辞書に要素を追加
print(scores)

scores["国語"] = 88                                                  # 辞書のvalueを変更
print(scores)

keys = scores.keys()                                                 # keyだけ取得(dict_keys)
print(keys)

keys = list(scores.keys())                                           # リストに型変換
print(keys)

values = scores.values()                                             # valueだけを取得(dict_values)
print(values)

values = list(scores.values())                                       # リスト型に変換
print(values)

max_score = max(scores.values())
min_score = min(scores.values())
subtraction = max_score - min_score
print(f"{subtraction}点差です")

avg_score = sum(scores.values()) / len(scores.values())
print(f"平均点は{avg_score}点です！")