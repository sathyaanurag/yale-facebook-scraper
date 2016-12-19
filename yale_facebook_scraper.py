with open('html_yale_facebook') as f:
	content = f.readlines()
	content = content[1].split(' ')

	email_content = []
	for each in content:
		if 'class="email"' in each:
			email_content.append(each)

	emails = []

	for each in email_content:
		beginning = each.find('>') + 1
		end = each.find('<')
		emails.append(each[beginning:end])

	print emails
