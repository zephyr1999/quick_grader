# quick_grader is a way to quickly grade a full (potentially zipped) directory of
# student's files downloaded from moodle. User specifies a file or directory,
# whether or not its zipped, and then parses the student's files. It unzippes 
# them if necessary, does a compile with the specified compiler, and runs with 
# given input/output files (or interacts with the user) and grades according 
# to a specified rubric. 

import sys
import os
import subprocess

def handle_args():
    #TODO impliment me
    input_file = "input1.txt"
    output_file = "output1.txt"
    rubric_file = "rubric.txt"
    directory = "anon_data/"
    compiler = "python"
    zipped = False

    return input_file, output_file, rubric_file, compiler, directory, zipped

def unzip(directory):
    #TODO impliment me
    # directory ends in '.zip' so we unzip and return the unziped filename
    # for now, jsut call teh directory extracted
    subprocess.check_output(["unzip", directory, '-d','extracted'])
    return 'extracted'


def run_interact_mode(rubric,directory,compiler):
    #TODO impliment me
    return -1

def run_with_files(input_file, output_file, rubric, directory,compiler):
    #TODO impliment compilers

    # dictionary to store users grades
    grades = {}

    # compiling bonus (should be an int) 
    bonus = int(read_property('COMPILE_BONUS',rubric))

    #specified filename
    student_file = read_property('PROGRAM_NAME',rubric).strip()
    
    # loop over each student
    for student in os.listdir(directory):
        # create an entry for that student with compile grade
        grades[student] = bonus

        # open student's folder 
        student_exe = directory+'/'+student+'/'+student_file

    # run the student's file
    subprocess.run(['python',student_exe],stdin=open(input_file),stdout=open("out.txt",'w'))

    #TODO compare out.txt with output file

    #TODO grade output

    return grades

def read_property(prop_name,rubric):
    # opens the rubric file
    with open(rubric) as fl:
        # read in all lines
        lines = fl.readlines()
    # find line with 'COMPILE_BONUS' property
    for line in lines:
        if prop_name in line:
            # return value found after a space
            return line.split(' ')[1]

if __name__ == '__main__':
    # handle the commandline arguments
    input_file, output_file, rubric_file, compiler, directory, zipped = handle_args()

    # unzip if needed
    if zipped:
        directory = unzip(directory)       

    if input_file == None:
        # the user wishes to interact with each program
        grades = run_interact(rubric_file, directory, compiler)

    else:
        # we jsut use the input and output for each file
        grades = run_with_files(input_file, output_file, rubric_file, directory,compiler)
