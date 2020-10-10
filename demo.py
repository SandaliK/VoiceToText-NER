from ner import Parser

p = Parser()

p.load_models("models/")

print(p.predict("සීගිරිය සෑදුවේ කවුරුන් විසින්ද?"))

#සීගිරිය පිහිටා ඇත්තේ කොහිද?
#සීගිරිය සෑදුවේ කවුරුන් විසින්ද?