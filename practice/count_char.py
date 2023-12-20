l = 'Gopi Krishna Bandaru Nikhil Arjuna'
list_a = l.split()
for i in list_a:
    if i[0].lower() not in 'aeiou' and i[-1].lower() in 'aeiou':
        print(i,end=" ")