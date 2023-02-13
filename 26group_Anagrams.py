class Solution:
    # def is_anagrams(self, str1, str2):
    #     str_l1 = list(str1)
    #     str_l1.sort()
    #     str_l2 = list(str2)
    #     str_l2.sort()

    #     if str_l1 == str_l2:
    #         return True
    #     return False

    def groupAnagrams(self,list_str):
        d = {}

        for i in range(len(list_str)):
            x = ''.join(sorted(list_str[i]))
            if x not in d:
                d[x] = [list_str[i]]
            else:
                d[x].append(list_str[i])
        return d.values()
    # final_list = []
    #     new_list = list_str
    #     l = [""]
    #     if list_str == [""]:
    #         print('in', final_list.append(list_str.append('\""')))
    #         return final_list.append(list_str.append('\"\"'))
    #     elif len(list_str) == 1:
    #         print('hi')
    #         return list(list_str)
    #     for i, str1 in enumerate(list_str):
    #         sublist = []
    #         for j, str2 in enumerate(new_list):
    #             if j > 0 and str1 != str2:
    #                 if self.is_anagrams(str1, str2):
    #                     if not sublist:
    #                         sublist.extend((str1, str2))
    #                     else:
    #                         sublist.append(str2)
    #                     list_str.pop(j)
    #             elif j > 0 and (str1 == str2):
    #                 if str1 not in sublist:
    #                     sublist.append(str1)
    #         final_list.append(sublist)
    #     return final_list



