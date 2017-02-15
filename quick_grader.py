import sys
import subprocess
import getopt
import os

def handle_args():
    # too lazy to handle args with a library so I do it like this.
    # ARG LIST
    # -z => (True/False) directory file is a zip and needs to be unzipped
    # -f filename => input file. if not specified, user wants to interact.
    try:
        opts,args = getopt.getopt(sys.argv[1:],"d:zf:o:",['directory=','zipped','file=','outputdir='])
    except getopt.GetoptError:
        print("usage: quick_grader.py -d <directory> -z -f <inputfile> -o <outputdir>")
        sys.exit()
    
    #initialize these arguments because we need to handle the cases that they aren't specified
    directory = None
    in_file = None
    zipped = False
    unzipped_dir = 'out'

    # actually handle the arguments
    for opt,arg in opts:
        # first, set the directory
        if opt in ['-d','--directory']:
            directory = arg

        # set up the input file
        elif opt in ['-f','--file']:
            in_file = arg
        
        # set zippped boolean to true
        elif opt in ['-z','--zipped']:
            zipped = True

        # if this option is specified, it means user has specified an unzipping location
        elif opt in ['-o','--outputdir']:
            unzipped_dir = arg

    # if the directory is zipped, unzip it and set directory = unzipped
    if zipped:
        # unzip the directory to the (un-)specified folder
        output = subprocess.check_output(['unzip','-d',unzipped_dir,directory])
        # set directory to the newly unzipped directory
        directory = unzipped_dir

    # return our stuff
    return directory,in_file

def run_code(directory,infile):
    # compiles and runs the code in the specified directory. 
    # if the code is zipped, it unzips it first.
    #TODO impliment me
    pass

# main method
if __name__=='__main__':
    directory,in_file = handle_args()

    # Moodle unpacks the submissions into directories
    # so loop over all folders in directory and run the programs in each
    for student_dir in os.listdir(directory):
        # prepending directory here since student_dir isnt in root
        run_code(directory+student_dir, in_file)
