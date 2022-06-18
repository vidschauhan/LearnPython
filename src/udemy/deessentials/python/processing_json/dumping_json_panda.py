# Created by vidit.singh at 16-06-2022

import json
import pandas as pd
import src.utils.datasets as ds

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

# Dumping a JSON documents into a file with one JSON document per line.

coursed_df = pd.DataFrame(courses)
coursed_df.to_json(ds.output_dir() + '\\courses_pandas.json', orient='records',
                   lines=True)  # To write valid json in each line

coursed_df.to_json(ds.output_dir() + '\\courses_pandas_string_json.json',
                   orient='records')  # To json string as list of string

coursed_df.to_json(ds.output_dir() + '\\courses_pandas_split_index_cols.json',
                   orient='split')  # To write json in split format.
