#!/usr/bin/env python
# coding=utf-8
import argparse
import subprocess
from subprocess import PIPE, STDOUT

parser = argparse.ArgumentParser(description="some information here")
requiredArg = parser.add_argument_group('required arguments')
requiredArg.add_argument("-adb", "--adbpath", help="your adb path of your computer", required=True)
requiredArg.add_argument("-ap", "--androidvncserverpath", help="your file path of androidvncserver", required=True)
args = parser.parse_args()

adb_path = args.adbpath
emulator_androidvncserver_path = args.androidvncserverpath

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

device = device_list[device_idx]

push_vnc_format = "\"{adb_path}\" -s {device} push {androidvncserver_path} {emulator_androidvncserver_path}" \
    .format(adb_path=adb_path,
            device=device,
            androidvncserver_path=flask_config.androidvncserver_path,
            emulator_androidvncserver_path=emulator_androidvncserver_path)
ret_mes = subprocess.check_output(push_vnc_format, shell=True)

chmod_775_format = "\"{adb_path}\" -s {device} shell chmod 775 {emulator_androidvncserver_path}" \
    .format(adb_path=adb_path,
            device=device,
            emulator_androidvncserver_path=emulator_androidvncserver_path)
ret_mes = subprocess.check_output(chmod_775_format, shell=True)

forward_tcp_5901_format = "\"{adb_path}\" -s {device} forward tcp:5901 tcp:5901" \
    .format(adb_path=adb_path,
            device=device)
ret_mes = subprocess.check_output(forward_tcp_5901_format, shell=True)

forward_tcp_5801_format = "\"{adb_path}\" -s {device} forward tcp:5801 tcp:5801" \
    .format(adb_path=adb_path,
            device=device)
ret_mes = subprocess.check_output(forward_tcp_5801_format, shell=True)

start_vnc_format = "\"{adb_path}\" -s {device} shell ./{emulator_androidvncserver_path}" \
    .format(adb_path=adb_path,
            device=device,
            emulator_androidvncserver_path=emulator_androidvncserver_path)
subprocess.Popen(start_vnc_format, shell=True,
            stdin=None, stdout=None, stderr=None, close_fds=True)