import argparse
import smtplib
import mimetypes
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def parseOptions():
	parser = argparse.ArgumentParser(description='Send e-books to my Kindle Paperwhite.')
	parser.add_argument('file', type=str, help='The e-book file.')
	parser.add_argument('-c', type=str, default = 'y', help='Convert?.')
	parser.add_argument('-t', type=str, default = 'n', help='Test mode, email sent to yahoo.')
	args = parser.parse_args()
#	print args
	return args

def send2Kindle():
	opt = parseOptions()
	
	msg = MIMEMultipart()
	msg['From'] = YOUR_EMAIL_ADDR
	msg['To'] = YOUR_KINDLE_EMAIL_ADDR if opt.t == 'n' else DEBUG_EMAIL_ADDR
	
	msg['Subject'] = '' if opt.c == 'n' else 'Convert'
	
	fileToSend = opt.file # the file to attach

	if not os.path.exists(fileToSend):
		return IOError
	
	
	# get maintype and subtype for MIMEBase
	ctype, encoding = mimetypes.guess_type(fileToSend)
	maintype, subtype = ctype.split("/", 1)
	
	# read (only) 1 attachment file
	fp = open(fileToSend,"rb")
	attachment = MIMEBase(maintype, subtype)
	attachment.set_payload(fp.read())
	fp.close()
	encoders.encode_base64(attachment)
	attachment.add_header("Content-Disposition", "attachment", filename = fileToSend.split('/')[-1])
	
	msg.attach(attachment)
	
	# set mail server info
	username = str(YOUR_EMAIL_ACCOUNT)  
	password = str(YOUR_EMAIL_PASSWORD)
	  
	try :
		server = smtplib.SMTP("smtp.mail.yahoo.com",587) # replace with your own smtp
		print 'Logging into {server}'.format(server='mail.yahoo.com') # replace with your own mail server
		server.starttls()
		server.login(username,password)
		print 'Login success!'
		print 'Sending "{file}" to {to}.'.format(file = fileToSend, to = msg['To'])
		server.sendmail(msg['From'], msg['To'], msg.as_string())
		server.quit()    
		print 'Email has been sent successfully!'
	except :
		print 'Cannot send the Email!'
		
if __name__ == '__main__':
	send2Kindle()
