import pprint
message='Bila je guzva na salteru ali sam uspeo da stignem na red'
count={}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1

pprint.pprint(count)