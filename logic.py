import numpy

def calculate_center_coordinate(dataframe):
    """
    Sum all vectors row-wise and normalize the sum

    Returns numpy array
    """
    assert len(dataframe) > 0
    series_center = dataframe.sum(axis=0) * 1 / len(dataframe)

    return series_center.values

def calculate_coordinate_radius(center_coordinate, dataframe):
    """
    Performs two_norm(a-b) row-wise, then finds largest distance
    """
    assert len(center_coordinate) == len(dataframe.columns)

    array_center_coordinate = numpy.array(center_coordinate)
    dataframe_p = dataframe.sub(array_center_coordinate, axis = 'columns')
    array_radii = numpy.linalg.norm(dataframe_p, axis = 1)
    best_radius = max(array_radii)

    return best_radius

def construct_dict_features(list_coordinates, list_times, weight):
    dict_feature = {
        "type" : "Feature",
        "geometry" : None,
        "properties" : None,
    }

    dict_feature["geometry"] = {
        "type" : "LineString",
        "coordinates" : list_coordinates
    }

    dict_feature["properties"] = {
        "times" : list_times,
        # "style" : None
    }
    # dict_feature["properties"]["style"] = {
    #     # "color" : color,
    #     "weight" : weight,
    # }
    return dict_feature

