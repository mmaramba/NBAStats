from bs4 import BeautifulSoup
import pandas as pd
import csv
import requests

baseURL = 'https://www.basketball-reference.com/play-index/draft_finder.cgi?request=1&year_min=&year_max=&round_min=1&round_max=2&pick_overall_min=1&pick_overall_max=60&franch_id=&college_id=0&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=year_id&order_by_asc=&offset='
table_len = 100  # length of table for each page
num_pages = 29

# URLs to scrape
url_list = [baseURL + str(num*table_len) for num in range(num_pages)]

# CSV File setup
draft_csv = open("nba_draft.csv", "w")
draft_csv.write("Year,Rd,Pk,Tm,Player,Pos,College,G,MP,PTS,TRB,AST,STL,BLK,FG%,3P%,FT%,WS,WS/48\n")
writer = csv.writer(draft_csv)

# Go through the tables, find stats, store in CSV file
for url in url_list:
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")

	table = soup.find("table", { "id" : "stats" })
	body = table.find("tbody")
	rows = body.findAll("tr")

	for row in rows:

		# Player name
		name_td = row.find("td", { "data-stat" : "player" })
		if not name_td:
			continue
		name = name_td.find("a")
		if not name:
			continue
		
		# Draft info
		year = row.find("td", { "data-stat" : "year_id" })
		rd = row.find("td", { "data-stat" : "round" })
		pick = row.find("td", { "data-stat" : "pick_overall" })
		team = row.find("td", { "data-stat" : "team_id" })

		# Player info
		position = row.find("td", { "data-stat" : "pos" })
		college = row.find("td", { "data-stat" : "college" })
		games = row.find("td", { "data-stat" : "g" })

		# Per game stats
		mins = row.find("td", { "data-stat" : "mp_per_g" })
		points = row.find("td", { "data-stat" : "pts_per_g" })
		rebs = row.find("td", { "data-stat" : "trb_per_g" })
		assists = row.find("td", { "data-stat" : "ast_per_g" })
		steals = row.find("td", { "data-stat" : "stl_per_g" })
		blocks = row.find("td", { "data-stat" : "blk_per_g" })

		# Shooting percentages
		fg_pct = row.find("td", { "data-stat" : "fg_pct" })
		fg3_pct = row.find("td", { "data-stat" : "fg3_pct" })
		ft_pct = row.find("td", { "data-stat" : "ft_pct" })

		# Advanced stats
		ws = row.find("td", { "data-stat" : "ws" })
		ws_per_48 = row.find("td", { "data-stat" : "ws_per_48" })

		writer.writerow([year.text, rd.text, pick.text, team.text, name.text,
			position.text, college.text, games.text, mins.text, points.text, rebs.text, assists.text,
			steals.text, blocks.text, fg_pct.text, fg3_pct.text, ft_pct.text, ws.text, ws_per_48.text])
		