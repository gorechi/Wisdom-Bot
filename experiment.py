import markovify

# Get raw text as string.
with open("pogovorki_source.txt", encoding='utf-8') as f:
    text1 = f.read()


# Build the model.
pogovorki_model = markovify.Text(text1)


# Print three randomly-generated sentences of no more than 280 characters
for i in range(100):
    print("-"*40)
    print(pogovorki_model.make_short_sentence(1000))