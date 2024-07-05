from sentence_transformers import SentenceTransformer, util
import re
from datetime import datetime
from difflib import SequenceMatcher
import pandas as pd

class FormatData:
  def __init__(self) -> None:
    self.wordSimilarityModel = SentenceTransformer("all-MiniLM-L6-v2")

  def format(self, ocrFileData:pd.DataFrame, invoiceNo):
    testData = None

    if self.isOCRIdentifyInvoiceNo(ocrFileData,invoiceNo) == False:
      return (ocrFileData,testData)

    ocrFileData['ocr_similarityDateValue'] = None
    ocrFileData['ocr_similarityOCRValue'] = None
    ocrFileData['ocr_similarityInvoNoValue'] = None

    # Add new Invoice Number patterns into Collection
    self.identifyNewInvoiceNoPatters(invoiceNo)
    i=0
    for ocrFileindex, ocrFileRow in ocrFileData.iterrows():
      ocrDatum = ocrFileRow["ocr_data"]
      for ocrDatum1 in ocrDatum.split(' '):
        if self.isThisInvoiceNo(ocrDatum1,invoiceNo):
          testData = ocrFileindex

      # Add ocr_similarityValue to Date formats
      if self.identify_dates(ocrDatum) == True:
        ocrFileData.at[ocrFileindex, 'ocr_similarityDateValue'] = 0
      else:
        ocrFileData.at[ocrFileindex, 'ocr_similarityDateValue'] = 1

      # Add ocr_similarityValue to Data frame
      ocrFileData.at[ocrFileindex, 'ocr_similarityOCRValue'] = self.similarityValue(str(ocrDatum))

      # Add ocr_similarityValue to Invoice No patterns
      for ocrDatum1 in ocrDatum.split(' '):
        existInvoNoPatterns = open('metaData/invoiceNoPatterns.txt','r')
        for existInvoNoPattern in existInvoNoPatterns:
          if self.invoiceNoPatternMatch(existInvoNoPattern,ocrDatum1) == True:
            ocrFileData.at[ocrFileindex, 'ocr_similarityInvoNoValue'] = 1
            print('found ocr pattern')
          else:
            ocrFileData.at[ocrFileindex, 'ocr_similarityInvoNoValue'] = 0

    return(ocrFileData,testData)
  
  
  def formatInvoice(self,ocrFileData:pd):
    ocrFileData['ocr_similarityDateValue'] = None
    ocrFileData['ocr_similarityOCRValue'] = None
    ocrFileData['ocr_similarityInvoNoValue'] = None

    for ocrFileindex, ocrFileRow in ocrFileData.iterrows():
      ocrDatum = ocrFileRow["ocr_data"]

      # Add ocr_similarityValue to Date formats
      if self.identify_dates(ocrDatum) == True:
        ocrFileData.at[ocrFileindex, 'ocr_similarityDateValue'] = 0
      else:
        ocrFileData.at[ocrFileindex, 'ocr_similarityDateValue'] = 1

      # Add ocr_similarityValue to Data frame
      ocrFileData.at[ocrFileindex, 'ocr_similarityOCRValue'] = self.similarityValue(str(ocrDatum))

      # Add ocr_similarityValue to Invoice No patterns
      for ocrDatum1 in ocrDatum.split(' '):
        existInvoNoPatterns = open('metaData/invoiceNoPatterns.txt','r')
        for existInvoNoPattern in existInvoNoPatterns:
          if self.invoiceNoPatternMatch(existInvoNoPattern,ocrDatum1) == True:
            ocrFileData.at[ocrFileindex, 'ocr_similarityInvoNoValue'] = 1
            print('found ocr pattern')
          else:
            ocrFileData.at[ocrFileindex, 'ocr_similarityInvoNoValue'] = 0

    return(ocrFileData)


  def isThisInvoiceNo(self,ocrDatum,invoiceNo):
    invoiceNo = re.sub(r'\b(\d)+([a-zA-Z])+\b', '', invoiceNo)
    ocrDatum = re.sub(r'\b(\d)+([a-zA-Z])+\b', '', ocrDatum)
    if (SequenceMatcher(None, invoiceNo, ocrDatum).ratio()) > 0.65:
        return True
    else:
      return False

  def isOCRIdentifyInvoiceNo(self, ocrFileData,invoiceNo):
    invoiceNo = re.sub(r'\b(\d)+([a-zA-Z])+\b', '', invoiceNo)

    for ocrValue in ocrFileData["ocr_data"].values:
      for ocrDatum1 in ocrValue.split(' '):
        ocrDatum1 = re.sub(r'\b(\d)+([a-zA-Z])+\b', '', ocrDatum1)
        # print(ocrValue,(SequenceMatcher(None, invoiceNo, ocrValue).ratio()))
        if (SequenceMatcher(None, invoiceNo, ocrDatum1).ratio()) > 0.65:
          print('ocr_value: ',ocrDatum1)
          return True
        else:
          continue
    return False

  def similarityValue(self, word2):
        cosine_scores = []
        for word1 in ["invoice", "no", "number"]:
            embeddings1 = self.wordSimilarityModel.encode(word1, convert_to_tensor=True)
            embeddings2 = self.wordSimilarityModel.encode(word2, convert_to_tensor=True)

            cosine_scores.append(util.cos_sim(embeddings1, embeddings2).item())

        return round(max(cosine_scores),6)

  def identify_dates(self,text):
    date_patterns = [
        r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',   # mm/dd/yyyy
        r'\b\d{1,2}-\d{1,2}-\d{2,4}\b',   # m-d-yy
        r'\b\d{4}\.\d{1,2}\.\d{1,2}\b',   # yyyy.mm.dd
        r'\b\d{1,2} [a-zA-Z]+ \d{2,4}\b'  # dd Month yyyy
    ]

    matches = []
    for pattern in date_patterns:
        matches.extend(re.findall(pattern, text))

    date = False
    date_patterns = ['%m/%d/%Y', '%m-%d-%y', '%Y.%m.%d', '%d %B %Y']
    for match in matches:
        for pattern in date_patterns:
            try:
                date_object = datetime.strptime(match, pattern)
                date = True
                break
            except ValueError:
                date = False

    return date

  def identifyNewInvoiceNoPatters(self,invoNo):
    existInvoNoPatterns = open('metaData/invoiceNoPatterns.txt','r+')
    found = False
    for existInvoNoPattern in existInvoNoPatterns:
      found = self.invoiceNoPatternMatch(existInvoNoPattern, invoNo)
      if found:break

    if found == False:
      pattern = self.patternGen(invoNo)
      existInvoNoPatterns.write('\n'+pattern)
      print('Found new Invoice Number Pattern')

  def patternGen(self,ocrData):
    symbols = "[@_-!#$%^&*()<>?/\|}{~:]"
    regex = []
    for letter in ocrData:
        if letter in symbols:
            regex.append("[{}]".format(letter))
            continue
        try:
            int(letter)
            regex.append("[0-9]")
        except:
            regex.append("[a-zA-Z]")
            # # Also if you wanna check case sensitivity
            # if str(letter).isupper():
            #     regex.append("[A-Z]")
            # else:
            #     regex.append("[a-z]")
    return "".join(regex)

  def invoiceNoPatternMatch(self,pattern,ocrData):
    return(bool(re.match(pattern, ocrData)))