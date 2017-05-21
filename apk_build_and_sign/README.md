# apk build and sing tool

## 目的
當修改完apk檔案後，能快速的build和加上sign，不用打一堆指令

## 使用方式
有2種方式  
1. 啟動後，再輸入，這方法使用`apk_build_and_sign_for_input.py`這檔案  
2. 一行指令方式，這方法使用`apk_build_and_sign_for_command_line.py`這檔案  
指令範例  
<code>python apktool_build_and_sign_for_command_line.py -ap {apktool path} -f {file path} -j {java jdk path} -kp {keystore path} -sp {storepass} -a {alias}</code>
