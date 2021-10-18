import os

class prettySoldier:

	def RenameFunction(self,_pathfolder):
		  for file in _pathfolder:
					_cfile = os.rename(file , file.capitalize())
					get = os.getcwd()
					print(f"After renamining the file {get}")


	def RenamePng(self,png):
		i = 0
		for pngfiles in png:
			re = os.path.splitext(png)
			s=str(i+re)
			renFile = os.rename(pngfiles,s)
			i = i+1
			# print(pngfiles)
	print("Successfully completed")





pre = prettySoldier()
changedirectory = os.chdir("C:\Mohit's Folder")  
changedirectory2 = os.chdir("F:\mohit") 
pathfolder = os.listdir(changedirectory)
pathfolder2 = os.listdir(changedirectory2)
pre.RenameFunction(pathfolder)
pre.RenamePng(pathfolder2)


