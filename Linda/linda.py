'''
    Linda tuplespace implementation for blog system
    Authors:
        Guilherme Nishi Kanashiro - 628298
        Rodolfo Krambeck Asbahr - 628042
'''


'''
    Function to produce a tuple, writing it into tuplespace
    append the tuple in a tuplespace
'''
def _out(tuple_space,tuple):
    tuple_space.append(tuple)

'''
    Function to atomically read and remove a tuple from tuplespace
    return the number of removed entries
'''
def _in(tuple_space, tuple):
    entries = 0
    for entry_tuple in tuple_space:
        #print tuple, idx
        if tuple == entry_tuple:
            entries += 1

    msg = "Number of removed entries: " + str(entries) +"\n"

    while entries > 0:
        tuple_space.remove(tuple)
        entries -= 1

    return msg

'''
    Function to read a tuplespace - non-destructive
    return all the messages related the selected subject
'''
def _rd(tuple_space,subject):
    subject_entries = []

    for entry_owner, entry_subject, entry_text in tuple_space:
        if subject == entry_subject:
            subject_entries.append((entry_owner,entry_text))

    return subject_entries
