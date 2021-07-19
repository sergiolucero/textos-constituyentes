#SOURCE: https://www.kaggle.com/currie32/comparing-books-with-word2vec-and-doc2vec
import codecs
import gensim
import glob
import pandas as pd
from pprint import pprint
import seaborn as sns
import matplotlib.pyplot as plt

program_filenames = sorted(glob.glob('*.txt'))
program_corpus = []

for program_filename in program_filenames:
    with codecs.open(program_filename, "r", "utf-8") as program_file:
        program_corpus.append(
            gensim.models.doc2vec.TaggedDocument(
                gensim.utils.simple_preprocess( # Clean the text with simple_preprocess
                    program_file.read()),
                    ["{}".format(program_filename)])) # Tag each program with its filename

model = gensim.models.Doc2Vec(vector_size = 300, min_count = 3, epochs = 100)
model.build_vocab(program_corpus)
print("tamaño del vocabulario del modelo:", len(model.wv.vocab))
#########################################
model.train(program_corpus, total_examples=len(program_corpus),epochs=100)

for ix in range(len(program_corpus)):
    print(program_filenames[ix])
    pprint(model.docvecs.most_similar(ix))

ms_boric = model.docvecs.most_similar(4)
sim_boric = pd.DataFrame(dict(programa=[msb[0][11:-4] for msb in ms_boric], 
                                semejanza=[round(msb[1],3) for msb in ms_boric]))
sim_boric = sim_boric.sort_values('semejanza', ascending=False)

f, ax = plt.subplots(figsize=(12, 12))
# sns.barplot(x="semejanza", y="programa", data=sim_boric, color="b")
ax.hlines(y=sim_boric.programa, xmin=0.0, xmax=sim_boric.semejanza, color='firebrick', alpha=0.7, linewidth=2)
ax.scatter(y=sim_boric.programa, x=sim_boric.semejanza, s=250, color='firebrick', alpha=0.7)
ax.set_xlim(0, 0.2)
plt.title("Semejanza de programas presidenciales al de Gabriel Boric, según gensim/doc2vec", fontsize=18)
plt.show()