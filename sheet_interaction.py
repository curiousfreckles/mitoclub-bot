def get_everything():
	RANGE_NAME = '!A1:E'
	store = file.Storage('token.json')
	creds = store.get()
	store = file.Storage('token.json')
	service = build('sheets', 'v4', http=creds.authorize(Http()))
	result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
	numRows = result.get('values') if result.get('values') is not None else "Wow, such empty!"
	everything = "\n".join(["\t".join(i) for i in numRows])
	return everything