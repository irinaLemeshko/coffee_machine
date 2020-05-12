string = input()
half_len = len(string) // 2
for i in range(half_len):
    if string[i] != string[-i - 1]:
        print("Not palindrome")
        break
else:
    print("Palindrome")
