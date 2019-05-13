def _out(tuple_space,tuple):
    tuple_space.append(tuple)

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

def _rd(tuple_space,subject):
    subject_entries = []

    for entry_owner, entry_subject, entry_text in tuple_space:
        if subject == entry_subject:
            subject_entries.append((entry_owner,entry_text))



    return subject_entries
