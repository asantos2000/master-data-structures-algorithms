# https://www.guru99.com/python-queue-example.html
# https://event.on24.com/eventRegistration/console/EventConsoleApollo.jsp?&eventid=3304055

if __name__ == "__main__":

    # List
    print("List")
    a = [2,4,5,2]
    print(a)
    a.append(9)
    print(a)
    v = a.pop()
    print(v, a)

    # Bad use - force shift all element to left
    a = [2,4,5,2]
    print(a)
    v = a.pop(0)
    print(v, a)

    # Deque
    print("deque")
    from collections import deque
    st = deque([2,3,4])
    st.append(27)
    print(st)
    v = st.pop()
    print(v, st)

    # remove first
    print("deque popleft")
    st = deque([2,3,4])
    st.append(30)
    print(st)
    v = st.popleft()
    print(v, st)

    # LifoQueue
    print("LifoQueue")
    from queue import LifoQueue
    st = LifoQueue()
    st.put(95)
    print(st.queue)
    v = st.get()
    print(v, st.queue)

    # Queue
    print("Queue")
    from queue import Queue
    st = Queue()
    st.put(95)
    print(st.queue)
    v = st.get()
    print(v, st.queue)
