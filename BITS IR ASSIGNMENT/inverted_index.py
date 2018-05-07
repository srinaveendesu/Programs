import unicodedata
import os
import docx
import sys
import re
import nltk
import argparse

parser = argparse.ArgumentParser(description='Inverted-Index Builder ( Positional)',
                                formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                )
parser.add_argument("-l", "--library", help="NLTK library will be used for stemming and tokenization if set to 1 otherwise case-folding, length normalization and stopwords are used for preprocessing\nNOTE: Need active internet connection to download data for NLTK",\
                    default = 0 )

parser.add_argument("-o", "--output", help="Print Search query output from document files.If set to 1 matching content will be returned from docs",\
                    default = 0)

parser.add_argument("-q", "--searchquery", help="Query to be searched for.If not specified default search queries will be used",\
                    default = "")

parser.add_argument("-d", "--invertedindex", help="Print complete list of inverted index",\
                    default = 0)


args = parser.parse_args()
nltk_library = args.library
query_match_output = args.output
search_query = args.searchquery
inverted_ind = args.invertedindex

#Taken from nltk
#first time downloads the library to local machine
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
STOPWORDS = frozenset(['i', 'me', 'my', 'myself', 'we', 'our', 'ours',\
                         'ourselves', 'you', "you're", "you've", "you'll",\
                         "you'd", 'your', 'yours', 'yourself', 'yourselves',\
                         'he', 'him', 'his', 'himself', 'she', "she's",\
                         'her', 'hers', 'herself', 'it', "it's", 'its',\
                         'itself', 'they', 'them', 'their', 'theirs',\
                         'themselves', 'what', 'which', 'who', 'whom',\
                         'this', 'that', "that'll", 'these', 'those', 'am',\
                         'is', 'are', 'was', 'were', 'be', 'been', 'being',\
                         'have', 'has', 'had', 'having', 'do', 'does',\
                         'did', 'doing', 'a', 'an', 'the', 'and', 'but',\
                         'if', 'or', 'because', 'as', 'until', 'while', \
                         'of', 'at', 'by', 'for', 'with', 'about', 'against',\
                         'between', 'into', 'through', 'during', 'before',\
                         'after', 'above', 'below', 'to', 'from', 'up', \
                         'down', 'in', 'out', 'on', 'off', 'over', 'under',\
                         'again', 'further', 'then', 'once', 'here', 'there',\
                         'when', 'where', 'why', 'how', 'all', 'any', 'both',
                         'each', 'few', 'more', 'most', 'other', 'some',\
                         'such', 'no', 'nor', 'not', 'only', 'own', 'same',\
                         'so', 'than', 'too', 'very', 's', 't', 'can', \
                         'will', 'just', 'don', "don't", 'should', \
                         "should've", 'now', 'd', 'll', 'm', 'o', 're',\
                         've', 'y', 'ain', 'aren', "aren't", 'couldn',\
                         "couldn't", 'didn', "didn't", 'doesn', "doesn't",\
                         'hadn', "hadn't", 'hasn', "hasn't", 'haven',\
                         "haven't", 'isn', "isn't", 'ma', 'mightn', \
                         "mightn't", 'mustn', "mustn't", 'needn', "needn't",\
                         'shan', "shan't", 'shouldn', "shouldn't", 'wasn',\
                         "wasn't", 'weren', "weren't", 'won', "won't", \
                         'wouldn', "wouldn't"])


def getText(filename):
    """
       Desc       : This function allows to read data from docx file
                    and return as text
       Parameters : <filename> -> Name of the file
       Return     : string containing text from file
    """
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def tokenizer(text):
    """
       Desc       : This function tokenizes the text from doc using NLTK
                    library
       Parameters : <text> -> Text content of each doc
       Return     : List of tokenized words
    """
    text = re.sub("[^a-zA-Z]+", " ", text)
    #To be used when running for first time to download tokenization
    #data from NLTK library
    #nltk.download('punkt')
    tokens = nltk.tokenize.word_tokenize(text)
    return tokens        

def preprocessor_lib(text):
    """
       Desc       : This function preprocesses text from doc using NLTK LIB
       Parameters : <text> -> Text content of each doc
       Return     : str containing the preprocessed text
    """
    tokens = tokenizer(text)
    lemmatizer  = nltk.stem.WordNetLemmatizer()
    stemmer = nltk.stem.porter.PorterStemmer()
    stopwords = nltk.corpus.stopwords.words('english')
    new_text = ""
    for token in tokens:
        token = token.lower()
        if token not in stopwords:
            token = lemmatizer.lemmatize(token)
            new_text += stemmer.stem(token)
            new_text += " "
        
    return new_text

def preprocessor_manual(text):
    """
       Desc       : This function preprocesses text manually from doc 
       Parameters : <text> -> Text content of each doc
       Return     : List of Preprocessed words
    """
    word_list = []
    wcurrent = []
    windex = None
    WORD_LENGTH = 1

    for i, c in enumerate(text):
        if c.isalnum():
            wcurrent.append(c)
            windex = i
        elif wcurrent:
            word = u''.join(wcurrent)
            word_list.append((windex - len(word) + 1, word))
            wcurrent = []

    if wcurrent:
        word = u''.join(wcurrent)
        word_list.append((windex - len(word) + 1, word))

    #CASE FOLDING 
    normalized_words = []
    for index, word in word_list:
        words_casefolded = word.lower()
        normalized_words.append((index, words_casefolded))

    #Stopwords Removal
    cleaned_words = []
    for index, word in normalized_words:
        if len(word) < WORD_LENGTH or word in STOPWORDS:
            continue
        cleaned_words.append((index, word))

    return cleaned_words


def preprocessor_type(text):
    """
       Desc       : This function selects the type of preprocessing
                    Manual or NLTK library 
       Parameters : <text>   -> Text content of each doc
                    <flag>   Default = 0 For running through manual
                                       1 For running through NLTK   
       Return     : List of Preprocessed words and their indexes
    """
    if nltk_library:
        text = preprocessor_lib(text)
    words = preprocessor_manual(text)
    return words

def inverted_index(text):
    """
       Desc       : This function creats an Inverted-Index of the
                    Document Specified
                    Term-Index format (positional)
                    {term1: [pos1, pos2, pos3...],                        
                     term2: [pos1, pos2, pos3...],
                     ...
                    }
                    Manual or NLTK library 
       Parameters : <text>   -> Text content of each doc
                    <flag>   Default = 0 For running through manual
                                       1 For running through NLTK   
       Return     : Dictionary of lists
    """
    
    inverted = {}

    for index, word in preprocessor_type(text):
        locations = inverted.setdefault(word, [])
        locations.append(index)

    return inverted

def inverted_index_add(inverted, doc_id, doc_index):
    """
       Desc       : This function creats an Inverted-Index of the
                    Document Specified
                    Inverted-Index format (positional)
                    {term1: {doc1: [pos1, pos2, pos3...],
                             doc2: [pos1, pos2, pos3...]
                            },
                     term2: {doc1: [pos1, pos2, pos3...],
                             doc2: [pos1, pos2, pos3...]
                            },...
                    }
                    Manual or NLTK library 
       Parameters : <text>   -> Text content of each doc
                    <flag>   Default = 0 For running through manual
                                       1 For running through NLTK   
       Return     : Positional inverted index as given above
    """
    
    for word, locations in doc_index.items():
        indices = inverted.setdefault(word, {})
        indices[doc_id] = locations
    return inverted

def search(inverted, query):
    """
       Desc       : This function selects the type of preprocessing
                    Manual or NLTK library 
       Parameters : <inverted>   -> Inverted index of all docs
                    <query>      -> Query to be searched
       Return     : Return docs containing the search query
    """
    import functools
    words = [word for _, word in preprocessor_type(query) if word in inverted]
    results = [set(inverted[word].keys()) for word in words]
    #print (results)
    for _, word in preprocessor_type(query):

        m = re.search(r"or|OR|Or|oR",  query)
        if m:
            break
        if word not in inverted:
            results.append(set({}))
            #print (results)
    return functools.reduce(lambda x, y: x & y, results) if results else []

def main():
    """
       Desc       : This function processes the docs in dataset and passes
                    data to other functions for preprocessing.The funciton
                    also passes the search query and fetches appropriate
                    docs.Finally from the searched docs prints the documents
                    if users wishes to print data from doc as well.
                    
       Parameters : None
       Return     : None
    """
    list_doc = os.listdir("./Dataset")
    documents = {}
    for i,doc in enumerate(list_doc):
        doc_loc = "./Dataset/" + str(doc)
        file_doc = getText(doc_loc)
        documents['doc'+ str(i+1)] = file_doc
    
    # Build Inverted-Index for documents
    inverted = {}
    
    for doc_id, text in documents.items():
        doc_index = inverted_index(text)
        inverted_index_add(inverted, doc_id, doc_index)

    # Print Inverted-Index
    if inverted_ind:
        for word, doc_locations in inverted.items():
            print (word,'->' , doc_locations)
        
    print ('TOTAL No. of Dict Terms Generated ==> ', len(inverted))

    # Search something and print results
    queries = ['lab', 'project and lead and american', 'radiology center',\
               'mike or batch','computing and mike' ]
    if search_query:
        queries.append(search_query)
    print (queries)
    for query in queries:
        result_docs = search(inverted, query)
        if len(result_docs):  
            print ("Search for '%s': %r" % (query, result_docs))
            if query_match_output:
                for _, word in preprocessor_type(query):
                    def extract_text(doc, index): 
                        return documents[doc][index:index+20].replace('\n', ' ')

                    for doc in result_docs:
                        try:
                            for index in inverted[word][doc]:
                                print ('\t- %s...' % extract_text(doc, index))
                        except:
                            pass
        else:
            print ("Search for '%s': %r" % (query, 'No matching Docs'),list(result_docs))
        print

if __name__ == '__main__':
    print("-----------------------------")
    print("|    BIS IR ASSIGNMENT      |")
    print("|    2017HT12532            |")
    print("|    DESU SRINAVEEN         |")
    print("-----------------------------")    
    main()

    
