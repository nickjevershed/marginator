import json
from shapely.geometry import Point, shape
import csv

def assignMargin(year,inputFile):
	
	with open('{year}.json'.format(year=year)) as f:
		js = json.load(f)

	with open(inputFile,'r') as csvinput:
		with open('output.csv', 'w') as csvoutput:

			reader = csv.DictReader(csvinput, lineterminator='\n')
			headers = reader.fieldnames
			electorate = 'electorate-{year}'.format(year=year)
			incumbent = 'incumbent-{year}'.format(year=year)
			margin = 'margin-{year}'.format(year=year)
			headers = headers + [electorate, incumbent, margin]
			
			writer = csv.DictWriter(csvoutput, headers, lineterminator='\n')
			
			newrows = []

			for row in reader:
				print("Finding", row['location'])
				row[electorate] = 'na'
				row[incumbent] = 'na'
				row[margin] = 'na'
				for area in js['features']:
					print(area['properties']['name'])
					if area['geometry']:
						shapeGeo = shape(area['geometry'])
						point = Point(float(row['lon']),float(row['lat']))
						if shapeGeo.contains(point):
							print(area['properties']['name'])
							row[electorate] = area['properties']['name']
							row[incumbent] = area['properties']['incumbent']
							row[margin] = area['properties']['margin']

				newrows.append(row)			

			writer.writeheader()
			writer.writerows(newrows)

# Example of use
# assignMargin('2016','input.csv')