import logic
import process

import folium
import folium.plugins
import itertools
import pandas
import pathlib
import tqdm

def generate_html_map(dataframe, column_lat, column_lon, column_time, size_zoom = 11):
    """
    Calls the Folium map to plot lat, lon data centered about a calculated coordinate.

    Note: Assumes the Earth is flat
    """
    center_coordinate = logic.calculate_center_coordinate(dataframe[[column_lat, column_lon]])
    # radius = logic.calculate_coordinate_radius(center_coordinate, window)
    route_map = folium.Map(
        location=center_coordinate,
        zoom_start=size_zoom,
        zoom_control=False,
        tiles= "Stamen Terrain", #"Stamen Toner", #'CartoDBPositron', 
        width=1024,
        height=600
    )
    
    list_dict_features = []
    groups = dataframe.groupby('name')
    for group, group_df in tqdm.tqdm(groups, desc='TimeStamped widgets'):

        dict_features = logic.construct_dict_features(
            group_df[[column_lon, column_lat]].to_records(index=False).tolist(), 
            group_df[column_time].tolist(),
            weight = 5)
        list_dict_features.append(dict_features)

    folium.plugins.TimestampedGeoJson(
        {
            "type": "FeatureCollection",
            "features": list_dict_features,
        },
        period="PT1M",
        add_last_point=True,
        transition_time=1000,
        time_slider_drag_update=True
    ).add_to(route_map)

    route_map.save(outfile= str(path_out / "map.html"))

    return

if __name__ == "__main__":

    path_dir = pathlib.Path.cwd() / 'data'
    path_out = pathlib.Path.cwd() / 'out'
    path_out.mkdir(parents=True, exist_ok=True)
    files_gpx = path_dir.glob("*")

    # Read gpx data as a dataframe
    iter_dataframes = []
    for file in tqdm.tqdm(files_gpx, desc = 'GPX as dataframe'):
        # We know the structure by observing an xml
        try:
            dict_gpx = process.gpx_to_dict(file)['gpx']['trk']
            name = dict_gpx['name'] + "_" + file.stem
            list_dicts_gpx = dict_gpx['trkseg']['trkpt']

            dataframe = pandas.DataFrame(list_dicts_gpx)
            dataframe.loc[:, 'name'] = name
            iter_dataframes = itertools.chain(iter_dataframes, [dataframe]) # no longer list

        except KeyError as exception:
            print(exception)

    gpx = (
        pandas.concat(iter_dataframes)
        .pipe(process.process_gpx)
    )

    generate_html_map(gpx, '@lat', '@lon', 'time_normalized', size_zoom = 11)