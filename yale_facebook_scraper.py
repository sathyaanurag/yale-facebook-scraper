emails = []
colleges = ['_saybrook', '_branford', '_je', '_stiles', "_morse", '_calhoun', '_berkeley', '_trumbull', '_davenport', '_pierson', '_silliman', '_td']

def scrape():
	for college in colleges:
		with open('html_yale_facebook' + college) as input_file:
			content = input_file.readlines()
			content = content[1].split(' ')

			email_content = []
			for each in content:
				if 'class="email"' in each:
					email_content.append(each)

			for each in email_content:
				beginning = each.find('>') + 1
				end = each.find('<')
				emails.append(each[beginning:end])

def write_to_file(filename):
	outfile = open(filename, 'w')
	for person in emails:
		outfile.write(person)
		outfile.write("\n")

	outfile.close()

scrape()
write_to_file("email_list")
