import paralleldots
paralleldots.set_api_key('hyFtgaNczygoDR7GCMxwns58GGXtZ5JEMTj5og4rFwM')

def ner(text):
    ners = paralleldots.ner(text)
    return ners
