import json
#load file
entry_file = open("./input/songbook.txt","r",encoding="utf-8")
lines = entry_file.readlines()

#identify title in UPPER cases and put "_" before to split
for i in range(len(lines)):
    if(lines[i][:6].isupper()):
        lines[i] = "_"+lines[i]

song_array = "\n".join(lines)#put all together in one string
song_array = song_array.split("_")#and divide it into songs

#split each song into multiples lines
splited = []
for i in song_array:
    splited.append(i.splitlines(False))

#adds new line in the lyric instead of an empty space
songs = []
for i in splited:
    lyric = []
    for j in i:
        a = j
        if(a ==""):
            a = "\n"
        lyric.append(a)
    songs.append(lyric) 
#print(len(songs)) #number of songs

#removes consecutives lines jumps allowing max 2 (one empty line)
out = []
jumps = 0
for i in songs:
    aux = []
    for j in range(len(i)):
        if(i[j] == "\n"):
            jumps += 1
            if(jumps < 3):
                aux.append(i[j])
        else:
            aux.append(i[j])
            jumps = 0
    out.append(aux)

#output_file.txt
#output_file = open("./output/output_file.txt","w",encoding="utf-8")
#for i in out:
#    for j in i:
#        output_file.write(j)

#titles.txt
#output_file = open("./output/titles.txt","w",encoding="utf-8")
#for i in out:
#    output_file.write(i[0])
#    output_file.write("\n")

apart = []
for i in out:
    words = i[0].split()
    title = ""
    autor = ""
    aux = {}
    for word in words:
        if(word.isupper()):
            if( len(word)==2 and word[1]!= "."):
                title += word
                title += " "
            elif(len(word)==2 and word[-1]== "."):
                autor += word
                autor += " "
            else:
                title += word
                title += " "
        elif(word.isnumeric()):
            title += word
            title += " "
        else:
            autor += word
            autor += " "
    title = title[:-1]
    autor = autor[:-1]
    aux["title"] = title
    aux["autor"] = autor
    aux["lyric"] = i[2:]
    apart.append(aux)

#output.json
#output_file = open("./output/output.json","w",encoding="utf-8")
#for i in apart:
#    output_file.write(str(i))
#    output_file.write(",")

with open("./output/output.json", "w", encoding="utf-8") as outfile:  
    json.dump(apart, outfile) 
