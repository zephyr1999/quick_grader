import sys
import subprocess
import getopt

def handle_args():
    # too lazy to handle args with a library so I do it like this.
    # ARG LIST
    # -z => (True/False) directory file is a zip and needs to be unzipped
    # -f filename => input file. if not specified, user wants to interact.
    try:
        opts,args = getopt.getopt(sys.argv[1:],"d:zf:",['directory=','zipped','file='])
    except getopt.GetoptError:
        print("usage: quick_grader.py -d <directory> -z -f <inputfile>")
        sys.exit()
    
    #initialize these arguments because we need to handle the cases that they aren't specified
    directory = None
    in_file = None
    zipped = False

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

    # if the directory is zipped, unzip it and set directory = unzipped
    if zipped:
        #TODO impliment unzipping
        print("unzipped: " + directory)

    return directory,in_file

# main method
if __name__=='__main__':
    directory,in_file = handle_args()
