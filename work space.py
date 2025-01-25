__author__ = 'Chris'


def no_punct(s):
    ''' This function takes a string as input and returns that string without any kind of punctuation symbols.'''
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    s_no_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_no_punct += letter
    return s_no_punct


def count_letters (s):
    '''This function takes a string as input, and makes it lowercase. It then counts the number of times that every letter appears in the string.'''
    d = {}
    s = s.lower()
    s = no_punct(s)
    letters = "abcdefghijklmnopqrstuvwxzy"
    for ltr in letters:
        d[ltr] = 0
    for i in range (len(s)):
        if s[i] in letters:
            d[(s[i])] += 1
    return d


def count_words (s):
    ''' This function takes a string as input, and then removes all punctuation from that string using the function no_punct(s), converts the whole string to lower case, and then splits the string up into a list of its individual words. Then the number of appearances of each word are counted and returned as a dictionary.'''
    s = no_punct(s)
    s = s.lower()
    l = s.split()
    d = {}
    for w in l:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d


# I got most of this function from lecture on 5-15. I tweaked it a little bit to fit my needs.

def sorted_keys_by_value (d):
    ''' This function takes a dictionary as an input, and then orders that dictionary based on the values of each key.
    This reordered list is returned as a list of tuples.'''
    counts = []
    for k in d.keys():
        counts.append ((d[k], k))
    counts.sort()
    counts.reverse()
    sorted_keys = []
    for item in counts:
        sorted_keys.append ((item[1], item[0]))
    return sorted_keys


def tuple_to_list (t):
    '''This function takes a list of tuples, and returns a new list composed solely of the second value in each tuple.'''
    new_list = [0]*30
    for j in range (30):
        new_list[j] = 0
        new_list[j] += t[j][1]
    return new_list


def top_thirty (word_count):
    '''This function takes a dictionary as an input, and then it reorders that dictionary using the function
    sorted_keys_by_value. It then returns the new sorted list (a list of tuples), and slices the list to only
    include the top 30 words.'''
    list = sorted_keys_by_value(word_count)
    new_list = list[0:30]
    return new_list


def thirty_frequency (book, tuple_list):
    '''This function takes 2 inputs: a string and a list (of tuples) of the number of times the top 30 words in that
    string are used. It then takes the number of times each word is seen and divides those numbers by the total number
    of words in the string to return the percentage the top 30 words were used in the entire string.'''
    book = no_punct(book)
    book_list = book.split()
    total_words = len(book_list)
    tuple_list = tuple_to_list(tuple_list)
    for j in range (30):
        tuple_list[j] /= float(total_words)
        tuple_list[j] *= 100.0
    return tuple_list


def top_30_combined (list1, list2, list3):
    combined_counts = [0]*90
    for i in range (30):
        combined_counts[i] = list1[j] + list2[j] + list3[j]
        combined_counts[i] /= 3


def process_book (book_file):
    '''This function takes the name of a text file (a string) as an input, and then it opens and reads that text file,
    returning the following information: the number of times every word in the book is used, and the number of times
    every letter in the alphabet was used. This information is returned as a tuple of two dictionaries.'''
    file = open (book_file, "r")
    new_file = no_punct(file)
    word_count = count_words (new_file)
    letter_count = count_letters(new_file)
    return (word_count, letter_count)





book = open("wells.txt", "r")

book = no_punct(book)

word_count = count_words(book)

top_30 = top_thirty(word_count)

print thirty_frequency(book, top_30)






if __name__ == '__main__':

    wells = open("wells.txt", "r")
    wells = no_punct(wells)
    stevenson = open("stevenson.txt", "r")
    stevenson = no_punct(stevenson)
    dickens = open("dickens.txt", "r")
    dickens = no_punct(dickens)


    wells_words = count_words(wells)
    wells_30 = top_thirty(wells_words)

    for i in range (30):
        print '{0:18s} : {1:.2f}%'.format(count_words(wells)[i], thirty_frequency(wells, wells_30))

def top_30_combined (list1, list2, list3):
    ''' This function takes the input of 3 lists of numbers, and then it averages the corresponding values and returns
    the averages as a new list.'''
    combined_counts = [0]*90
    for j in range (30):
        combined_counts[i] = list1[j] + list2[j] + list3[j]
        combined_counts[i] /= 3
    return combined_counts


def overall_word_freq (w1, s1, d1, top_22):
    new_dict = {}
    new_list0 = []
    new_list1 = []
    new_list2 = []
    for i in range (22):
        new_list0 += [top_22[i][0]]
    for i in range (30):
        if w1[i][0] not in new_list0:
            new_list1 += [(w1[i][0], w1[i][1])]
        if s1[i][0] not in new_list0:
            new_list1 += [(s1[i][0], s1[i][1])]
        if d1[i][0] not in new_list0:
            new_list1 += [(d1[i][0], d1[i][1])]
    new_list1.sort()
    for j in range (10):
        if new_list1[j][0] == new_list1[j+1][0]:
            new_list2 += [(new_list1[j][0], (new_list1[j+1][1] + new_list1[j][1]) / 2.0)]
            new_list1.remove(new_list1[j])
            new_list1.remove(new_list1[j+1])






    for i in range (len(new_list1)):
        new_dict[new_list1[i][0]] = new_list1[i][1]
    new_dict1 = sorted_keys_by_value(new_dict)
    return new_list2
