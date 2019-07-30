file_path= 'my_file.txt'
file_hand=open(file_path,'w')
text1='writing line 1 \n '
file_hand.write(text1)
text2='writing line 2 \n '
file_hand.write(text2)
file_hand.close()