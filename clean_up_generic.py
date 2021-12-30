import os,shutil,argparse,getopt
parser = argparse.ArgumentParser(description='Enter the directory to remove everything expect last 2 builds and latest ')
parser.add_argument('--search_dir', type = str, required = True)
args = parser.parse_args()
print("Your Input Root Directory for cleanup is ")
print((args.search_dir))
search_dir=args.search_dir
os.chdir(search_dir)
files = filter(os.path.isdir, os.listdir(search_dir))
files = [os.path.join(search_dir, f) for f in files] # add path to each file
files.sort(key=lambda x: os.path.getmtime(x))
not_del_counter=3
for i in range(0,len(files)-not_del_counter):
	if "latest" not in files[i]:
		#print(files[i])
		try:
			## Try to remove tree; if failed show an error using try...except on screentry:
    			#shutil.rmtree(files[i])
			print("Removing Directory")
			print(files[i])
		except OSError as e:
    			print ("Error: %s - %s." % (e.filename, e.strerror))