# Generating_Random_Sentences_with_N-gram_Language_Model with NLP, N-gram model, Markov assumption, text-processing(From Scratch)

1. Project objective

    - Build an N-gram language model from an arbitrary number of plain text files. 
    - Generate a given number of sentences based on that N-gram model


2. N-gram model

    - Separate punctuation marks from text and treat them as tokens. Numeric data is treated as tokens
    - Identify sentence boundaries, and n-grams should *not* cross these boundaries. 



 3. Please follow the following example to input the command.

   '>Python ngram.py 2 10 ngram.py warandpeace.txt middlemarch.txt shakespear.txt'
    
        - 2 bigrams
        - 10 implies the generation of 10 random sentences  
        - The last argument is the book name, or a book list.  
        - I used the novels warandpeace.txt middlemarch.txt shakespear.txt, please put the book/books in the same path with the script.
