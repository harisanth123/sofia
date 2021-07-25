>>> wikipedia.summary("Mercury")
Traceback (most recent call last):
...
wikipedia.exceptions.DisambiguationError: "Mercury" may refer to:
Mercury (mythology)
Mercury (planet)
Mercury (element)

>>> try:
...     mercury = wikipedia.summary("Mercury")
... except wikipedia.exceptions.DisambiguationError as e:
...     print e.options
...
[u'Mercury (mythology)', u'Mercury (planet)', u'Mercury (element)', u'Mercury, Nevada', ...]

>>> wikipedia.summary("zvv")
Traceback (most recent call last):
...
wikipedia.exceptions.PageError: "zvv" does not match any pages. Try another query!


wiki_data = wikipedia.summary(info, sentences=5)
                print(wiki_data)
                speak(wiki_data)