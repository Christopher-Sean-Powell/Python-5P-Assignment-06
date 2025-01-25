__author__ = 'Chris'

# Christopher Powell
# cspowell@ucsc.edu
# Assignment06: What's the Frequency, Kenneth?

# Note: I deleted all of the extraneous words form my text files, so they only contain the words that are in the books.
# I downloaded all three of the books from http://www.gutenberg.org/wiki/Main_Page.



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


def letters_total (l):
    ''' This function takes an ordered list of tuples, such as the output from sorted_keys_by_value, and sums up the
    values in the second slot in the tuple.'''
    total = 0
    for i in range (26):
        total += l[i][1]
    return total


def count_words (s):
    ''' This function takes a string as input, and then removes all punctuation from that string using the function
    no_punct(s), converts the whole string to lower case, and then splits the string up into a list of its individual
    words. Then the number of appearances of each word are counted and returned as a dictionary.'''
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


def counts_one_word (s, w):
    '''This function takes a string and a single word as input, and then returns the number of times that the entered
    word appeared in the entered string.'''
    counts = 0
    s = no_punct(s)
    s = s.lower()
    l = s.split()
    for i in range (len(l)):
        if w == l[i]:
            counts += 1
        else:
            pass
    return counts


# I got most of this next function from lecture on 5-15. I tweaked it a little bit to fit my needs.

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
    total_words = float(len(book_list))
    no_tuple_list = tuple_to_list(tuple_list)
    remade_tuples = []
    for j in range (30):
        no_tuple_list[j] /= total_words
        no_tuple_list[j] *= 100.0
    for k in range (30):
        remade_tuples.append ((tuple_list[k][0], no_tuple_list[k]))
    return remade_tuples


def words_in_all_30(l1, l2, l3):
    '''This function takes 3 lists (of tuples) as input, and then it creates a new list that contains only the values
    that were found in all 3 lists, along with their frequencies (averaged). Output is a dictionary.'''
    new_dict = {}
    for i in range (30):
        for j in range (30):
            for k in range (30):
                if l1[k][0] == l2[j][0] and l1[k][0] == l3[i][0]:
                    new_dict[l1[k][0]] = ((l1[k][1] + l2[k][1] + l3[k][1]) / 3.0)
                else:
                    pass
    return new_dict


def process_book (book_file):
    '''This function takes the name of a text file (a string) as an input, and then it opens and reads that text file,
    returning the following information: the number of times every word in the book is used, and the number of times
    every letter in the alphabet was used. This information is returned as a tuple of two dictionaries.'''
    file_1 = open (book_file, "r")
    new_file = no_punct(file_1)
    word_count = count_words (new_file)
    letter_count = count_letters(new_file)
    return (word_count, letter_count)

if __name__ == '__main__':

    wells = open("wells.txt", "r")
    wells = no_punct(wells)
    wells_words = count_words(wells)
    wells_30 = top_thirty(wells_words)
    wells_30_freq = thirty_frequency(wells, wells_30)
    wells_letters = count_letters(wells)
    wells_ltrs_ordered = sorted_keys_by_value(wells_letters)
    wells_ltrs_total = float(letters_total(wells_ltrs_ordered)) / 100.0

    stevenson = open("stevenson.txt", "r")
    stevenson = no_punct(stevenson)
    stevenson_words = count_words(stevenson)
    stevenson_30 = top_thirty(stevenson_words)
    stevenson_30_freq = thirty_frequency(stevenson, stevenson_30)
    stevenson_letters = count_letters(stevenson)
    stevenson_ltrs_ordered = sorted_keys_by_value(stevenson_letters)
    stevenson_ltrs_total = float(letters_total(stevenson_ltrs_ordered)) / 100.0

    dickens = open("dickens.txt", "r")
    dickens = no_punct(dickens)
    dickens_words = count_words(dickens)
    dickens_30 = top_thirty(dickens_words)
    dickens_30_freq = thirty_frequency(dickens, dickens_30)
    dickens_letters = count_letters(dickens)
    dickens_ltrs_ordered = sorted_keys_by_value(dickens_letters)
    dickens_ltrs_total = float(letters_total(dickens_ltrs_ordered)) / 100.0

    words_in_all = words_in_all_30(wells_30_freq, stevenson_30_freq, dickens_30_freq)
    ordered_words_all = sorted_keys_by_value(words_in_all)


    def overall_ltr_freq (w1, s1, d1):
        '''This function takes 3 lists as input. Its use is very particular to the program word_count. It takes the
        lists of tuples which contain the information for the frequency of each letter in the three books, and returns
        a new dictionary that contains the frequency of letter use across all 3 books, with each book weighted
        equally.'''

        new_list = []
        new_dict = {}
        w1_new = []
        s1_new = []
        d1_new = []
        for ltr in "abcdefghijklmnopqrstuvwxyz":
            for i in range (26):
                if w1[i][0] == ltr:
                    w1_new.append((w1[i][0], w1[i][1] / wells_ltrs_total))
                if s1[i][0] == ltr:
                    s1_new.append((s1[i][0], s1[i][1] / stevenson_ltrs_total))
                if d1[i][0] == ltr:
                    d1_new.append((d1[i][0], d1[i][1] / dickens_ltrs_total))
                else:
                    pass
        for j in range (26):
            new_list.append((w1_new[j][0], ((w1_new[j][1] + s1_new[j][1] + d1_new[j][1])) / 3.0))

        for k in range (26):
            new_dict[new_list[k][0]] = new_list[k][1]

        return new_dict


    overall_ltr_frequencies = overall_ltr_freq(wells_ltrs_ordered, stevenson_ltrs_ordered, dickens_ltrs_ordered)
    ordered_frequencies = sorted_keys_by_value(overall_ltr_frequencies)


    def top_30_combined (w1, book1, s1, book2, d1, book3):
        '''This function is rather complicated, and only very useful for the program word_count. It takes as input three
        books (or strings), as well as 3 lists of tuples that contain the top 30 words that appear in each of the books.
        It then combines these top 30 lists, and creates a new list (without repeats). Then, it searches through all 3
        books for the number of times each word in the new list appears, and sums those numbers. Then it inputs this
        information into a new dictionary, and divides the numbers by the total number of words in all 3 books, hence
        finding the percentages associated with the occurence of each word. The output is in the form of a dictionary.'''

        book1 = no_punct(book1)
        book_list1 = book1.split()
        total_words1 = float(len(book_list1))
        book2 = no_punct(book2)
        book_list2 = book2.split()
        total_words2 = float(len(book_list2))
        book3 = no_punct(book3)
        book_list3 = book3.split()
        total_words3 = float(len(book_list3))
        new_dict = {}
        new_dict2 = {}
        for i in range (30):
            if w1[i][0] in new_dict:
                new_dict[w1[i][0]] += 0
            else:
                new_dict[w1[i][0]] = 0
            if s1[i][0] in new_dict:
                new_dict[s1[i][0]] += 0
            else:
                new_dict[s1[i][0]] = 0
            if d1[i][0] in new_dict:
                new_dict[d1[i][0]] += 0
            else:
                new_dict[d1[i][0]] = 0
        new_list = new_dict.keys()
        if "utterson" in new_list:
            new_list.remove('utterson')
        for i in range (len(new_list)):
            new_dict2[new_list[i]] = 0
            new_dict2[new_list[i]] = (counts_one_word(book1, new_list[i]) / total_words1) + (counts_one_word(book2, new_list[i]) / total_words2) + (counts_one_word(book3, new_list[i]) / total_words3)
            new_dict2[new_list[i]] /= 3
            new_dict2[new_list[i]] *= 100.0
        return new_dict2


    top_30_combined1 = top_30_combined(wells_30_freq, wells, stevenson_30_freq, stevenson, dickens_30_freq, dickens)
    top_30_combined2 = sorted_keys_by_value(top_30_combined1)
    top_30_combined3 = top_30_combined2[0:30]


    print ""
    print "Wells Top 30 Words:"
    for i in range (30):
        print '{0:18s} : {1:.3f}%'.format(wells_30[i][0], thirty_frequency(wells, wells_30)[i][1])

    print ""
    print "Wells Letter Frequencies:"
    for j in range (26):
        print '{0:18s} : {1:.3f}%'.format(wells_ltrs_ordered[j][0], wells_ltrs_ordered[j][1]/wells_ltrs_total)

    print ""
    print "Stevenson Top 30 Words:"
    for i in range (30):
        print '{0:18s} : {1:.3f}%'.format(stevenson_30[i][0], thirty_frequency(stevenson, stevenson_30)[i][1])

    print ""
    print "Stevenson Letter Frequencies:"
    for j in range (26):
        print '{0:18s} : {1:.3f}%'.format(stevenson_ltrs_ordered[j][0], stevenson_ltrs_ordered[j][1]/stevenson_ltrs_total)

    print ""
    print "Dickens Top 30 Words:"
    for i in range (30):
        print '{0:18s} : {1:.3f}%'.format(dickens_30[i][0], thirty_frequency(dickens, dickens_30)[i][1])

    print ""
    print "Dickens Letter Frequencies:"
    for j in range (26):
        print '{0:18s} : {1:.3f}%'.format(dickens_ltrs_ordered[j][0], dickens_ltrs_ordered[j][1]/dickens_ltrs_total)

    print ""
    print "Overall Top 30 Words:"
    for w in range (30):
        print '{0:18s} : {1:.3f}%'.format(top_30_combined3[w][0], top_30_combined3[w][1])

    print ""
    print "Overall Letter Frequencies:"
    for k in range (26):
        print '{0:18s} : {1:.3f}%'.format (ordered_frequencies[k][0], ordered_frequencies[k][1])

    print ""
    print "Words in all three Top 30 lists:"
    for i in range (22):
        print ordered_words_all[i][0]