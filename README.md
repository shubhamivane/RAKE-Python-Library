# RAKE Python Library
RAKE(Rapid Automatic Keyword Extraction) is a graph based keyword extraction algorithm. The graph formed is weighted undirected graph in which vertex represents words and edges represents relation. The edge between two words define they both are part of same candidate keyword and the count how many time they appear in same candiate keyword is weight of that edge. Score is calculated for every vertex using its degree and weight of the connecting edges.

## Preprocessing
The text data which is given input directly or in the form of file is raw data which can not be direclty given to the algorithm so preprocessing is performed in this raw data to make feedable for algorithm. Preprocessing is multi step 
process (steps described below used in this project).
* Sentence Tokenization 
* POS Tagging of sentences
* Removing words based upon their POS Tags
* Lemmatization
* SW Filteration
* Conversion into lower case
<a/>
Now, the words remain are called Candidate Keywords because some of them will be extracted as keyword by the algorithm. 

## Postprocessing
In postprocessing step, score for each candidate word is calculated. Now, the candidate keywords are sorted based upon their score and top 40%(this value is not fixed it can be changed) candidate keywords are final extracted keywords.

## Usage
* Install dependencies using 
```python
  pip install -r reuirement.txt
```
* Then, import rake and pass file path as argument to the rake function which return list of extracted keywords.. 
```python
  import rake
  rake = rake.rake(file_path)
```
