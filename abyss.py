import os
import shutil
from tqdm import tqdm

class Pull_From_Abyss:
    dst_dir = os.getcwd() + '/files from abyss/'
    abyssal_files_count = 0
    abyssal_dir = ''
    ext = ''

    def __init__(self, abyssal_dir, extension = 'all'):
        self.abyssal_dir = abyssal_dir
        self.ext = extension

        self.verify_output_dir()

        files_path = self.abyssal_files_path(abyssal_dir, extension)
        self.pull_from_abyss(files_path)

    def verify_output_dir(self):
        output_folder = os.getcwd() + '/files from abyss/'
        
        if not os.path.exists(output_folder):
           os.mkdir(output_folder) 

    def abyssal_files_path(self, abyssal_dir, ext):
        abyssal_walker = os.walk(abyssal_dir)
        files_in_abyss = []

        for dirpath, dirnames, filenames in abyssal_walker:
            for filename in filenames:
                if ext != 'all' and not filename.endswith(ext):
                    print(filename)
                    continue

                file_path = f'{dirpath}/{filename}'
                files_in_abyss.append(file_path)

        self.abyssal_files_count = len(files_in_abyss)
        print(f"Found {self.abyssal_files_count} files\n")

        return files_in_abyss

    def pull_from_abyss(self, files_path):
        for path in tqdm(files_path, desc="Pulling files from the abyss"):
            filename = path.rsplit('/', 1)[1]
            final_dst = self.dst_dir + filename
            shutil.move(path, final_dst)

        print(f"Successfully moved {self.abyssal_files_count} files to {self.dst_dir}")