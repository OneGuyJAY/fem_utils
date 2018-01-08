import os, re

from fem_utils import common_utils


def is_abaqus_ext(ext):
    return ext in ['.inp']


def is_abaqus_fname(fname):
    _, ext = os.path.splitext(fname)
    return is_abaqus_ext(ext.lower())


def get_include_files(fpath):
    include_files = list()

    basedir = os.path.dirname(fpath)
    with open(fpath, 'r') as fp:
        while 1:
            line = fp.readline()
            if not line:
                break

            if line.startswith('*INCLUDE'):
                fields = line.split(',')
                if len(fields) > 1:
                    item = fields[-1].split('=')[-1].strip()
                    include_files.append(common_utils.get_abspath(basedir, item))

    return include_files

def is_nastran_file(fpath):
    if is_abaqus_fname(fpath):
        return True
    return is_abaqus_file_by_content(fpath)


def is_abaqus_file_by_content(fpath):
    with open(fpath, 'r+') as fp:
        f_content_line_list = fp.readlines()
        for line in f_content_line_list:
            if line.startswith('*NODE') or line.startswith('*node'):
                # compare the following five lines, because ls-dyna file also has the same *node keyword
                index = f_content_line_list.index(line)
                i = 1
                while i <= 5:
                    new_ind = index + i
                    new_line = f_content_line_list[new_ind].strip()
                    if re.match(r'^\d(.+?)', new_line) and re.search(r',', new_line):
                        return True
                    i += 1
            if line.startswith('*INCLUDE') or line.startswith('*include'):
                wordsInLine_list = line.split(',')
                if re.match(r'''(.+?)=(.+?)\.inp$''', wordsInLine_list[1].strip()):
                    return True

    return False



if __name__ == "__main__":
    fpath = 'D:/Models/V0-futian_spring_25Feb05.inp/tttt'
    print(is_nastran_file(fpath))
