#!/usr/bin/env python
# coding=utf-8
import argparse
import sys
import subprocess
from subprocess import PIPE, STDOUT

parser = argparse.ArgumentParser(description="some information here")
requiredArg = parser.add_argument_group('required arguments')
requiredArg.add_argument("-ap", "--apktoolpath", help="your apktool path of your computer", required=True)
requiredArg.add_argument("-f", "--filepath", help="your file path what you want build", required=True)
requiredArg.add_argument("-j", "--javapath", help="your java jdk path of your computer", required=True)
requiredArg.add_argument("-kp", "--keystorepath", help="your keystore path", required=True)
requiredArg.add_argument("-sp", "--storepass", help="your storepass of keystore", required=True)
requiredArg.add_argument("-a", "--alias", help="your alias of keystore", required=True)
parser.add_argument("-c", "--createsign", help="type this if you want create sign", default=False)
args = parser.parse_args()

apktool_path = args.apktoolpath
file_path = args.filepath
java_path = args.javapath
keystore_path = args.keystorepath 
storepass = args.storepass 
alias = args.alias
creat_sign_flag = args.createsign

apktool_format = "\"{apktool_path}\" b {file_path}".format(apktool_path=apktool_path,file_path=file_path)

ret_mes = str(subprocess.check_output(apktool_format, shell=True))
if 'ERROR' in ret_mes:
	print("Error", ret_mes)
	exit()

apk_name = file_path.split('\\')[-1] + '.apk'
apk_file_path = "{file_path}\dist\{apk_name}".format(file_path=file_path, apk_name=apk_name)

if creat_sign_flag:
	print("Input keytool information:")
	keystore_path = input("keystore path: ")
	alias = input("alias: ")
	keypass = input("keypass: ")
	storepass = input("storepass: ")
	common_name = input("common name: ")
	organization_unit = input("organization unit: ")
	organization_name = input("organization name: ")
	locality_name = input("locality name: ")
	state_name = input("state name: ")
	country = input("country: ")
	
	keytool_format = \
		("\"{java_path}\keytool\" -genkey -v -keyalg DSA -keysize 1024 -sigalg SHA1withDSA -validity 20000 " + \
		"-keystore {keystore_path} -alias {alias} -keypass {keypass} -storepass {storepass}") \
		.format(java_path=java_path,
				keystore_path=keystore_path,
				alias=alias,
				keypass=keypass,
				storepass=storepass)

	keytool_sign_info_format = \
		"{common_name}\n{organization_unit}\n{organization_name}\n{locality_name}\n{state_name}\n{country}\ny\n" \
		.format(common_name=common_name,
				organization_unit=organization_unit,
				organization_name=organization_name,
				locality_name=locality_name,
				state_name=state_name,
				country=country)
	
	p = subprocess.Popen(keytool_format, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	
	out = p.communicate(input=keytool_sign_info_format.encode())[0]
	if 'Exception' in str(out):
		print("Exception", str(out))
		exit()
	else:
		print("create sign success!")
	
	
jarsigner_format = \
	("\"{java_path}\jarsigner\" -tsa http://timestamp.digicert.com -verbose -sigalg SHA1withDSA -digestalg SHA1 " + \
	"-keystore {keystore_path} -storepass {storepass} \"{apk_file_path}\" {alias}") \
	.format(java_path=java_path,
			keystore_path=keystore_path,
			storepass=storepass,
			apk_file_path=apk_file_path,
			alias=alias)
			
p = subprocess.Popen(jarsigner_format, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate()[0]
if 'jar signed' in str(out):
	print("Success!")
else:
	print("Error", out.decode('UTF-8', 'strict'))
