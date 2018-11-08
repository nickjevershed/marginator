# Classify points into Australian federal electorates

A Python function that takes a csv of locations and checks which electorate they fall into, then adds the electorate name, margin from preceding election and incumbent party. The function takes two arguments, year and inputFile location. 

The inputFile should have a row for each location, with a seperate column "lat" and "lon" for each.

## Notes

- Uses geoJSON files simplified to 10% using mapshaper, Visvalingam simplification with "prevent shape removal" selected.
- Electoral divisions 2016 from the ABS: http://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/1270.0.55.003July%202016?OpenDocument
- Electoral divisions 2013 from the AEC: https://www.aec.gov.au/Electorates/gis/gis_datadownload.htm
- Margins and incumbent parties taken from the ABC's election pendulums.
