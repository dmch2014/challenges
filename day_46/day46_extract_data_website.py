# Extra Challenge: Website Data with Pandas
#     Create a code that extracts data from a website. You will extract a
# table from the website. And from that table you will extract columns
# about the data types in Python and their mutability. You will extract
# information from the following website:
# https://en.wikipedia.org/wiki/Python_(programming_language)
# The following table (next page) is what you will extract from the
# website.
import pandas as pd

def extract_data_website():
    reading = pd.read_html("https://en.wikipedia.org/wiki/Python_(programming_language)")
    print(len(reading))
    print(reading[4])
    print("\n")
    table_1= reading[1]
    #print(table_1)
    print("\n")
    data_types = table_1[["Type", "Mutability"]]
    print(data_types)