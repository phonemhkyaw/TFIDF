import sys
import pprint
f = open("bible.txt", "r")

# fruits = ["apple", "banana", "watermelon", "mango", "kiwi"]
# print(fruits)
# print(fruits[2::])
# print(fruits)

# TASK: 
#  count how many times each word appears 
#  "The" - 500, "and" - 1000
freq_count = {}

for row in f.readlines():
    # print(row.strip())
    row_split = row.strip().split(":")
    # print(row_split)
    row_split = row_split[2::] # make a new array starting from index 2
    # print(row_split)

    for sentence in row_split: # row_split = [' Johnny ate an apple with his fork', ' and he said he screwed Up']
        # print(sentence.strip())

        sentence = sentence.strip().split(" ") # ['Johnny', 'ate', 'an', 'apple', 'with', 'his', 'fork']
        
        for word in sentence: 
            word = word.strip().lower() # strip gets rid of white spaces 
            print(word) # 'Johnny' 

            if word in freq_count: # is the word "Johnny" in the freq_count?
                freq_count[word] = freq_count[word] + 1
            else: # if the word is not in the freq_count 
                freq_count[word] = 1

pprint.pprint(freq_count)






