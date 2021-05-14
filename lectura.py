import glob, pandas as pd

cfiles=glob.glob('CONSTITUYENTES/*.txt')
ctexts=[open(fn).read() for fn in cfiles]
cdf = pd.DataFrame(dict(archivo=cfiles, texto=ctexts))
cdf['distrito']=cdf.archivo.apply(lambda fn: fn.split('/')[1].split('_')[0])
cdf['largo']=cdf.texto.apply(len)

print('LEIMOS', len(cdf), 'documentos')
