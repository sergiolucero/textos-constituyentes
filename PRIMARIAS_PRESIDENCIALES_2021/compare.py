#SOURCE: https://www.kaggle.com/currie32/comparing-books-with-word2vec-and-doc2vec
import codecs
import gensim
import glob
import time
import pandas as pd
from pprint import pprint

program_filenames = glob.glob('*.txt')
program_corpus = []

t0=time.time()
for program_filename in program_filenames:
    with codecs.open(program_filename, "r", "utf-8") as program_file:
        program_corpus.append(
            gensim.models.doc2vec.TaggedDocument(
                gensim.utils.simple_preprocess( # Clean the text with simple_preprocess
                    program_file.read()),
                    ["{}".format(program_filename)])) # Tag each program with its filename
t1=time.time()
print('DT:', round(t1-t0,2))

model = gensim.models.Doc2Vec(size = 300, 
                              min_count = 3, 
                              epochs = 100)

model.build_vocab(program_corpus)
t2=time.time()
print("model's vocabulary length:", len(model.wv.vocab))
print('DT:', round(t2-t1,2))
#########################################
model.train(program_corpus, total_examples=len(program_corpus),epochs=100)

for ix in range(len(program_corpus)):
    print(program_filenames[ix])
    pprint(model.docvecs.most_similar(ix))

ms_boric = model.docvecs.most_similar(0)
sim_boric = pd.DataFrame(dict(programas=[msb[0] for msb in ms_boric], sims=[round(msb[1],3) for msb in ms_boric]))
####################
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(6, 15))

sns.set_color_codes("pastel")
sns.barplot(x="semejanza", y="programa", data="sim_boric", color="b")
