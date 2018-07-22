# -*- coding: utf-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding('gbk')
import matplotlib.pyplot as plt
import xlwings as xw
import datetime
import pythoncom
pythoncom.CoInitialize()
class Exceltool(object):
	timeneed=str(datetime.date.today()-datetime.timedelta(days=1))
	filename='C:\Users\ZFM\Desktop\采集器监控文档\受理轨迹新门户日志数据统计%s.xlsx'%(timeneed)
	dicdata={}
	def __init__(self):
		pass
	def exceldata(self):
		app=xw.App(visible=False,add_book=False)
		app.display_alerts=False
		wb=app.books.open(self.filename.decode("utf8","ignore").encode("gbk","ignore"))
		alldata=wb.sheets[0].range(1,1).options(expand='table').value
		headlist=alldata[0]#第一行
		collect_code=[]
		returndata1=[]
		returndata=[]
		for i in range(1,len(alldata)-1):
			 collect_code.append(alldata[i][0]) 
		for i in headlist:
			if self.timeneed in i:
				indexnum=headlist.index(i)
				break
		for i in headlist:
			if u'''部署IP''' in i:
				ipindexnum=headlist.index(i)
				break
		for i in range(1,len(alldata)-1):
			returndata1.append(alldata[i][0])
			returndata1.append(alldata[i][1])
			for j in range(indexnum,len(alldata[i])-1):
				returndata1.append(alldata[i][j])
			returndata.append(returndata1)
			returndata1=[]
		wb.close()
		return  returndata
		
if __name__=='__main__':
   a=Exceltool()
   print a.exceldata()