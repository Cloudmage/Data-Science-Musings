# UK Energy Consumption

## Link to Data

UK Government Power

-[Energy Data](https://www.gov.uk/government/statistics/postcode-level-electricity-estimates-2015-experimental)

OS Map Data

- [OS Map Data](https://www.ordnancesurvey.co.uk/business-government/products/code-point-open)

## Python Modules

Python modules used

- numpy
- matplotlib
- pandas
- geopandas
- pathlib
- plotly
- os
- glob
- pyproj

### Geopandas

If you have a problem installing geopandas check this solution on stack exchange [Geopandas on Stack Exchange](https://gis.stackexchange.com/questions/330840/error-installing-geopandas)

The latest version of Fiona can be found at [Fiona Files](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona)

You may have to install GDAL first which can also be downloaded at this page. Make sure its the version of GDAL that relates to the version of Python you are using.

pip install path/to/GDALnnnnn.whl
pip install path/to/Fionannnnn.whl

where nnnnn = the rest of the filename

So for Python 3.9.1, I have used the files listed below:

- GDAL-3.2.2-cp39-cp39-win_amd64.whl
- Fiona-1.8.19-cp39-cp39-win_amd64.whl
