from Movie_Recommendation_System.entity import ModelTrainerConfig
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from Movie_Recommendation_System.logging import logger
import pickle
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def count_vectorizer_model(self):
        data = pd.read_csv(self.config.data_path + "/" + "cleaned_dataset")
        cv = CountVectorizer(max_features= 5000,stop_words="english")
        vector = cv.fit_transform(data['tags']).toarray()
        similarity = cosine_similarity(vector)
        pickle.dump(data, open(self.config.root_dir+"/"+'movie_list.pkl', 'wb'))
        pickle.dump(similarity, open(self.config.root_dir + "/" + 'similarity.pkl', 'wb'))
        logger.info("Pickle file sucessfully downloaded")



