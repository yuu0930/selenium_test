numbers = [10, 21, 32, 65]

for n in numbers:           # for文の途中で後続処理をスキップして次の繰り返し処理を行いたい場合に使用する
    print(f"{n}:前処理")
    if n % 2 == 0:          # 2の倍数の時だけ後続処理を行わない
        continue            # つまり、この場合、奇数の時だけ後処理とprintされる
    print(f"{n}:後処理")