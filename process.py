import datetime
import pandas
import tqdm
import xml.etree.ElementTree as ET
import xmltodict

# Ensure GPX/1/1 is the default namespace
ET.register_namespace('', "http://www.topografix.com/GPX/1/1")

def process_time(series):
    """
    Calculates the difference in time relative to the earliest time
    Users: Verify the resulting units
    """
    series_p = pandas.to_datetime(series)
    series_difference = series_p - series_p.min()

    return series_difference

def gpx_to_dict(fname):
    tree = ET.parse(fname)
    root = tree.getroot()
    xml = ET.tostring(root, encoding='unicode')
    dict_gpx = xmltodict.parse(xml)

    return dict_gpx

def process_gpx(dataframe):
    """
    Converts @lat and @lon columns to float
    Normalizes the time column to all start at the same time from the same date
    """
    column_name = 'name'
    column_time = "time"
    columns_floats = ['@lat', '@lon']
    # Synthetic
    column_time_normalised = 'time_normalized'
 
    dataframe_p = dataframe.copy()

    for column in columns_floats:
        dataframe_p.loc[:, column] = dataframe[column].astype('float')

    list_dataframes = []
    groups = dataframe_p.groupby(column_name)
    for group, group_df in tqdm.tqdm(groups, desc='Normalizing times'):
        # TimeDelta + datetime = Timestamp, not JSON Serializable
        group_df.loc[:, column_time_normalised] = process_time(group_df[column_time]) + datetime.datetime.today()
        group_df.loc[:, column_time_normalised] = group_df[column_time_normalised].astype(str) # JSON Serializable
        list_dataframes.append(group_df)
    
    dataframe_p = pandas.concat(list_dataframes)

    return dataframe_p

