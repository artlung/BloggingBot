import markovify

corpus = open("artlung.corpus.cleaned.txt").read()

text_model = markovify.Text(corpus, state_size=3)
model_json = text_model.to_json()

handle = open('artlung.model.json','r+')
handle.write(model_json)
handle.close()
