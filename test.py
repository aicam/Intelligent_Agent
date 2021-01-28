import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia(
        language='fa',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)


def print_categorymembers(categorymembers, level=0, max_level=1):
    for c in categorymembers.values():
        print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)


cat = wiki_wiki.page("Category:صنعت")
i = 0
for p in cat.categorymembers.values():
  if i > 10:
      break
  if p.namespace == wikipediaapi.Namespace.CATEGORY:
    # it is category, so you have to make decision
    # if you want to fetch also text from pages that belong
    # to this category
    print(p)
  elif p.namespace == wikipediaapi.Namespace.MAIN:
    # it is page => we can get text
    f = open("./Dataset/Technology/" + str(i) + '.txt', 'w+')
    f.write(p.text)
    f.close()
    print("Saved")
  i += 1