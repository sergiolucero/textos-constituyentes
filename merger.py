import glob, pandas as pd

def loader(path, tag):

    files = glob.glob(path)
    texts = [open(fn).read() for fn in files]

    df = pd.DataFrame(dict(archivo=files, texto=texts))
    df['largo'] = df.texto.apply(len)
    df['tipo'] = tag
    print(path, 'N=', len(df))

    return df

cdf=loader('CONSTITUYENTES/*txt', 'general')
odf=loader('ORIGINARIOS/*txt','originarios')
gdf=loader('GOBERNADORES/*txt','gobernadores')

cdf.to_csv('CSV/constituyentes_general.csv',index=False)
odf.to_csv('CSV/constituyentes_originarios.csv',index=False)
gdf.to_csv('CSV/gobernadores.csv',index=False)

xdf=(cdf.append(odf)).append(gdf)
xdf.to_csv('CSV/programas.csv',index=False)
