import os
class WfBat(object):
    def __init__(self) -> None:
        pass

class BioProject(WfBat):
    def __init__(self) -> None:
        self.projectName = None
        self.workFlowList = []
    
    def startproject(self,Name):
        self.projectName = Name
        print(os.getcwd())
        
    def mkdir(self,path):
        path = path.strip()
        path = path.rstrip("\\")
        if isExists := os.path.exists(path):
            print(f'ERROR: {path} \nThe project already exists, please change the project name!')
            return False
        else:
            os.makedirs(path)
            print("项目创建成功!\n项目位于: {path}")
            return True
