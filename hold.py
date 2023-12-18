
        def getAll(self):
            cursor = self.getCursor()
            sql="select * from student"
            cursor.execute(sql)
            result = cursor.fetchall()
            self.closeAll()
            return result
            


        def findByID(self, id):
            cursor = self.getCursor()
            sql="select * from student where id = %s"
            values =(id, )

            cursor.execute(sql, values)
            result = cursor.fetchone()
            self.closeAll()
            return result
              
        
        def update(self, values):
            cursor = self.getCursor()
            sql="update student set name= %s, age=%s where id = %s"
            #values = ("Joe", 22, 1)
            cursor.execute(sql, values)
            self.connection.commit()
            self.closeAll()

              

        def delete(self, id):
            cursor = self.getCursor()
            sql="delete from student where id = %s"
            values =(id, )
            cursor.execute(sql, values)
            self.connection.commit()
            self.closeAll()
              