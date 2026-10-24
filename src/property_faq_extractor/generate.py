#The only file that invokes the LLM and generates the result
from .schema import FAQ

def generateFAQ(files):
    # Calls LLM passing FAQ on the parse method and returns back the list of FAQs
    return