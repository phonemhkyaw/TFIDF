import pprint


# task: count unique words 
# task: make sure each words having the same base are the same, "the," = "the?" = "the"
# hint: google how to get rid of puntuations or special characters while processing the files
# TFIDF = Text Frequency (# of words) - Inverse Document Frequency (# of documents)

# good good good / ~ TF/IDF ~ 1 Ratios. 10/10 cookies 4.3

f = open("bible.txt", "r")  #opens bible.txt file

frequency_count = {} #creates empty dictionary



for row in f.readlines(): #for every row in the entire txt file...           #READING ENTIRE TEXT LINES (INDEX AT 2)
 
    row_split = row.strip().split(":")  #split colons (:)                                    
 
    row_split = row_split[2::] #index now starts at 2 

    for sentence in row_split: #for every sentence in the list starting at index 2... #READING ENTIRE SENTENCES 
    
        sentence_split = sentence.strip().split(" ")  #split spaces

        for word in sentence_split: #for every word in the split spaces list    #READING WORDS
            word = word.lower().strip(",").strip(".").strip(";").strip("?").strip("-").strip("\'s")  #NOTE: \'s is set as normal word
            

            if word in frequency_count:  #if word is in dictionary
                      
                frequency_count[word] = frequency_count[word] + 1 #add to dictionary key and add 1 to its value

            else: #but if not...., 
                frequency_count[word] = 1 #the dictionary key is added but the value is at 1

print(frequency_count)  #pretty printing 