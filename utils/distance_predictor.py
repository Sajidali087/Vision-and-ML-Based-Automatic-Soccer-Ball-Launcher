# distance_predictor.py

import pickle
import numpy as np

class DistancePredictor:
    def __init__(self):
        # Load the regression model and poly transformer
        with open('models/regression_model.pkl', 'rb') as model_file:
            self.regression_model = pickle.load(model_file)
        with open('models/poly_transformer.pkl', 'rb') as poly_file:
            self.poly_transformer = pickle.load(poly_file)

    def predict_distance(self, normalized_pixel_height):
        """
        Predict distance based on the normalized pixel height.
        :param normalized_pixel_height: Normalized height of the detected person in the frame.
        :return: Predicted distance in meters.
        """
        pixel_height = np.array([[normalized_pixel_height]])
        pixel_height_poly = self.poly_transformer.transform(pixel_height)
        predicted_distance = self.regression_model.predict(pixel_height_poly)
        return predicted_distance[0]
