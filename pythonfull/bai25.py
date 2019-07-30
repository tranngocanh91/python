def is_group_member(group_data,m):
        for value in  group_data:
            if m == value :
                return  True
        return  False


print(is_group_member([2,4,5,6,2],4))