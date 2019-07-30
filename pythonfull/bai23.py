def substring_coppy(str,n):

        substr = str[:3]
        result = " "
        for i in range(n):
            result=result+substr
        return result
print(substring_coppy("aawdawd",2))


