def sort(data):
    gaps = [7, 3, 1] # ギャップの値をあらかじめ設定
    for gap in gaps:  # Gapをだんだん狭めて繰り返す
        for start in range(gap): # gap文離れた複数の組を順番にソート
            for i in range(start, len(data), gap): # gapの幅で飛ばしながら挿入ソート
                for j in range(i-gap, -1, -gap): # 終値を-1に設定（０まで実行）
                    if data[j] > data[j+gap]: #gap文離れた要素で前の方が大きい場合
                        data[j], data[j+gap] = data[j+gap], data[j] #要素を入れ替える
                    else:
                        break #挿入する部分が見つかれば終わり


data = [1, 3, 2, 5, 4, 2, 1]
sort(data)
print(data)


