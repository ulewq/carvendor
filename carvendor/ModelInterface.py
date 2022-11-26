import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor

from joblib import dump, load
from scipy import sparse


class ModelInterface:
    # Loading encoder and prediction model
    model = load("saves/model.save")
    enc = load("saves/encoder.save")

    NORMALIZATION_VALUES = [
        (1.0, 1000000.0),
        (400.0, 8285.0),
        (1.0, 1398.0),
        (1915, 2021),
    ]

    CATEGORICAL_COLUMNS = [
        "Colour",
        "Fuel_type",
        "Type",
        "Transmission",
        "Vehicle_model",
        "Drive",
        "Condition",
        "Vehicle_brand",
    ]

    VALUE_COLUMNS = ["Mileage_km", "Displacement_cm3", "Power_HP", "Production_year"]

    # Dictionary to fill with values from website

    def processing(self, vehicle_dict: dict) -> float:
        """Entire processing dataframe and predicting value

        Args:
            vehicle_dict (dict): Dictionary containing car specification

        Returns:
            None
        """

        model_input = pd.DataFrame.from_dict([vehicle_dict])

        model_input = encode_categories(model_input, CATEGORICAL_COLUMNS)
        model_input = standarize_columns(
            model_input, VALUE_COLUMNS, NORMALIZATION_VALUES
        )

        predicted_price = predict_price(model_input)
        return predicted_price

    def encode_categoriesself(
        self, dataframe: pd.DataFrame, cols: list
    ) -> pd.DataFrame:
        """Function for encoding categorical values in dataframe as dummies for prediction model

        Args:
            dataframe (pd.DataFrame): Dataframe with some categorical columns to encode
            cols (list): List of columns in dataset to encode

        Returns:
            pd.DataFrame: Copy of dataframe with encoded categorical values
        """
        codes = enc.transform(dataframe[cols]).toarray()
        feature_names = enc.get_feature_names_out(cols)

        values = dataframe.drop(columns=cols)
        categories = pd.DataFrame(codes, columns=feature_names).astype(int)

        return pd.concat([values, categories.set_index(values.index)], axis=1)

    def standarize_columns(
        self, dataframe: pd.DataFrame, cols: list, params: list = None
    ) -> pd.DataFrame:
        """Function for normalization continous values in dataframe

        Args:
            dataframe (pd.DataFrame): Dataframe with continous values to normalize
            cols (list): List of columns to normalize
            params (list): List of tuples - min-max of continous values of dataset used to train prediction model

        Returns:
            pd.DataFrame: Copy of dataframe with normalized continous values
        """
        new_dataframe = dataframe.copy()

        if params is not None:
            for idx, col in enumerate(cols):
                col_min, col_max = params[idx]
                new_dataframe[col] = (dataframe[col] - col_min) / (col_max - col_min)
            return new_dataframe
        else:
            return None

    def predict_price(self, input: pd.DataFrame) -> float:
        """Function for prediction price of vehicle with given technical specification and features

        Args:
            input pd.Dataframe: Normalized and encoded dataframe with specification of vehicle

        Returns:
            float: Predicted vehicle price
        """
        input = sparse.coo_matrix(input)
        predicted_price = model.predict(input)
        return predicted_price[0]
