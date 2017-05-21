#!/usr/bin/env python
# coding=utf-8
import argparse
import subprocess
from subprocess import PIPE, STDOUT

parser = argparse.ArgumentParser(description="some information here")
requiredArg = parser.add_argument_group('required arguments')
requiredArg.add_argument("-e", "--emulatorpath", help="your emulator path fo your computer", required=True)
args = parser.parse_args()

emulator_path = args.emulatorpath

emulator_list_format = "\"{emulator_path}\" -list-avds".format(emulator_path=emulator_path)

ret_mes = subprocess.check_output(emulator_list_format, shell=True)
device_list = [device.strip() for device in ret_mes.decode('utf-8').split('\n') if device]
for idx, device in enumerate(device_list):
	print(idx, ':', device)
	
device_idx = int(input('Enter idx:'))
if device_idx < 0 or device_idx >= len(device_list):
	print('bye')
	exit(1)
	
open_emulator_format = "\"{emulator_path}\" -avd {device} -netdelay none -netspeed full" \
	.format(emulator_path=emulator_path, device=device_list[device_idx])
ret_mes = subprocess.check_output(open_emulator_format, shell=True)
print(ret_mes)