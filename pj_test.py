from polyjuice import Polyjuice

pj = Polyjuice(model_path="uw-hai/polyjuice", is_cuda=True)

# the base sentence
text = "It is great for kids."

# perturb the sentence with one line:
# When running it for the first time, the wrapper will automatically
# load related models, e.g. the generator and the perplexity filter.
perturbations = pj.perturb(text)

# return: ['It is bad for kids too.',
# "It 's great for kids.",
# 'It is great even for kids.']

print(perturbations)