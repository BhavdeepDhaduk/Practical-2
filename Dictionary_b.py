"""BHAVDEEP DHADUK -20CE024
Write a Python script to merge two Python dictionaries."""

dict1 = {
    "trial":"easy",
    "money":"happiness"
}
dict2 = {
    1 : 11,
    200 : 29
}
#creating a new dictionary and copying the elements of first dictionary
dict3 = dict1.copy()
#updating the new dictionary by merging all elements of second dictionary
dict3.update(dict2)
print("combined dictionary is : ",dict3)