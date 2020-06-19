import os
import json

from flask import render_template, safe_join

from app import app as application


def get_projects():
    projects = {}
    for root, dirs, files in os.walk(os.path.join(application.static_folder, 'projects/')):
        for file in files:
            data = {}
            with open(os.path.join(root, file), 'r') as f:
                data = json.loads(f.read())

            projects[file.split('.')[0]] = data

    return projects


@application.route('/')
def index():
    return render_template('index.html', projects=get_projects())


@application.route('/project/<project_name>')
def project(project_name):
    return render_template('project.html', project=project_name, projects=get_projects())
