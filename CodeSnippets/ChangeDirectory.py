#cannot use subprocess to change directory in parent process
#if you use vhange directory in child process, it willnot reflect in parent process
my_cwd = os.getcwd()
print("my_cwd :", my_cwd)

os.chdir("C:\\temp\\MisraZips_AS403_labelApplied")
my_new_cwd = os.getcwd()
print("my_new_cwd :", my_new_cwd)

os.chdir(my_cwd)
my_new_new_cwd = os.getcwd()
