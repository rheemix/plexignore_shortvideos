import glob
import subprocess
import os


# Get video duration in seconds using ffprobe
def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries",
                             "format=duration", "-of",
                             "csv=p=0", filename],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    return float(result.stdout)


mypath = os.path.abspath(os.path.dirname(__file__)) + '\\'
duration_limit = float(5.0)  # add file name to .plexignore file if duration is less than this value

num_scanned_files = int(0)   # number of scanned video files initialization

# For all directories in the specified path
dirlist = glob.glob(mypath + '/**/*/', recursive=True)
dirlist.insert(0, mypath)
for dir in dirlist:
    print('\n' + dir, end="")

    plexignore = dir + '.plexignore'  # .plexignore file to be placed at each directory

    # remove existing .plexignore files
    if os.path.exists(plexignore):
        os.remove(plexignore)

    f = open(plexignore, "w")  # create new plexignore file in append mode

    # get list of all .MOV & .AVI files
    types = (dir + "*.MOV", dir + "*.AVI", dir + "*.MP4")
    all_files = []
    for files in types:
        all_files.extend(glob.glob(files))

    # For all .MOV & .AVI files, check video duration and add to .plexignore file if < duration_limit
    for file in all_files:
        num_scanned_files += 1
        pathname, filename = os.path.split(file)  # separate path and file name

        try:
            duration = get_length(file)  # get vidoe duration
        except:
            print('** ERROR: Unable to retrieve duration from file ' + file)
        else:
            print('.', end="")
            if duration < duration_limit:
                f.write(filename + '\n')  # add to .plexignore file
    f.close()  # Done writing to the file. Close

    # delete .plexignore file if the file is empty
    if os.stat(plexignore).st_size == 0:
        os.remove(plexignore)
print('\n\nTotal number of scanned videos: ' + str(num_scanned_files))

