import heapq as hq
def heapsort(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for _ in range(len(h))]

if __name__ == '__main__':
    # a = [(1, 'B'), (3, 'D'), (5, 'F'), (7, 'H'), (9, 'J'), (2, 'C'), (4, 'E'), (6, 'G'), (8, 'I'), (0, 'A')]
    # q = heapsort(a)
    # for i in q:
    #     print(i[0], i[1])

    # q = hq.heapify(a)
    # print(a)

    import random
    h = []
    for i in range(10, -1, -1):
        # hq.heappush(h, (i + i, i))
        key = random.randint(0, 10)
        hq.heappush(h, (key + i, key, i))
    print(f'heap min: {h}')
    print("-" * 20)
    print(f'Smallest {hq.nsmallest(1,h)}')
    print(f'Largest {hq.nlargest(1,h)}')

    print('-' * 20)
    print('Heap sort:')
    for i in range(len(h)):
        item = hq.heappop(h)
        #print(item[0], item[1], item[2])
        print(i, item)
