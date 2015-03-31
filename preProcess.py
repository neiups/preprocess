__author__ = 'Asanka'

import json
import codecs

class preProcess:
    jsonStr = "output.json"
    detailStr = "details.txt"

    def __init__(self):
        self.jsonFile = open(preProcess.jsonStr, 'r').read()
        self.detailFile = codecs.open(preProcess.detailStr, 'w', 'utf-8')

    def getProperty(self,text,key,delimiter):
        index = 0
        while 1:
            index = text.find(key,index)
            if index > -1:
                if delimiter:
                    list = []
                    end = text.find(delimiter,index + len(key))
                    list.append(text[index + len(key) -1 :end + 1])
                    index = end
                    self.writeToDetailFile(list)
            else:
				break

    def writeToDetailFile(self, list):
        jFile = json.loads(list[0])
        self.detailFile.write(jFile["url"] + ' ,' + jFile["topic"] + '\n')

    def run(self):
        self.getProperty(self.jsonFile, '{', '}\n')


if __name__ == '__main__':
    createDataFile = preProcess()
    createDataFile.run()
