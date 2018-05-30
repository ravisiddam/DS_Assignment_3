
# coding: utf-8

# In[14]:


fName = input("First Name?")
lName = input("Last Name?")
rev_str = ""
my_list = []
new_str = fName + " " + lName
idx = len(new_str)

while idx:
    idx = idx - 1
    rev_str += new_str[idx]
    
print(rev_str)




