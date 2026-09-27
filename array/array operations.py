def two_sum_sorted(a, target):
    left = 0
    right = len(a) - 1

    while left < right:
        current_sum = a[left] + a[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


def reverse_array(a):
    left = 0
    right = len(a) - 1

    for _ in range(len(a) // 2):
        temp = a[left]
        a[left] = a[right]
        a[right] = temp

        left += 1
        right -= 1

    return a

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
      
a = [23, 40, 50, 60, 70]

print(two_sum_sorted(a, 100))
print(reverse_array(a))
print(is_palindrome("charan"))