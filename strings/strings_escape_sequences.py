def main():
    #String escape sequences

    synp =  """Dracula comprises journal entries, letters, and telegrams written by the main characters.
It begins with Jonathan Harker, a young English lawyer, as he travels to Transylvania.
Harker plans to meet with Count Dracula, a client of his firm, in order to finalize a property transaction.
When he arrives in Transylvania, the locals react with terror after he discloses his destination: Castle Dracula.
Though this unsettles him slightly, he continues onward.
The ominous howling of wolves rings through the air as he arrives at the castle.
When Harker meets Dracula, he acknowledges that the man is pale, gaunt, and strange.
Harker becomes further concerned when, after Harker cuts himself while shaving, Dracula lunges at his throat.
Soon after, Harker is seduced by three female vampires, from whom he barely escapes.
He then learns Dracula’s secret—that he is a vampire and survives by drinking human blood.
Harker correctly assumes that he is to be the count’s next victim.
He attacks the count, but his efforts are unsuccessful.
Dracula leaves Harker trapped in the castle and then, along with 50 boxes of dirt, departs for England."""

    print('Synopsis:', synp)


#escape string using \' Single Quote
    mystr = "It\'s alright"
    print(mystr)

#escape string using \\ Backslash
    mystr = "This is \\ (Backslash)"
    print(mystr)

#escape string using \n New Line
    mystr = "This is 1st line \n and its newline (Backslash)"
    print(mystr)

#escape string using \r Carriage Return
    mystr = "This is 1st line \r and its newline (Carriage Return)"
    print(mystr)

#escape string using \t tab
    mystr = "This is 1st line \t with tab (Tab)"
    print(mystr)

#escape string using \b Backspace
    mystr = "Hello\bWorld"
    print(mystr)

#escape string using \ooo Octal Value
    mystr = "\110\145\154\154\157"
    print(mystr)

#escape string using \xhh Hexa Value
    mystr = "\x48\x65\x6c\x6c\x6f"
    print(mystr)

if __name__=='__main__':
    main()