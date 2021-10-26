from heapq import heappush, heappop # ヒープを扱う標準ライブラリheapqを利用

def sort(data):
    heap = [] #空のヒープ（リスト）を作成
    while data: # dataから要素をとりだして、ヒープに入れる
        heappush(heap, data.pop()) # dataから要素を取り出して、ヒープに入れる
    while heap: #heapから順に要素を取り出し、dataに戻す
        data.append(heappop(heap)) # heapから最小値をとりだして、dataの最後に追加する


data = [1, 3, 2, 5, 4, 2, 1]
sort(data)
print(data)


