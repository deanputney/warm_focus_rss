import requests
import base64
from bs4 import BeautifulSoup

# Initialize list to store podcast data
podcast_data = []

# Loop through all 11 pages
for page_num in range(1, 12):
	url = f'https://bff.fm/shows/warm-focus/page:{page_num}'
	response = requests.get(url)

	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		broadcast_rows = soup.find_all('li', class_='BroadcastRow')
		for row in broadcast_rows:

			title = row.find('h3', class_='BroadcastRow-title').text
			air_date = row.find('time', class_='BroadcastRow-date').text
			image_url = row.find('img', class_='BroadcastRow-image')['src'].split('?')[0]
			playback_invoker = row.find('button', class_='PlaybackInvoker')
			if playback_invoker:
				encoded_url = playback_invoker.get('data-src')
				mp3_url = base64.b64decode(encoded_url).decode('utf-8')
			else:
				mp3_url = None

			podcast_data.append({'title': title, 'air_date': air_date, 'image_url': image_url, 'mp3_url': mp3_url})

# Create a valid podcast feed using the extracted information
rss_feed = f"""<?xml version='1.0' encoding='UTF-8' ?>\n<rss version='2.0'>\n\t<channel>\n\t\t<title>Warm Focus
Podcast</title>\n\t\t<link>https://bff.fm/shows/warm-focus</link>\n\t\t<description>Podcast feed for Warm Focus show</description>\n"""
for data in podcast_data:
	if data['mp3_url'] is not None:
		rss_feed += f"""\t\t<item>\n\t\t\t<title>{data['title']}</title>\n\t\t\t<pubDate>{data['air_date']}</pubDate>\n\t\t\t<image>{data['image_url']}</image>\n\t\t\t<enclosure
url='{data['mp3_url']}' />\n\t\t</item>\n"""
rss_feed += '</channel>\n</rss>'

# Save the script to a file named 'warm_focus_rss.xml'
with open('warm_focus_rss.xml', 'w') as file:
	file.write(rss_feed)

