import os
from Movie_Recommendation_System.logging import logger
from Movie_Recommendation_System.entity import DataTransformationConfig
import ast
from nltk.stem.porter import PorterStemmer
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def Genres_Convertor(self,obj):
        genre_arr = []
        for i in ast.literal_eval(obj):
            genre_arr.append(i["name"])
        return genre_arr

    def Cast_Convertor(self,obj):
        cast_arr = []
        counter = 0
        for i in ast.literal_eval(obj):
            if counter != 3:
                cast_arr.append(i["name"])
                counter += 1
            else:
                break
        return cast_arr

    def fetch_crew(self,obj):
        arr = []
        for i in ast.literal_eval(obj):
            if i["job"] == "Director":
                arr.append(i["name"])
                break
        return arr

    def file_extraction(self):
        file_list = []
        files = os.listdir(self.config.data_path)
        for file in files:
            file_list.append(file)
        return file_list
    def read_csv(self,file_list):
        movies_df = pd.read_csv(self.config.data_path+"/"+file_list[1])
        credit_df = pd.read_csv(self.config.data_path+"/"+file_list[0])
        df = movies_df.merge(credit_df, on="title")
        return df
    def csv_data_transformation(self,df):
        df = df[["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]]
        df.dropna(inplace=True)
        df["genres"] = df["genres"].apply(self.Genres_Convertor)
        df["keywords"] = df["keywords"].apply(self.Genres_Convertor)
        df["cast"] = df["cast"].apply(self.Cast_Convertor)
        df["crew"] = df["crew"].apply(self.fetch_crew)
        df["overview"] = df["overview"].apply(lambda x: x.split())
        df["genres"] = df["genres"].apply(lambda x: [i.replace(" ", "") for i in x])
        df["keywords"] = df["keywords"].apply(lambda x: [i.replace(" ", "") for i in x])
        df["cast"] = df["cast"].apply(lambda x: [i.replace(" ", "") for i in x])
        df["crew"] = df["crew"].apply(lambda x: [i.replace(" ", "") for i in x])
        df["tags"] = df["overview"] + df["genres"] + df["keywords"] + df["cast"] + df["crew"]
        new_df = df[["movie_id", "title", "tags"]]
        new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))
        new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())
        return new_df

    def store_dataframe_as_csv(self,df):
        file_path = os.path.join(self.config.root_dir+"/"+"cleaned_dataset")
        df.to_csv(file_path, index=False)











