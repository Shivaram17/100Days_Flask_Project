def is_anagrams(str1, str2):
  str_l1 = list(str1)
  str_l1.sort()
  str_l2 = list(str2)
  str_l2.sort()

  if str_l1 == str_l2:
    return True
  return False
