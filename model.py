from sentence_transformers import SentenceTransformer, util
from CSVfile import CSVfile
from database.database import Database
from database.tbl_ocr_data import tbl_ocr_data


class Model:
    def __init__(self) -> None:
        self.wordSimilarityModel = SentenceTransformer("all-MiniLM-L6-v2")
        self.db = Database()
        self.tblOCRData = tbl_ocr_data()

    def formatDataforTrain(self):
        self.db.connect()
        files = self.tblOCRData.retriveData()
        data = CSVfile.read()
        self.db.close()

    def similarityValue(self, word2):
        cosine_scores = []
        for word1 in ["invoice","no","number"]:
            embeddings1 = self.wordSimilarityModel.encode(word1, convert_to_tensor=True)
            embeddings2 = self.wordSimilarityModel.encode(word2, convert_to_tensor=True)

            cosine_scores.append(util.cos_sim(embeddings1, embeddings2))

        return max(cosine_scores)

    def model(self):
        pass

    def train(self):
        pass
