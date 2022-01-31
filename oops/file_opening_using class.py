class file_handling:
    def __init__(self,file_name) :
        try:
            self.filename = file_name
        except Exception as e:
            return e

    def read(self):
        try:
            f = open(self.filename,'r') 
            elememt = f.read()
            f.close
            return elememt
        except Exception as e:
            return e
    def write(self,text):
        if type(text)==str:
            try:
                f = open(self.filename,'a')
                f.write(text)
                return "You write into file successfully"
            except Exception as e:
                return e
        else : 
            raise Exception("Please Enter text data")


class base(file_handling):
    def __init__(self, file_name):
        super().__init__(file_name)

    def rutvik_greating(self):
        try:
            f = open(self.filename,'a')
            f.write("\nWelcome Rutvik Jaiswal")

            f.close()
            return "This is made by rutvik jaiswal"
        except Exception as e:
            return e

    def __str__(self) -> str:
        return "Author is rutvikjaiswal195@gmail.com"




rutvik = base('interitance_exerice.txt')


print(rutvik.rutvik_greating())