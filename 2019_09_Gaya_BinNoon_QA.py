import json


with open("2019_09_Gaya_BinNoon_QA.json", "r") as read_file:
    data = json.load(read_file)

## Name of patient
first_name = data["name"][0]["given"]
last_name = data["name"][0]["family"]
name_line = "Name of patient: " + first_name + " " + last_name

## Organization name
org_name = data["managingOrganization"]["display"]
org_line = "Organization name: " + org_name

## Gender
gender = data["gender"]
gender_line = "Gender: " + gender

## Number of conditions
num_con = len(data["conditions"])
num_con_line = "Number of conditions they have: " + str(num_con)

## Conditions list
list_con = data["conditions"]
list_con_line = "List of all conditions: "
for c in list_con:
    list_con_line = list_con_line + "<br/>- " + c

## Define the html output
html_output = '''
<!DOCTYPE html>
<html>
<head>
<title>Results</title>
</head>
<body>
<h1>Patient Results</h1>
<p>''' + name_line + '''</p>
<p>''' + org_line + '''</p>
<p>''' + gender_line + '''</p>
<p>''' + num_con_line + '''</p>
<p>''' + list_con_line + '''</p>
</body>
</html>
'''

read_file.close()


## Actually make the html
output_file = open("patient_output.html", "w+")
output_file.write(html_output)

output_file.close()
