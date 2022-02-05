# Strava-animation

Makes a simple html plot via folium that normalizes all GPX routes to start at the same time so you can see them go! Intended to be as easy to use as possible. See `out/map.html` for an example.

# Setup

Targets Python 3.
```
pip install -r requirements.txt
```
We always use the latest packages.

# Running

1. Put your strava `.gpx` files in the data folder.
2. Output html will be sent to out folder.

You can modify the main in run.py to fit your needs.

# Dev
We use the "http://www.topografix.com/GPX/1/1" namespace to read gpx files. Always use the latest packages.

# Todo
Add argparse to adjust some parameters like weight, color, etc.

# References

Inspired by a few of these projects.

1. https://medium.com/geospatial-analytics/how-to-animate-strava-gpx-tracks-in-qgis-8a8ca6b58ebc
2. https://towardsdatascience.com/visualize-your-strava-data-on-an-interactive-map-with-python-92c1ce69e91d
3. https://github.com/better-data-science/data-science-for-cycling
4. https://towardsdatascience.com/how-to-make-an-animated-gif-map-in-python-using-folium-and-imageio-91d3fc60d084
5. https://github.com/anitagraser/movingpandas/issues/103

# Demo

