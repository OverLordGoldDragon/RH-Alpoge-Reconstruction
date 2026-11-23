import sys; sys.argv=['q','x','x']; sys.path.insert(0,'/home/claude/eblock/scripts/cleanup')
import q, pickle, csv
P=pickle.load(open('/home/claude/idx/eb_sets.pkl','rb'))
cls={}
for r in csv.reader(open('/home/claude/eblock/support/Claude_Audit_Core/Final_D123/D123_Declaration_Classes.tsv'),delimiter='\t'):
    cls[r[0]]=r[1:]
for k,(SE,SD) in P.items():
    hit=[(q.names[j],cls[q.names[j]]) for j in SD if q.names[j] in cls]
    print(k, len(SD), "in D123 table:", len(hit))
    from collections import Counter
    print("   ", Counter(tuple(v[-1:]) for _,v in hit).most_common(6))
