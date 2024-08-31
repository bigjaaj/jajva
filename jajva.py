import sys

j = sys.argv[1:]

goodpart = lambda x: x[::-1].split(".",1)[1][::-1]

alias = {"prnt":"System.out.println","pub":"public","prv":"private","stat":"static","fin":"final"}

def tokens(j):
    l = []
    nl = ""
    for i in j:
        if i in ["	"," ",",",";","{","}","(",")","\n",'"']:
            l.append(nl)
            nl = ""
        else:
            nl = nl+i
    return l

def readalias(j):
    return j.replace("_"," ")


for i in j:
    with open(i) as f:
        with open(i.replace(".jajva",".java"),'w') as g:
            af = f.readlines()
            t = 0
            extra = 1
            if af[0]!="i":
                g.write(f"public class {goodpart(i)} {{")
            else:
                g.write(f"public interface {goodpart(i)} {{")
                t+=1
            if i == "Main.jajva":
                g.write("public static void main(String[] args) {")
                extra+=1
            stage = 0
            mode = 0
            attributs = []
            for k in af[t:]:
                if stage==0 and mode == 0:
                    nwat = []
                towrite = True
                good = k
                mots = tokens(good)
                print(mots)
                if mots[0] == "alias":
                    alias[mots[1]] = readalias(mots[2])
                    towrite = False
                    if word in alias:
                        good = good.replace(word,alias[word])
                if towrite:
                    g.write(good)
                # partie constructeurs

            for _ in range(extra):
                g.write("}")
