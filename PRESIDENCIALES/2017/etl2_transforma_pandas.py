import glob, fitz
import pandas as pd

files=glob.glob('*.pdf')
texts=[' '.join([page.getText() for page in fitz.open(fn)]) for fn in files]

for fn, text in zip(files,texts):
    tfn = fn.replace('.pdf','.txt')
    fw = open(tfn,'w')
    fw.write(text)
    fw.close()
    print(tfn)

df=pd.DataFrame(dict(archivo=files, texto=texts))
df['largo']=df.texto.apply(len)     # Piñera no quedó bien
df.to_csv('programas.csv',index=False)
