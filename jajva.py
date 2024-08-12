import sys

j = sys.argv[1:]

goodpart = lambda x: x[::-1].split(".",1)[1][::-1]

alias = {"prnt":"System.out.println","pub":"public","priv":"private","stat":"static"}

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
            for k in af[t:]:
                for ali in alias:
                    good = k.replace(ali,alias[ali])
                g.write(good)
            for _ in range(extra):
                g.write("}")
