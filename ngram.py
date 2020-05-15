# N-grams
# This program is written by Sree Bhanu Nori
# We have used the texts 'shakespear.txt', 'warandpeace.txt' and 'middlemarch.txt' to reach 10,000,000 words.
# For additional functionality we have set the time to how much time does it take for   the program to give the required output in seconds
# We are generating random sentences depending on the n-value given
# 1. We start tokenizing using word_tokenize and sent_tokenize 
# 2. padded_everygram_pipeline is used to pad the sentences and chain flat stream of  words
# 3. We save the script in the log.txt file
# 4. Then we set the model to design the data so that words can be saved and sentences can be generated
# We run this file on the command prompt using the file name ngram.py
# Eg: Python ngram.py 2 10 ngram.py warandpeace.txt middlemarch.txt shakespear.txt

import time
start = time.time()
import sys
from nltk import word_tokenize, sent_tokenize 
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.tokenize.treebank import TreebankWordDetokenizer
import random
detokenize = TreebankWordDetokenizer().detokenize
def generate_sent(model, num_words):
    content = []
    random_seed = random.random()
    tokens = list(model.generate(num_words,random_seed=random_seed))
    while(not tokens[0].isalpha()):
        random_seed = random.random()
        tokens = list(model.generate(num_words,random_seed=random_seed))
    tokens[0] = tokens[0].capitalize() 
    for token in tokens:
        if token == '<s>':
            continue
        if token == '</s>':
            break
        content.append(token)
    if(content[len(content)-1] != "."):
        content.append(".")
    return detokenize(content)
file = open("ngram-log.txt","a",encoding="utf-8")
n=int(sys.argv[1])
m=int(sys.argv[2])
s = "Generating " + str(m) + " sentences using ngrams with n = " + str(n) + " :\n"
file.write(s)
print(s)
text = ""
for i in range(3,len(sys.argv)):
    temp = open(sys.argv[i], 'rt', encoding="utf8").read()
    text = text + temp   
tokenized_text = [list(map(str.lower, word_tokenize(sent))) 
                 for sent in sent_tokenize(text)]
train_data, padded_sent = padded_everygram_pipeline(n, tokenized_text)
from nltk.lm import MLE
model = MLE(n)
model.fit(train_data, padded_sent)
for i in range(0,m):
    s = str(i+1) + ". " + generate_sent(model,2^32)
    print(s)
    file.write(s + "\n")
end = time.time()
s="\nTime taken to run the program = " + str(end-start) + "seconds"
print(s)
file.write(s + "\n\n")