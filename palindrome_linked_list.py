def isListPalindrome(l):
    temp = l
    count = 0

    while temp:
        count += 1
        temp = temp.next
    left, right= [], []
    temp = l
    for i in range(count //2):
        left.append(temp.value)
        temp = temp.next

    if count % 2 == 1:
        temp = temp.next
    for i in range(count //2):
        right.append(temp.value)
        temp = temp.next
    return left == right[::-1]
