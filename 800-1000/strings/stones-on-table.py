def main():
    n = input()
    s = input()
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    return count
print(main()) 