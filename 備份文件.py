-*- coding:utf-8 -*-
#python3

cp_File_Name = input("請輸入要備份的文件名:") 
#1.輸入複製的文件名

cp_read = (cp_File_Name, "r")
#2.打開複製的文件

position = cp_File_Name.rfind(".")
new_file_name = f [0:position] + "[new-cp]" + cp_File_Name [position:]
#附件加上

cp_write = open(new_file_name.txt,"w")
#3.創建一個新的文件

content = cp_read.read()
cp_File_Name.write(content)
#4.重cp_File_Name讀取數據,寫到newname文件中

cp_read.close
cpwrite.close
#5.關閉文件

