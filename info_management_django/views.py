from django.shortcuts import render
from . import stu_info_dao
from .entity.StudentInfo import StudentInfo


def hello(request):
    return render(request, 'hello.html')


def get_stu_info(request):
    data_list = []
    for row in stu_info_dao.get_stu_info():
        stu = StudentInfo(row[0], row[1], row[2], row[3], row[4], row[5])
        data_list.append(stu)
    return render(request, 'stu_info.html', {'list': data_list})
