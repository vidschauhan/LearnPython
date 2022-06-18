# Created by vidit.singh at 16-06-2022

import json
import pandas as pd
import src.utils.datasets as ds

base_dir = ds.base_dir()

course = {'course_name': 'Programming using Python',
          'course_author': 'Bob Dillon',
          'course_status': 'published',
          'course_published_dt': '2020-09-30'}

print((json.dumps(course)))
print(type(json.dumps(course)))  # converts json to string format

print("******************************************************")
courses = [{'course_name': 'Programming using Python',
            'course_author': 'Bob Dillon',
            'course_status': 'published',
            'course_published_dt': '2020-09-30'},
           {'course_name': 'Data Engineering using Python',
            'course_author': 'Bob Dillon',
            'course_status': 'published',
            'course_published_dt': '2020-07-15'},
           {'course_name': 'Data Engineering using Scala',
            'course_author': 'Elvis Presley',
            'course_status': 'draft',
            'course_published_dt': None},
           {'course_name': 'Programming using Scala',
            'course_author': 'Elvis Presley',
            'course_status': 'published',
            'course_published_dt': '2020-05-12'},
           {'course_name': 'Programming using Java',
            'course_author': 'Mike Jack',
            'course_status': 'inactive',
            'course_published_dt': '2020-08-10'},
           {'course_name': 'Web Applications - Python Flask',
            'course_author': 'Bob Dillon',
            'course_status': 'inactive',
            'course_published_dt': '2020-07-20'},
           {'course_name': 'Web Applications - Java Spring',
            'course_author': 'Mike Jack',
            'course_status': 'draft',
            'course_published_dt': None},
           {'course_name': 'Pipeline Orchestration - Python',
            'course_author': 'Bob Dillon',
            'course_status': 'draft',
            'course_published_dt': None},
           {'course_name': 'Streaming Pipelines - Python',
            'course_author': 'Bob Dillon',
            'course_status': 'published',
            'course_published_dt': '2020-10-05'},
           {'course_name': 'Web Applications - Scala Play',
            'course_author': 'Elvis Presley',
            'course_status': 'inactive',
            'course_published_dt': '2020-09-30'},
           {'course_name': 'Web Applications - Python Django',
            'course_author': 'Bob Dillon',
            'course_status': 'published',
            'course_published_dt': '2020-06-23'},
           {'course_name': 'Server Automation - Ansible',
            'course_author': 'Uncle Sam',
            'course_status': 'published',
            'course_published_dt': '2020-07-05'}]

# To write json in single json document each line.
output_dir = ds.output_dir()
file_obj = open(output_dir + '\\courses.json', 'w')

for item in courses:
    json.dump(item, file_obj)  # Writing one JSON at a time
    file_obj.write('\n')  # we need to add new line character after each JSON document in the file.

file_obj.close()

print(pd.read_json(output_dir + '\\courses.json', lines=True))
