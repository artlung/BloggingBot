import markovify

# Get raw text as string.
with open("artlung.model.json") as f:
    model_json = f.read()

reconstituted_model = markovify.Text.from_json(model_json)

# Print five randomly-generated sentences
print(reconstituted_model.make_sentence())

handle = open('sample_sentences.txt','r+')

# Print three randomly-generated sentences of no more than 140 characters
for i in range(10000):
    sentence = reconstituted_model.make_short_sentence(140).encode('utf-8')
    handle.write(sentence)
    handle.write("\n")

handle.close()
