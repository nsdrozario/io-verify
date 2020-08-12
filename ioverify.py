# (C) 2020 Nathaniel D'Rozario
# See LICENSE file for license details

from zipfile import ZipFile
import zipfile
import os
import subprocess
import sys
import datetime
import filecmp

# global vars
archive_name = None
program_name = None
input_files = []
output_files = []
success_count = 0

def main(argc, argv):
    
    if argc != 3:
        print("usage: python ioverify.py [program_name] [test_case_archive_name]")
        exit(0)
    
    program_name = argv[1]
    archive_name = argv[2]
    archive_size = None

    # check if files exist

    if (os.path.isfile(archive_name) and (os.path.isfile(program_name + ".exe") or os.path.isfile(program_name)) and zipfile.is_zipfile(archive_name)) == False:
        print("error: invalid files / files don't exist")
        exit(0)

    # then iterate through contents of zipfile
    
    with zipfile.ZipFile(archive_name, "r") as archive:

        files=archive.namelist()
        archive_size = len(files)

        if archive_size % 2 != 0:
            print("invalid number of files, please check there is an .in and .out file for each case")
            exit(-1)

        for file in files:
            if file[-3:] == ".in":
                input_files.append(file)
            elif file[-4:] == ".out":
                output_files.append(file)
        
        for i in range(int(archive_size/2)):
            it = i+1
            with archive.open(input_files[i], "r") as file_in:
                
                # read file contents of current test case and apply them to the real input file for the program
                contents = file_in.read()
                program_input = open(program_name + ".in", "wb")
                program_input.write(contents)
                program_input.close()

                # run process
                p = subprocess.run([program_name])

                # debugging output
                print("Test case " + str(it))
                print("===============================================")
                
                # extract expected output
                archive.extract(output_files[i])

                if filecmp.cmp(output_files[i], program_name + ".out"):
                    print("RESULT: Test case successful")
                    global success_count
                    success_count += 1
                else:
                    file_expected = open(output_files[i], "r")
                    file_actual = open(program_name + ".out", "r")
                    print("RESULT: Test case failed")
                    print("Expected output: " + file_expected.read())
                    print("Actual output: " + file_actual.read())
                    file_expected.close()
                    file_actual.close()
                
                os.remove(output_files[i]) # cleanup

            print("-----------------------------------------------")
        
        print("Passed cases: " + str(success_count) + " / " + str(int(archive_size/2)))
        

if __name__ == "__main__":

    main(len(sys.argv), sys.argv)