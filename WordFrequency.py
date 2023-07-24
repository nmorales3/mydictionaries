infile= open('sometext-1.txt','r')
  
word_count= {}
count= 0

for word in infile:
    word=word.rstrip('/n')
    count +=1
    if word:
        word_count[word]= count
print(word_count)
    