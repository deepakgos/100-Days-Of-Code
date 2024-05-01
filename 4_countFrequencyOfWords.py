def countWords(input_string):
    my_dict = {}
    split_string = input_string.split(' ')
    
    for word in split_string:
        print(my_dict.get(word,0))
        my_dict[word] = my_dict.get(word,0)+1
        print(my_dict.get(word))

        # if word not in my_dict.keys():
        #     my_dict[word] = 0
        # my_dict[word] += 1
    print(my_dict)

input_string = input("Enter a string:\n")
countWords(input_string)


#.get(word,0) returns the value of word or the key if present else initializes it with zero.