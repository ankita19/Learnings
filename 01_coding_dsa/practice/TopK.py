from collections import Counter


def findTopKWithRegularDic(data, k):
    if data is None:
        return []
    freq_dic = {}
    # build freq dict
    for item in data:
        freq_dic[item] = freq_dic.get(item, 0) + 1

    sorted_items = sorted(freq_dic.items(), key=lambda frq : (-frq[1], str(frq[0])))
    return sorted_items[:k]


def findTopKWithCounter(self, data):
    if data is None:
        return []

    freq_count = Counter(data)
    return freq_count.most_common(self.k)

if __name__ == "__main__":
    data = ["aa", "aa","bb", "cc", "bb", "cc", "cc","ca", "ca", "ca"]
    # topK.findTopK(data, 3)
    print(findTopKWithRegularDic(data, 3))
    #print(topK.findTopKWithCounter(data))
