import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

paper_total = 0
ribbon_total = 0
for line in lines:
    line = line.rstrip()
    dims = line.split("x")
    l, w, h = dims
    l = int(l)
    w = int(w)
    h = int(h)

    paper_area = 2*(l*w + w*h + h*l)
    extra_paper = min([l*w, w*h, h*l])
    paper_total += paper_area + extra_paper

    ribbon_length = 2*min([w + h, l + h, l + w])
    extra_ribbon = l*w*h
    ribbon_total += ribbon_length + extra_ribbon

print(f"The total amount of wrapping paper the elves should order is: {paper_total}")
print(f"The total amount of ribbon the elves should order is: {ribbon_total}")