
import logging
import time

class p1:
    def __init__(self) -> None:
        pass
    def details(self):
        print("Your in the P1")
        return 1
     
class p2:
    def details(self):
        print("here is class p2")        
        return 0
class project(p1,p2):
  
    def func(self, name, sub, mark):
        print("Here in the project class test")
        print(name)
        print(sub)
        print(mark)
        
    def func1(self, string):
        print("Function func1 {}".format(string))

meth = project()
meth.details()
var = meth.details()
print(var)
meth.func("Sat","math", 100)
meth.func1("World")


"""
class Car:
    value=0.5
    def __init__(self,company, model, price ):
        self.company=company
        self.model=model
        self.price=price
    def funcCarDesign(self):
        print("Get the details of vehicle value")

class Bike(Car):
    value=0.1
    def __init__(self, company, model, price, fuel):
        super().__init__(company, model, price)
        self.fuel=fuel    
    pass

vehicle1= Car("Tata","Taigo",800000)
print(Car.__dict__)
print(vehicle1.__dict__)
print(vehicle1.model)
print(vehicle1.price)
vehicle2={'Company':'MB', 'model':'xxx','price':9000000}
vehicle1.funcCarDesign() #both are the same
Car.funcCarDesign(vehicle1) #same as above statement
#Car.funcCarDesign(vehicle2)
vehicle2=Car(vehicle2['Company'],vehicle2['model'],vehicle2['price'])
print(vehicle2.__dict__)
print(vehicle2.model)
print(vehicle2.price)
Car.funcCarDesign(vehicle2)

veh3=Bike('honda','Sport',100000, 'petrol')
print(veh3.company)
print(veh3.model)
print(veh3.price)
print(veh3.value)
print(veh3.fuel)
#print(help(vehicle1))


#from pypdf import PdfReader
#import pdfplumber # to Find the table
#import fitz
import re

print("Hello Pro")
a=6; b=7
print("value of a {} and value of b {}".format(a,b))
c= "string1"
d= "string2"
print("print the details of c {} and d {}".format(c,d))
print("HI {} {} {other}".format("dear", "whats", other= "up"))

#str1= "Satish, Vijay, Akhade"
#a,b,c=map(str1, input().split(','))
#print("value a {} b {} c {}".format(a,b,c))

a=7
if(a>5):
    print("vslue of a more than 5 i.e.",a)
else:
    print("value of a less than 5 i.e.",a) 
a=5+6j
print(a, "is of type", type(a))
s = "string value"
s[1:]
print(s[8: 10])
a = [10,20.57, "hello"] #List
print("list a=",a)
t = (10,20.57, "hello") # tupple-> data type inside the tuple can not be change
print("tuple t=", t) 

b={10,20,30,40,50}  #set un-order value and can not assigned index
print("set order", b)
print(40 in b)
 
d ={'a': "string1", 'b': "string2"} # dictionary
print(d['a'])
print(d['b']) 
print(d['a'] is d['a'])


num=int(input("Enter number value  "))

#check the Prime number 

if (num > 1):
    print("its valid number")
    for x in range(2,num):
        if (num % x)==0:
            print(num, "is not prime number")
            print("index", x)
            break;
    else:
        print("this is the prime number",num)
else:
    print("it's not valid number")

#l = [10,20,30,40,50,60]
list = ["abc","lcm","pqr","stv"]
for x in list:
    print(x)
list.append("str")
list.insert(1,"xyz")
for x in list:
    print(x)
#####################################################

def is_prime(n):

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def classify_number(n):

    classification = {
        'Natural': False,
        'Prime': False,
        'Whole': False,
        'Even': False,
        'Odd': False
    }
    
    # Check if the number is a Natural number (positive integer)
    if n > 0:
        classification['Natural'] = True
    
    # Check if the number is a Whole number (non-negative integer)
    if n >= 0:
        classification['Whole'] = True
    
    # Check if the number is Even or Odd
    if n % 2 == 0:
        classification['Even'] = True
    else:
        classification['Odd'] = True
    
    # Check if the number is Prime
    if is_prime(n):
        classification['Prime'] = True
    
    return classification

# Test the function with an example
n= int(input("Enter the any Number "))
classification = classify_number(n)
print(f"Number {n} Classification: {classification}")

#New data type 

string1 =  "dockerid fskldfdsk imsgr byteof jkfldlks"

list1 = string1.split(' ')

print (list1)
print (list1[0])

list1_0 = [1,2,3,4,5,6,7,8,9,0,2,2,3,3,3,3]

print(list1_0[0:6:2])

#set does not include dupilcate data type

#s = "Hello india how are you ".rfind("you")
#print(s)

#video= 2:47
#Dictionary

dict = {"age" : 18, "name":'hello', "game":'cirecket' }
 
print(dict.items())
print(dict.keys())
print(dict.clear())
del dict
print(dict)

#video 4:38

class name:
    def your_name(self):
        print("You have to enter your name")
    def middle_name(self):
        print("enter ur father name")
        
    def suranme(self):
        print("put your last name")
        
vsr = name()
vsr.your_name()
vsr.suranme()
vsr.your_name()

class car:
    def __init__(self, honda, tata, mb, tesla):
        self.honda=honda
        self.tata=tata
        self.mb=mb
        self.tesla=tesla 
        
    def provide_car_details(self):
        print("My tata car is", self.tata)
        print("My honda car is", self.honda)
        print("my mb car is",self.mb)
        print("my tesla car is", self.tesla)
        
my_car=car("city","taigo","a400","s007")
my_car.provide_car_details()       

# Regex expersion
strng= "age of chintu 34, agae of pintu 50"
age = re.findall(r'\d{1,3}',strng)
print(age)

import matplotlib.pyplot as plt

#------------------------------------------------Create tsble ---------------------
import pandas as pd

# Create a dictionary with data for the table
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grapes', 'Honeydew', 'Kiwi', 'Lemon'],
    'C': [10.2, 15.3, 8.5, 12.1, 9.7, 11.0, 13.8, 7.5, 14.2, 6.8],
    'D': ['Red', 'Yellow', 'Red', 'Brown', 'Purple', 'Green', 'Purple', 'Green', 'Brown', 'Yellow']
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

#----------------------------------------------Generste the pdf file
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Create a dictionary with data for the table
data = {
    'Sr.No.': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'ID': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grapes', 'Honeydew', 'Kiwi', 'Lemon'],
    'Result': [10.2, 15.3, 8.5, 12.1, 9.7, 11.0, 13.8, 7.5, 14.2, 6.8],
    'Comment': ['Red', 'Yellow', 'Red', 'Brown', 'Purple', 'Green', 'Purple', 'Green', 'Brown', 'Yellow']
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a PDF file and add a table to it
pdf_filename = "table_example.pdf"
document = SimpleDocTemplate(pdf_filename, pagesize=letter)
table_data = [df.columns[:,].values.astype(str)] + df.values.tolist()
table = Table(table_data)

# Define table style
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Table body background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Table grid lines
])

table.setStyle(style)

# Build the PDF document
elements = [table]
document.build(elements)

print(f"Table saved to {pdf_filename}")


#-------------------------------------------------with email generation---------------

import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import tempfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Create a dictionary with data for the table
data = {
    'Sr.N.': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'ID': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grapes', 'Honeydew', 'Kiwi', 'Lemon'],
    'Result': [10.2, 15.3, 8.5, 12.1, 9.7, 11.0, 13.8, 7.5, 14.2, 6.8],
    'Comment': ['Red', 'Yellow', 'Red', 'Brown', 'Purple', 'Green', 'Purple', 'Green', 'Brown', 'Yellow']
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a PDF file and add a table to it
pdf_filename = "table_example_tmp.pdf"
document = SimpleDocTemplate(pdf_filename, pagesize=letter)
table_data = [df.columns[:,].values.astype(str)] + df.values.tolist()
table = Table(table_data)

# Define table style
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Table body background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Table grid lines
])

table.setStyle(style)

# Build the PDF document
elements = [table]
document.build(elements)

# Compose an email with the PDF attachment
email_from = ""
email_to = ""
email_subject = "Table PDF Attachment"

msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = email_to
msg['Subject'] = email_subject

body = "Please find the attached table in PDF format."
msg.attach(MIMEText(body, 'plain'))

attachment = open(pdf_filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename= {pdf_filename}")
msg.attach(part)

# Send the email
try:
    smtp_server = "smtp.gmail.com"  # Update SMTP server based on your email provider
    smtp_port = 587  # SMTP port for TLS
    smtp_username = ""
    smtp_password = ""

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(email_from, email_to, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print(f"Email sending failed: {str(e)}")

# Clean up temporary files
#import os
#os.remove(pdf_filename)

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Create a dictionary with data for the table
data = {
    'Sr.No.': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'ID': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grapes', 'Honeydew', 'Kiwi', 'Lemon'],
    'Result': [10.2, 15.3, 8.5, 12.1, 9.7, 11.0, 13.8, 7.5, 14.2, 6.8],
    'Comment': ['Red', 'Yellow', 'Red', 'Brown', 'Purple', 'Green', 'Purple', 'Green', 'Brown', 'Yellow']
}

class test:
    def tc_execution_fun(self):
        a,b=100,200
        match(a,b):
            case(100, 100):
                print("case number first")
                
            case(100, 200):
                print("case number second")
                
            case(100, 300):
                print("case number 4th")
                
            case(100,400):
                print("case number 5th")
                            
        print("Expected result")

p1=test()
p1.tc_execution_fun()

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Create a PDF file and add a table to it
pdf_filename = "table_example.pdf"
document = SimpleDocTemplate(pdf_filename, pagesize=letter)
table_data = [df.columns[:,].values.astype(str)] + df.values.tolist()
table = Table(table_data)

# Define table style
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Table body background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Table grid lines
])

table.setStyle(style)

# Build the PDF document
elements = [table]
document.build(elements)

print(f"Table saved to {pdf_filename}")

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os

comnd = os.popen('ls -al')
print(comnd.read())
print(comnd.close())

#************************
import subprocess
subprocess.check_call('commnd < (another command)', shell=True, executable= '/bin/bash')

##---------------------------------Bash command in python------#

import subprocess

# Define the Bash command you want to run
bash_command = "ls -l"

# Run the Bash command and capture the output (universal_newline used to store output in the string )
try:
    result = subprocess.check_output(bash_command, shell=True, universal_newlines=True)
    print("Bash Command Output:")
    print(result)
except subprocess.CalledProcessError as e:
    print("Error executing Bash command:", e)

###-------------------------------Few Bash command and respective output stored in list------

import subprocess

# List of Bash commands to execute
bash_commands = ["ls -l", "echo $PWD", "last"]

# Initialize an empty list to store the outputs
outputs = []

# Iterate through the list of commands and execute them
for command in bash_commands:
    try:
        result = subprocess.check_output(command, shell=True, universal_newlines=True)
        outputs.append(result.strip())  # Append the output to the list after stripping any trailing newline characters
    except subprocess.CalledProcessError as e:
        outputs.append(f"Error executing Bash command: {e}")

# Print the outputs
for i, output in enumerate(outputs):
    print(f"Output for command {i + 1}:\n{output}\n")

##--------------------------------Bash command with pdf file ---------------------------------------------------------------------

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import subprocess

# Define the Bash commands and their expected outputs
bash_commands = [
    {"command": "ls -l", "expected_output": "expected ls -l output goes here"},
    {"command": "echo $PWD", "expected_output": "expected echo $PWD output goes here"},
    {"command": "last", "expected_output": "expected last output goes here"}
]

# Create a PDF file
pdf_filename = "bash_commands_output.pdf"
document = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Create data for the table
data = [["Bash Command", "Expected Output", "Actual Output", "Result"]]

for command_info in bash_commands:
    command = command_info["command"]
    expected_output = command_info["expected_output"]
    
    try:
        actual_output = subprocess.check_output(command, shell=True, text=True).strip()
        result = "Pass" if actual_output == expected_output else "Fail"
    except subprocess.CalledProcessError as e:
        actual_output = str(e)
        result = "Fail"

    data.append([command, expected_output, actual_output, result])

# Create a table
table = Table(data)

# Define table style
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Table body background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Table grid lines
])

table.setStyle(style)

# Build the PDF document
elements = [table]
document.build(elements)

print(f"Table saved to {pdf_filename}")


##_--------------------------------------***********************************

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import subprocess

# Define the Bash commands and their expected outputs
bash_commands = [
    {"command": "ls -l", "expected_output": "expected ls -l output goes here"},
    {"command": "echo $PWD", "expected_output": "expected echo $PWD output goes here"},
    {"command": "last", "expected_output": "expected last output goes here"}
]

ID1_command = [
    {"p0": "ls -a", "expected_result": "strig1"},
    {"eth0": "ls -la", "expected_result": "string2"},
    {"vns0": "$PWD", "expected_result": "string2"}
]

ID2_command = [
    {
    }
]

# Create a PDF file
pdf_filename = "bash_commands_output.pdf"
document = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Create data for the table
data_id = [["Bash Command", "Expected Output", "Actual Output", "Result"]]

#execute the comamnd for each test cases 
class test_verification:
    def __init__(self, test_id, expected_result):
        self.test_id = test_id
        self.expected_result =expected_result
        
    def tc_execution_fun(self):
        a=1000
        b=100
        match(a,b):
            case(ID1,b):
                print("execute the function for the test case")
                for command_info in ID1_command:
                    command = command_info["command"]
                    expected_output = command_info["expected_output"]
                    try:
                        actual_output = subprocess.check_output(command, shell=True, text=True).strip()
                        result = "Pass" if actual_output == expected_output else "Fail"
                    except subprocess.CalledProcessError as e:
                        actual_output = str(e)
                        result = "Fail"
                    data_id.append[["command","expected_output","actual_output","result"]]
                print(data_id)
                     
            case(ID2,b):
                print("case number second")
                
            case(ID3,b):
                print("case number 4th")
                
            case(ID4,b):
                print("case number 5th")
                            
        print("Expected result")

p1=test_verification()
p1.tc_execution_fun()


for command_info in bash_commands:
    command = command_info["command"]
    expected_output = command_info["expected_output"]
    
    try:
        actual_output = subprocess.check_output(command, shell=True, text=True).strip()
        result = "Pass" if actual_output == expected_output else "Fail"
    except subprocess.CalledProcessError as e:
        actual_output = str(e)
        result = "Fail"

    data.append([command, expected_output, actual_output, result])

# Create a table
table = Table(data)

# Define table style
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header padding
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Table body background color
    ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Table grid lines
])

table.setStyle(style)

# Build the PDF document
elements = [table]
document.build(elements)

print(f"Table saved to {pdf_filename}")


######----------------------------
import paramiko

def run_ssh_command(hostname,ip_address,passwd,command_ex):
    
    client =  paramiko.SSHClient()
    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(hostname,ip_address,passwd,command_ex)
                # Run the command
        stdin, stdout, stderr = client.exec_command(command_ex)
        
        # Read the output
        output_ret = stdout.read().decode('utf-8')
        print(output_ret)
        return output_ret
    except paramiko.AuthenticationException:
        print("Authentication failed")
    except Exception as ex:
        print("Errro",{str(ex)})

    finally:
        client.close()
        
#Provide input details
hostname = Ip
ip_address = df
passwd = df
command_ex = df

command_to_run = "df -h"

# Run the SSH command
result = run_ssh_command(hostname, ip_address, passwd, command_ex)

# Print the result
print("Result of 'df -h' on the remote server:")
print(result)
 
####-------------------------- 
import subprocess

res = subprocess.run("sshpass -p <passwd>", "ssh hostname@ip", "df -h")

print(res)
#####___________________Regex for the string

import re

pattern = r'^[a-z]+\d+[a-z]+_\d+[a-z]+_\d+[a-z]+_\d+[a-z]+$'

string_to_match = "abcjdjj8asf_998dnfbajfd_7446gf6w37_74623hfdyfy"

if re.match(pattern, string_to_match):
    print("Match found!")
else:
    print("No match.")
    
##################---------------------------

#time_details = _time.time()
#t= _time.localtime()

################################################
class car:
    def __init__(self, color, model) -> None:
        self.color =  color
        self.model = model
        pass
    
    def show_car_details(self):
        print(self.model)
        
vehicle = car("Blue","MB")

cars = ["a","b","c","d"]
for x in cars:
    print(x)

vehicle = car("white",cars[1])

print(vehicle.model)
print(vehicle.color)

try:
    print(y)
except SyntaxError as a:
    print(a)
except NameError as n:
    print(n)

################################################## 01 test case
import re
patrn = "myvar-"

ret = "MTC-nfdnjkln-354565 PCM-kdkkjkjk-5655 myvar-fndndnfn-515"

output = re.findall(patrn, ret, flags=0) 
print(output)
print(patrn)
#output.__contains__()
result = "Fail" if patrn == output[0] else "Pass"

print(result)
if patrn == output[0]:
    print("Match found! Failed")
else:
    print("No match. Pass")
    

###################################################################
##TC-03
import re
patrn = "zam_heath_check.py"

ret = "MTC-nfdnjkln-354565.json PCM-kdkkjkjk-5655.log myvar-fndndnfn-515.sh root 2654 5646465 Aug 2023 zam_heath_check.py"

output = re.findall(patrn, ret, flags=0) 
print(output)
print(patrn)
#output.__contains__()
result = "Pass" if patrn == output[0] else "Fail"
print(result)

if patrn == output[0]:
    print("Match found! Pass")
else:
    print("No match. Fail")
    
    
patrn = "_heath_report_"

ret = "MTC-nfdnjkln-354565.json PCM-kdkkjkjk-5655.log myvar-fndndnfn-515.sh root 2654 5646465 Aug 2023 zam_heath_check.py 1564545655_heath_report_26546545-utc.json"

output = re.findall(patrn, ret, flags=0) 
print(output)
print(patrn)
#output.__contains__()
result = "Pass" if patrn == output[0] else "Fail"
print(result)    
    
################################################################
 ###00_d
import subprocess
# Create data for the table
import re

#mac_address_pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
#/^\d+:[a-z]+\d:[0-9]+\w:[a-z]{2}:[0-9]{2}:[0-9]+$
mac_address_pattern = re.compile(r'^\d+:[a-z]+\d:[0-9]+\w:[a-z]{2}:[0-9]{2}:[0-9]+$')
print(mac_address_pattern)
# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
res = mac_address.count(':')
print(res)
if mac_address_pattern.match(mac_address):
    print("Valid MAC address.")
else:
    print("Invalid MAC address.")

data_id = [["Bash Command", "Expected Output", "Actual Output", "Result"]]
ID1_command = [
    {"p0": "ls -a", "expected_result": "strig1"},
    {"eth0": "ls -la", "expected_result": "string2"},
    {"vns0": "$PWD", "expected_result": "string2"}
]
print("execute the function for the test case")
for command_info in ID1_command:
    command = command_info["command"]
    expected_output = command_info["expected_output"]
    try:
        actual_output = subprocess.check_output(command, shell=True, text=True).strip()
        result = "Pass" if actual_output == expected_output else "Fail"
    except subprocess.CalledProcessError as e:
        actual_output = str(e)
        result = "Fail"
    data_id.append[["command","expected_output","actual_output","result"]]
print(data_id)   
####################################################################
 
d ={'a': "string1", 'b': "string2", 'cmd': [1,2,3,4]} # dictionary
d['b'] = "string3"
d['cmd'][1] = 5

print()
print(d['a'])
print(d['b']) 
print(d['cmd'])
print(d['cmd'][0])

print(type(d))
#-----------
sr = "hello"
x= []
for i in sr:
    x.append(i)
print(sr)
print(x)
#--------------------
s="Geeks"
x=[i for i in s]
print(x)
#---------------

strh = "I Love my india"
x = list(strh.split())
print(x)

#---------------------
import re
# Function which uses re.findall method to convert string to list character wise
def Convert(string):
    return re.findall('[a-zA-Z]', string)    
# Driver code
str1="ABCD"
print("List of character is : ",Convert(str1))
#-----------------------------------------------issue in below code


#----------------------
import re 
#str1 = "l;f;asjkklklknl jnhkjdkjsnk,lnlk  amlkml;kas;ll;;l kjklkna,slkj,klkk kll .,mlkjllk,. etho: 88:56:j5:f5:25:96   eth1: 99:56:g5:f5:22:56"
#pathern = ''
#matchd = compile(re^[\w\w:\w\w:\w\w:\w\w:\w\w:\w\w])
#res = re.findall('', str1)
print(type(res))
print((res))

string="15345535_health_check-utc.json"
tmp = re.compile(r'-utc.json')
res_ = re.findall(tmp,string)
print(type(res_))
print((res_))
print((tmp))
if tmp == res_:
    print("pass")
else:
    print("fail")
    
#################%%%%%%%%%%%%%%%

import datetime

x = datetime.datetime.now()
print(x.year)
print(x.day, x.hour, x.minute, x.second)
print(x.strftime("%A"))
###############################____WORKING-Logic______________**********************************************************************
import re

txt = "The rain in Spain"
s= "Timeout-52635523153-xfnd544f4-ed1sd1412d-sdfjkdsk"
x = re.search("^Timeout-", s)

if x:
  print("YES! We have a match!")
else:
  print("No match")
############################################################
import re

#Check if the string starts with "The" and ends with "Spain":
print("***************************")
txt = ['eth1:','SAm','Match', 'p0:','56:d4:f5:56:54']
r= '56:d4:f5:56:54'
count=0
var =[]
for p in txt:
    ch = re.search("p0:", p)
    if ch:
        print("YES! We have a match!")
        #print(len(txt[p]))
        if x:
            print("Match found")
            count =count +1
        else:
            print("No Match")
    if count == 1:
        print(p)
        var.append(p)
        print("Got ID")
print(var)  
    #print(type(txt))
for z in var:
    x = re.search("\w\d:\w\w:\w\w:\w\w:\w\d", z)
    print(type(var))
    if x:
        print("YES! We have a match!")
        print(x)
    else:
        print("No match")
        
 
######################################################

#The Match object has properties and methods used to retrieve information about the search, and the result:

#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

############################################################
import re

#Check if the string starts with "The" and ends with "Spain":
print("***************************")
txt = ['eth1:','SAm','Match', 'ether:','56:d4:f5:56:54','jghkahjh']
r= '56:d4:f5:56:54'
count=0
var =[]
for p in txt:
    ch = re.search("ether:", p)
    if ch:
        print("YES! We have a match!")
        print(ch)
        count =count +1
    else:
        print("match Fail")
    if count == 1:
        print(p)
        var.append(p)
        print("Got ID")
        count = count +1
    elif count ==2:
        print(p)
        var.append(p)
        print("Got ID")
        count = 0      
print(var)  
    #print(type(txt))
for z in var:
    x = re.search("\w\d:\w\w:\w\w:\w\w:\w\d", z)
    print(type(var))
    if x:
        print("YES! We have a match!")
        print(x)
    else:
        print("No match")
    
    
######################################################################################
def dict1(sample_dict, key, list_of_values):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].insert(0,list_of_values)
    return sample_dict

word_freq = {'example': [1, 3, 4, 8, 10],
             'for': [3, 10, 15, 7, 9],
             'this': [5, 3, 7, 8, 1],
             'tutorial': [2, 3, 5, 6, 11],
             'python': [10, 3, 9, 8, 12]}
count=0
word_freq['tutorial'].clear()
for x in range(0,5):
	count=x
	word_freq = dict1(word_freq, 'tutorial', 0)
print(word_freq)

#output:-{'example': [1, 3, 4, 8, 10], 'for': [3, 10, 15, 7, 9], 'this': [5, 3, 7, 8, 1], 'tutorial': [0, 0, 0, 0, 0], 'python': [10, 3, 9, 8, 12]}

#######################################################################################################

import subprocess

def execute_script(script_path):
    try:
        result = subprocess.check_output(['python3', script_path], text=True, stderr=subprocess.STDOUT)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.strip()}"

# Replace 'script1.py' with the path to your script
script_path = 'script1.py'

# Execute script1.py and capture the output
execution_result = execute_script(script_path)

# Print or use the execution result as needed
print("Execution Result:")
print(execution_result)
#########++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import re

#Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "The rain in Spain abc_pqr555_arm64.deb"
x = re.search(r'abc.\w+\.deb$', txt)
#print(x.span())#
print(x)
#####################################################
import re

#Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "Regrup_efi-arm64-bin_xyz2kdk_arm64.deb asdfkdsakjfasjk lkafjsaslfnas 56456564 "
#p = re.compile(r"Regrup_efi-arm64-bin_\w+\.deb$")
#print(p)
x = re.search(r"Regrup_efi-arm64-bin_\w+.deb", txt)
print(x)

#########################
#match(pattern, pos= start, pos=end)
#search(pattern, pos= start, pos=end) # pos does not neccessary it will search full string



import datetime
import time

import logging

#logger = logging.getLogger(__name__)

logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s', filemode='w')

x = datetime.datetime.now()
logging.info(x)
logging.info(x.year)
logging.info(x.day, x.hour, x.minute, x.second)
logging.info(x.strftime("%A"))

starttime= time.time()
logging.info(starttime)
time.sleep(120)
endtime = time.time()
logging.info(endtime)
count = endtime -starttime
logging.info(count)

##########################################
#import re
#import logging

#logger = logging.getLogger(__name__)

#logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

#Strf = "Successfully mounted all disks - disconnect all disks PASSED - Unmount all disks PASSED - Connect to all nvme device PASSED -"

#search_str = re.search(r"Successfully.mounted.all.disks", Strf)

#logging.debug(search_str)

###########################################
#import logging

#logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

import logging
import time
logging.basicConfig(filename='test.log', level=logging.DEBUG, format='[%(asctime)s]- [%(levelname)s]- [%(message)s]', filemode='w')
x,y,z=4,3,5
logging.debug("Value of the x")
logging.debug("Value of the y")
logging.debug("Value of the z")
print(x)

#################
#parser

import logging
import time

class p1:
    def __init__(self) -> None:
        pass
    def details(self):
        print("Your in the P1")
        return 1
     
class p2:
    def details(self):
        print("here is class p2")        
        return 0
class project(p1,p2):
  
    def func(self, name, sub, mark):
        print("Here in the project class test")
        print(name)
        print(sub)
        print(mark)
        
    def func1(self, string):
        print("Function func1 {}".format(string))

meth = project()
meth.details()
var = meth.details()
print(var)
meth.func("Sat","math", 100)
meth.func1("World")

"""






