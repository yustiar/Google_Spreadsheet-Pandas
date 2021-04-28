from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def index(request):

	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	# add credentials to the account
	creds = ServiceAccountCredentials.from_json_keyfile_name('D:/yustiar/01.programming/python/leaflet_tinatar/GIS Desa Tinatar-7e3a8b4c0ac7.json', scope)
	# authorize the clientsheet 
	client = gspread.authorize(creds)
	# get the instance of the Spreadsheet
	sheet = client.open('database')
	# get the first sheet of the Spreadsheet
	sheet_instance = sheet.get_worksheet(0)
	# get all the records of the data
	records_data = sheet_instance.get_all_records()

	records_df = pd.DataFrame.from_dict(records_data)
	alamat_distinct = list(dict.fromkeys(records_df['alamat']))
	alamat_distinct.sort()	
	# for i in range(len(alamat_distinct)):
	# 	alamat_distinct[i] = str(i+1) + ' - '+ str(alamat_distinct[i])

	# alamat_distinct.append('semua SLS')
	ind = []
	for i in range(len(alamat_distinct)):
		ind.append(i+1)
	datazip = zip(ind,alamat_distinct)
	geojson = {
	    "type": "FeatureCollection",
	    "features": [
	    {
	        "type": "Feature",
	        "geometry" : {
	            "type": "Point",
	            "coordinates": [d["longitude"], d["latitude"]],
	            },
	        "properties" : d,
	     } for d in records_data]
	}

	dfcount = records_df['alamat'].value_counts()
	slscountnum = list(dfcount)
	slscounttext = list(dfcount.index.values)

	jumlahsls_info_card = len(list(dict.fromkeys(records_df['alamat'])))
	jumlahkk_info_card = len(list((records_df['nama'])))
	jumlahpddk_info_card = len(list((records_df['nama']))) + sum(list((records_df['jumlahart'])))
	context = {
		'Title' : 'Leaflet Tinatar | Input Data',
		'Heading' : 'Dashboard Data',
		'basemaster' : records_data,
		'alamat_dropdown' : datazip,
		'alamat_only' : alamat_distinct,
		'marker_geojson' : geojson,
		'slscountnum' : slscountnum,
		'slscounttext' : slscounttext,
		'jumlahsls_info_card' : jumlahsls_info_card,
		'jumlahkk_info_card' : jumlahkk_info_card,
		'jumlahpddk_info_card' : jumlahpddk_info_card,
	}

	return render(request, 'index.html', context)