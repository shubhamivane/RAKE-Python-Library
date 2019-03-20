'''
    Preprocessing Module

    This Module is for pre-processing the raw text 

'''
# Imports
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
import functools
import nltk
import re
import swfilter

class Preprocess:
    def __init__(self):
        self.idxWords = []
        self.SWTList = ['CC','DT','EX', 'FW','IN','LS','MD','PDT','PRT','PRP','PRP$','POS','RB','RBR','RBS','RP','TO','UH','WDT','WP','WP$','WRB','VB','VBD','VBG','VBN','VBP','VBZ',',','.',':',';','(',')','[',']','{','}','CD']
        self.SWFObj = swfilter.SWFilter()

    def wordNetTags(self,tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN

    def LSTRules(self, prvTag, curTag, word, nxtTag):
        excepWord = ['of']
        if curTag in [',','.',':',';','(',')','[',']','{','}']:
            return False
        if (prvTag == "NNP" or prvTag == "NNPS") and (nxtTag == "NNP" or nxtTag == "NNPS") and word in excepWord:
            return True
        else:
            return False

    def preprocess(self,rawTxt):
        lmtizer = WordNetLemmatizer()
        sentList = sent_tokenize(rawTxt)
        for sent in sentList:
            wordList = nltk.word_tokenize(sent)
            for idx in range(len(wordList)):
                if re.search(r'^[a-zA-Z]+$',wordList[idx]) == None:
                    wordList[idx] = ','
            #print(wordList)
            wordTagTup = nltk.pos_tag(wordList)
            lth = len(wordTagTup)
            ptag = None
            for idx in range(lth):
                word = wordTagTup[idx][0]
                tag = wordTagTup[idx][1]
                if tag in self.SWTList:
                    if idx > 0 and (idx+1) < lth:
                        if self.LSTRules(ptag, tag, word, wordTagTup[idx+1][1]):
                            wordTagTup[idx] = lmtizer.lemmatize(word,self.wordNetTags(tag)).lower()
                        else:
                            wordTagTup[idx] = "-"
                    else:
                        wordTagTup[idx] = "-"
                else:
                    wordTagTup[idx] = lmtizer.lemmatize(word,self.wordNetTags(tag)).lower()
                ptag = tag
            wordTagTup = " ".join(wordTagTup).split("-")
            wordTagTup = list(filter(lambda w: len(w) != 0 and w != " ", wordTagTup))
            self.idxWords.extend(list(map(lambda word: word.strip(),wordTagTup)))
        self.idxWords = self.SWFObj.filterList(self.idxWords)
        return self.idxWords
