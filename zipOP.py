import zipfile


class MZipFile(object):
    def __init__(self, zip_path, method: str = 'r'):
        self.zip = zipfile.ZipFile(zip_path, method)  # 创建一个zipfile

    def get_filecount(self):
        return len(self.zip.namelist())

    def get_one_file(self):
        for name in self.zip.namelist():
            yield self.read_lines(name)  # 生成器

    def read_lines(self, name):
        return [line.decode() for line in self.zip.open(name).readlines()]

    def read_all(self, name):
        return self.zip.open(name).read()

    def get_filenames(self):
        return self.zip.namelist()

    def extract_to(self, path):
        self.zip.extractall(path)
        return path

    def deflated_to(self, files):
        for file in files:
            self.zip.writestr(file.filename, file.file.read(), zipfile.ZIP_DEFLATED)
        self.zip.close()
        return False

    def get_file_by_type(self, end_name):
        files = []
        for file_name in self.get_filenames():
            if file_name == 'overview.json':
                continue
            if file_name.endswith(end_name):
                files.append(file_name)
        return files
