import Tkinter as tk
import urllib2
def search(word):
	file=open("web.txt",'w')
	response = urllib2.urlopen("http://www.yourdictionary.com/"+word+"?direct_search_result=yes")
	page_source = response.read()
	file.write(page_source)
	file.close()
	string=""
	meaning = ""
	thing=""
	flag=0
	file=open("web.txt",'r')
	li=''
	a=0
	x=0
	x1=0
	x2=0
	counter=-1
	for line in file:
			a=line.find('class=\'sense\'')
			if(a!=-1):
				x1=a
				x2=a
				string=line
				break
	b=string.count('class=\'sense\'')
	for i in range(0,b):
		tmp=string.find('class=\"custom_entry_pos\">',x)
		thing=string[tmp+25:a-11]
		c=string.find('class=\'sense\'',a+10)
		if c!=-1:
			d=string.count('class=\'custom_entry\'',x1,c)
		else:
			d=string.count('class=\'custom_entry\'',x1)
		for j in range(0,d):
			e=string.find('_entry\'>',x2)
			f=string.find('</div>',e)
			meaning=string[e+8:f]
			li+=(thing.upper()+" : "+meaning.upper()+"\n")
			x2=e+10
		x=a+20
		a=c
		x1=a
		x2=a
						
	file.close()
	if len(li)==0:
		li+='NO MEANING'
	root=tk.Tk()
	root.title("MEANING")
	#root.geometry("1000x50")
	tk.Label(root,text=li).grid(row=0)
	tk.Button(root, text="OK", command=quit,width=25).grid(row=1,column=0)
	root.mainloop()		
