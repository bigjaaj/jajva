import sys

j = sys.argv[1:]

goodpart = lambda x: x[::-1].split(".",1)[1][::-1]

for i in j:
    with open(i) as f:
        with open(i.replace(".jajva",".java"),'w') as g:
            af = f.read()
            af = af.replace("prnt","System.out.println")
            t = 0
            extra = 1
            if af[0]!="i":
                g.write(f"public class {goodpart(i)} {{")
            else:
                g.write(f"public interface {goodpart(i)} {{")
                t+=2
            if i == "Main.jajva":
                g.write("public static void main(String[] args) {")
                extra+=1
            g.write(af[t:])
            for _ in range(extra):
                g.write("}")
