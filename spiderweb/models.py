import pymysql
from pymongo import MongoClient

class EmpOperations:
    def addnewemployee(self,nm,dp,ps,sl):
        status=None
        try:
            con=pymysql.connect(host='b7ynlwm9vi4twzsxsu9f-mysql.services.clever-cloud.com',user='udsypi8l3ys4ac0q',password='A4qUKkNz34O2aiQ46dk6',database='b7ynlwm9vi4twzsxsu9f')
            curs=con.cursor()
            curs.execute("insert into employee(empnm,dept,post,salary) values('%s','%s','%s','%.2f')" %(nm,dp,ps,sl))
            con.commit()
            con.close()
            status='success'
        except:
            status='error'
        
        return status
    
    def getreportdata(self):
        con=pymysql.connect(host='b7ynlwm9vi4twzsxsu9f-mysql.services.clever-cloud.com',user='udsypi8l3ys4ac0q',password='A4qUKkNz34O2aiQ46dk6',database='b7ynlwm9vi4twzsxsu9f')
        curs=con.cursor()
        curs.execute("select * from employee")
        data=curs.fetchall()
        return data
    

    def addnewworker(self,id,nm,dp,ps,lo,sl):
        status=None
        try:
            client=MongoClient("mongodb+srv://sharayu:mongodb913@ethancluster.npsn31t.mongodb.net/?retryWrites=true&w=majority")
            db=client["praffulldb"]
            coll=db["workers"]
            dic={}
            dic['_id']=id
            dic['name']=nm
            dic['dept']=dp
            dic['post']=ps
            dic['location']=lo
            dic['salary']=sl

            coll.insert_one(dic)
            status='success'
        except Exception as err:
            print(err)
            status='error'
        
        return status

    def allworkers(self):
        client=MongoClient("mongodb+srv://sharayu:mongodb913@ethancluster.npsn31t.mongodb.net/?retryWrites=true&w=majority")
        db=client["praffulldb"]
        coll=db["students"]
        dic={}
        dic['data']=coll.find()
        return dic
