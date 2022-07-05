#   duck typing

class vscode:
    
    def execute(self):
        print("compiling")
        print("running")
        
        
        
class editor:
    def execute(self):
         print("checking")
         print("debuging")
         print("compiling")
         print("running")
class laptop:
    
    def code(self,ide):
        ide.execute()
        
ide=vscode()
ide=editor()

lap1=laptop()
lap1.code(ide)