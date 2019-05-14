import linda

tuple_space = []

print tuple_space
fContinue = 1

whoAmI = raw_input("Who are you? ")

while(fContinue == 1):

    service = raw_input("Enter a service(in, out, rd): ")

    if service == "in":
        subject = raw_input("Enter a subject: ")
        text = raw_input("Enter a text: ")
        linda._in(tuple_space, (whoAmI, subject, text))
    elif service == "out":
        subject = raw_input("Enter a subject: ")
        text = raw_input("Enter a text: ")
        linda._out(tuple_space, (whoAmI, subject, text))
    elif service == "rd":
        subject = raw_input("Enter a subject: ")
        subject_entries = linda._rd(tuple_space, subject)
        if subject_entries != []:
            all_texts = ""

            for owner, text in subject_entries:
                all_texts += owner + ": " + text + "\n"
        else:
            all_texts = "No entries found for given subject."
        print(all_texts)
    else:
        print("Invalid service.")


    #print tuple_space

    fContinue = int(raw_input("Continue? "))
