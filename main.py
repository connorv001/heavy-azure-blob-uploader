import os
import concurrent.futures
import config
import uploader

def upload_files(files, container_name):
    with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
        futures = [executor.submit(uploader.upload_file, file, container_name) for file in files]
        concurrent.futures.wait(futures)

if __name__ == '__main__':
    source_dir = '/path/to/source/dir'
    target_container = 'target-container'
    files = [os.path.join(source_dir, file) for file in os.listdir(source_dir)]
    upload_files(files, target_container)
