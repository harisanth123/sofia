import wikipedia
#wiki_data=wikipedia.summary("sunny leon", sentences=5)
try:
    wiki_data=wikipedia.summary("sunny leon", sentences=5)
    print(wiki_data)
except wikipedia.exceptions.PageError as e:
    print(e)