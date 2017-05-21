#!/usr/bin/env python
# coding=utf-8
import argparse
import subprocess
from subprocess import PIPE, STDOUT

parser = argparse.ArgumentParser(description="some information here")
requiredArg = parser.add_argument_group('required arguments')
requiredArg.add_argument("-ap", "--apktoolpath", help="your apktool path fo your computer", required=True)
requiredArg.add_argument("-z", "--z7azpath", help="your 7za path fo your computer", required=True)
requiredArg.add_argument("-d", "--dex2jarpath", help="your dex2jar path of your computer", required=True)
requiredArg.add_argument("-f", "--filepath", help="your file path what you want build", required=True)
args = parser.parse_args()

apktool_path = args.apktoolpath
z7az_path = args.z7azpath
dex2jar_path = args.dex2jarpath
file_path = args.filepath

apktool_format = "\"{apktool_path}\" d {file_path}".format(apktool_path=apktool_path, file_path=file_path)

ret_mes = str(subprocess.check_output(apktool_format, shell=True))
if 'ERROR' in ret_mes:
	print("Error", ret_mes)
	exit()
	
z7az_path_format = "\"{z7az_path}\" e {file_path} classes.dex".format(z7az_path=z7az_path, file_path=file_path)

ret_mes = str(subprocess.check_output(z7az_path_format, shell=True))

if 'Error' in str(ret_mes) or 'ERROR' in str(ret_mes ):
	print("Error", str(ret_mes))
	exit()
else:
	print("extract classes.dex success!")
	
z7az_path_format = "\"{dex2jar_path}\" classes.dex".format(dex2jar_path=dex2jar_path)
ret_mes = str(subprocess.check_output(z7az_path_format, shell=True))


	