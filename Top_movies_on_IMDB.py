from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top_250_movies_on_imdb'
sheet.append(['s_no','name', 'release year', 'IMDB Rating'])
try:
	source = requests.get('https://www.imdb.com/chart/top/')
	source.raise_for_status()

	soup = BeautifulSoup(source.text,'html.parser')
	
	movies = soup.find('tbody', class_="lister-list").find_all('tr')
	
	for movie in movies:
		name = movie.find('td', class_="titleColumn").a.text
		s_no = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
		year = movie.find('td', class_="titleColumn").span.text.strip('()')
		rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
		print(s_no, name, year, rating)

		sheet.append([s_no, name, year, rating])

except Exception as e:
	print(e)
excel.save('Top_250_movies_on_imdb.xlsx')