its simply shows  how django rest framework works within elastic search
in this tutorial we assume that we installed elastic search 6.8

we are using elastic dsl drf and elastic dsl to implement the elastic search in drf

before running you need to index  elastic search by  python manage.py search_index --rebuild
####its perform a suggest searching :
127.0.0.1:8000/tasker/task/suggest/?title_suggest__completion=yourtitle
