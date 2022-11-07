from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from zipOP import MZipFile
import time
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    # max_age=1000
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api/overview/")
async def overview(title: str = ''):
    ZIP = MZipFile(f"zip_files/{title}.zip")
    OverView = ZIP.read_all('overview.json')
    view = eval(OverView)
    view['id'] = title
    return view


@app.get("/api/overview/process")
async def overview_process(title: str = ''):
    os.system(f'java -jar jplag.jar other_files/{title} -l cpp -r zip_files/{title} -s other_files/{title}')
    ZIP = MZipFile(f"zip_files/{title}.zip")
    OverView = ZIP.read_all('overview.json')
    view = eval(OverView)
    view['id'] = title
    return True


@app.get("/api/overview/submission")
async def overview_submission(title: str = ''):
    ZIP = MZipFile(f'zip_files/{title}.zip')
    files = ZIP.get_file_by_type('json')

    submission_user = set()
    submission_result = []
    submission_map = {}
    for file_name in files:
        content = ZIP.read_all(file_name)
        content = eval(content)
        del content['matches']
        submission_map[content['id1']] = submission_map.get(content['id1'], {})
        submission_map[content['id1']][content['id2']] = content['similarity']
        submission_map[content['id2']] = submission_map.get(content['id2'], {})
        submission_map[content['id2']][content['id1']] = content['similarity']
        submission_user.add(content['id1'])
        submission_user.add(content['id2'])
        submission_result.append(content)
    submission_result.sort(key=lambda x: x['similarity'], reverse=True)
    submission_user = list(submission_user)
    submission_total = {it: {'total': 0, 'count': 0} for it in submission_user}
    for con in submission_result:
        submission_total[con['id1']]['total'] += con['similarity']
        submission_total[con['id1']]['count'] += 1
        submission_total[con['id2']]['total'] += con['similarity']
        submission_total[con['id2']]['count'] += 1
    submission_total = [{'name': it, 'result': submission_total[it]['total'] / submission_total[it]['count']}
                        for it in submission_user]
    return {
        'submission_user': submission_user,
        'submission_total': submission_total,
        'submission_map': submission_map,
        'submission_result': submission_result
    }


@app.post("/api/overview/upload")
async def overview_upload(file: List[UploadFile] = File(...), title: str = Form(...)):
    file = file[0]
    path = f'other_files/{title}'
    if not os.path.exists(path):
        os.mkdir(path)
    path = path + '/' + file.filename
    with open(path, 'wb') as f:
        f.write(file.file.read())
    return title


@app.post("/api/overview/zip")
async def overview_zip(files: List[UploadFile] = File(...)):
    # t = int(time.time())
    # zz = MZipFile('zip_files/%s.zip' % t, 'w')
    # zz.deflated_to(files)
    # ZIP = MZipFile('zip_files/%s.zip' % int(t))
    # OverView = ZIP.read_all('overview.json').decode()
    # view = eval(OverView)
    # view['id'] = int(t)
    return True


@app.get("/api/overview/sourceFile")
async def overview_source(file: str = '', first: str = '', second: str = ''):
    ZIP = MZipFile('zip_files/%s.zip' % file)
    file1 = ZIP.read_all('submissions/%s/%s' % (first, first))
    file2 = ZIP.read_all('submissions/%s/%s' % (second, second))
    return {
        'first_submission': file1,
        'second_submission': file2,
    }


if __name__ == '__main__':
    zip = MZipFile("zip_files/1667641300409.zip")
    # overview = zip.read_all('submissions/21新生赛-来孟阳_E.txt/21新生赛-来孟阳_E.txt')
    print(zip.get_filenames())
