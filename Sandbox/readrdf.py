from rdflib import Graph, URIRef
from rdflib.namespace import DC, DCTERMS, FOAF

# Initialize the graph
g = Graph()

# Parse the RDF data from a URL
url = "https://pc.watch.impress.co.jp/data/rss/1.0/pcw/feed.rdf"
g.parse(url, format="xml")

# Attempt to find the title using different common namespaces
title_predicates = [
    DC.title,         # Dublin Core title
    DCTERMS.title,    # Dublin Core Terms title
    FOAF.name,        # FOAF name (sometimes used as a title)
]

title = None

# Search for the title in the RDF graph
for predicate in title_predicates:
    for s, p, o in g.triples((None, predicate, None)):
        title = o
        break
    if title:
        break

# Print the extracted title
if title:
    print("Title:", title)
else:
    print("Title not found.")
