# Squirrel Tracker


## Introduction
The Squirrel Tracker is an application that allows users to add, update, and view all the known squirrels in Central Park in 2018. 
In this application, [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) data is used. 
<br />

## Description
### Name: Squirrel Tracker
### Management Commands
- Import: A command the can be used to import data in CSV format.
- Export: A command the can be used to export data in CSV format.
### Views
- Homepage
- Map (/map): A view that shows a map that displays the location of the squirrel sightings
- Sightings (/sightings): A view that lists all squirrel sightings with links to view each sighting
- Update (/sightings/<unique-squirrel-id>): A view to update a particular sighting
- Add (/sightings/add): A view to create a new sighting
- Stats (/sightings/stats): A view with general stats about the sightings
<br />

## Main Features
1. **Import and Export data** <br />
Users can use management commands to import or export the data in CSV format. The file path should be specified at the command line after the name of the management command.<br />
- Import:
```sh
python manage.py import_squirrel_data /path/to/file.csv
```
- Export:
```sh
python manage.py export_squirrel_data /path/to/file.csv
```
2. **List of Sightings with links to unique squirrel sighting** <br />
Users can see the sightings of all the known squirrels and their basic features. Also, with links, users can find out the detailed information of a particular sighting.
3. **A Map of the locations of squirrel sightings** <br />
The amazing map displays the location of the squirrel sightings on an [**OpenStreets map**](https://www.openstreetmap.org/about/).
4. **Add a new sighting or update an existing sighting** <br />
Users are allowed to make some changes to the dataset.
5. **Interesting summary and statistics of sightings** <br />
Squirrel Tracker provides some interesting stats to users for fun.
<br />

## Contributors
- Group Name: Zichan & Chengqian, Section 1
- UNIs: [zl2947, cj2666]
