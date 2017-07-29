#!/usr/bin/env python
# coding=utf-8
import argparse
import sys
import subprocess
from subprocess import PIPE, STDOUT

parser = argparse.ArgumentParser(description="some information here")
requiredArg = parser.add_argument_group('required arguments')
requiredArg.add_argument("-d", "--dex2jarpath", help="your dex2jar path of your computer", required=True)
requiredArg.add_argument("-s", "--d2jsmalipath", help="your d2j smali path of your computer", required=True)
requiredArg.add_argument("-j", "--jadxpath", help="your jadx path of your computer", required=True)
requiredArg.add_argument("-sd", "--smalidirpath", help="your smali dir path what you want unpack", required=True)
args = parser.parse_args()


dex2jar_path = args.dex2jarpath
d2j_smali_path = args.d2jsmalipath
jadx_path = args.jadxpath
smali_dir_path = args.smalidirpath

dj2_smali_path =  "\"{d2j_smali_path}\" {smali_dir_path} -o classes.dex"\
	.format(d2j_smali_path=d2j_smali_path,
			smali_dir_path=smali_dir_path)
ret_mes = str(subprocess.check_output(dj2_smali_path, shell=True))

dex2jar_path_format = "\"{dex2jar_path}\" classes.dex -o classes.jar".format(dex2jar_path=dex2jar_path)
ret_mes = str(subprocess.check_output(dex2jar_path_format, shell=True))

jadx_path_format = "\"{jadx_path}\" -d out classes.jar".format(jadx_path=jadx_path)
ret_mes = str(subprocess.check_output(jadx_path_format, shell=True))