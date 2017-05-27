#!/usr/bin/env python
# coding=utf-8
import argparse
import subprocess
from subprocess import PIPE, STDOUT

parser = argparse.ArgumentParser(description="some information here")
requiredArg = parser.add_argument_group('required arguments')
requiredArg.add_argument("-adb", "--adbpath", help="your adb path of your computer", required=True)
requiredArg.add_argument("-f", "--filepath", help="your file path what you want install", required=True)
requiredArg.add_argument("-p", "--packagename", help="your package name of your apk file", required=True)
args = parser.parse_args()

adb_path = args.adbpath
file_path = args.filepath
package_name = args.packagename

adb_list_format = "\"{adb_path}\" devices".format(adb_path=adb_path)

ret_mes = subprocess.check_output(adb_list_format, shell=True)

device_list = [device.split('\t')[0].strip() for device in ret_mes.decode('utf-8').split('\n') \
	if device.strip() and len(device.split('\t')) == 2 and 'device' in device.split('\t')[-1]]
for idx, device in enumerate(device_list):
	print(idx, ':', device)
	
device_idx = int(input('Enter idx:'))
if device_idx < 0 or device_idx >= len(device_list):
	print('bye')
	exit(1)
	
uninstall_format = "\"{adb_path}\" -s {device} uninstall {package_name}" \
	.format(adb_path=adb_path, device=device_list[device_idx], package_name=package_name)
ret_mes = subprocess.check_output(uninstall_format, shell=True)
print(ret_mes.decode('utf-8'))

install_format = "\"{adb_path}\" -s {device} install {file_path}" \
	.format(adb_path=adb_path, device=device_list[device_idx], file_path=file_path)
ret_mes = subprocess.check_output(install_format, shell=True)
print(ret_mes.decode('utf-8'))