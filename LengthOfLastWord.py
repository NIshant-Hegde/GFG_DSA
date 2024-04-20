def lengthOfLastWord(s):
    count = 0
    for i in range(len(s), 0, -1):
        t, count = i - 1, 0
        print(s[i - 1])
        if s[i - 1] != " ":
            print("here")
            while s[t] != " ":
                count += 1
                if t <= 0:
                    break
                else:
                    t -= 1
            break
            
    return count

s = 'Nishant is awesome'
print(lengthOfLastWord(s))