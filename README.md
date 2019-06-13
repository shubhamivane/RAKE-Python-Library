# RAKE Python Library
RAKE(Rapid Automatic Keyword Extraction) is a graph based keyword extraction algorithm. The graph formed is weighted undirected graph in which vertex represents words and edges represents relation. The edge between two words define they both are part of same candidate keyword and the count how many time they appear in same candiate keyword is weight of that edge.

## Preprocessing
The text data which is given input directly or in the form of file is raw data which can not be direclty given to the algorithms so preprocessing is performed in this raw data to make feedable for algorithm. Preprocessing is multi step 
process (steps described below used in this project).
* Sentence Tokenization 
* POS Tagging of sentences
* Removing words based upon their POS Tags
* Lemmatization
* SW Filteration
* Conversion into lower case
<a/>
Now, the words remain are called Candidate Keywords because some of them will be extracted as keyword by the algorithm. 
