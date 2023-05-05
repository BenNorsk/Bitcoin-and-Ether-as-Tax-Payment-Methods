import os
# Delete "All Weights for all Cases" if it exists
try:
    os.system('rm -r "All Weights for all Cases"')
except:
    pass

# Create a new folder called All Weights for all Cases
os.mkdir('All Weights for all Cases')
os.mkdir('All Weights for all Cases/Case 0')
os.mkdir('All Weights for all Cases/Case 1')
os.mkdir('All Weights for all Cases/Case 2')
os.mkdir('All Weights for all Cases/Case 3')
os.mkdir('All Weights for all Cases/Case 4')

# Iterate through the folders in automatise
for folder in os.listdir('automatise'):
    # Iterate through the files in the folder
    case = str(folder)
    print(case)
    try:
        for folder2 in os.listdir(f'automatise/{folder}/data'):
            os.system(f'cp -r automatise/{folder}/data/{folder2} "All Weights for all Cases/Case {case}/{folder2}"')
    except:
        pass

def modify_filename(filename):
    # If the filename does not start with a digit, delete it
    basename = os.path.basename(filename)
    print(basename)
    print(basename[0])
    # If the filename does not start with a digit, delete it
    try:
        s = int(basename[0])
        starts_with_digit = True
    except:
        starts_with_digit = False
        pass
    print(starts_with_digit)
    if not starts_with_digit:
        print("Deleting", filename)
        os.remove(filename)
        return

    # If the filename contains "_rspe_", replace it with "_mspe_"
    if "_rspe_" in basename:
        new_filename = filename.replace("_rspe_", "_mspe_")
        os.rename(filename, new_filename)
        return

# Set the path to the "All Weights for all Cases" folder
folder_path = "All Weights for all Cases"

# Iterate over all files in the folder and its subdirectories
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        full_path = os.path.join(root, filename)
        modify_filename(full_path)

            
            

