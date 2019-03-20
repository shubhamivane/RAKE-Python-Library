import sys
import readFile
import preprocessing
import postprocessing

def rake(filePath):
	'''
		Main function of our project
		params:
			filePath | string     : Path of file which we have to read.
		
		return:
			keywordsList | string : List of index keywords. 
	'''
	rawText = readFile.readFile(filePath)
	preObj = preprocessing.Preprocess()
	candidateKeywordList = preObj.preprocess(rawText)
	indexKeywordList = postprocessing.postprocess(candidateKeywordList)
	return indexKeywordList

if __name__ == "__main__":
#	rake(filePath)
	rake("AP830325-0143")