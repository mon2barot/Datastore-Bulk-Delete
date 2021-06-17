from googleapiclient.discovery import build
import base64
import google.auth
import os
import datetime
def hello_pubsub(event, context):
    if 'data' in event:
        message = base64.b64decode(event['data']).decode('utf-8')
    else:
        message = 'hello world!'
    (credentials, _) = google.auth.default()
    service = build('dataflow', 'v1b3', credentials=credentials)
    gcp_project = 'enter your gcp project name here'
    template_path = \
        'gs://dataflow-templates/latest/Datastore_to_Datastore_Delete'
    template_body = {'jobName': 'enter a job name here',
                     'environment': {'tempLocation': 'gs://abcd/temp',
                     'ipConfiguration': 'WORKER_IP_UNSPECIFIED',
                     'additionalExperiments': []},
                     'parameters': {'datastoreReadGqlQuery': "Enter a GQL query here, e.g SELECT * FROM MyKind",
                     'datastoreReadProjectId': 'gcp project id',
                     'datastoreDeleteProjectId': 'gcp project id'}}
request = \
        service.projects().templates().launch(projectId=gcp_project,
            gcsPath=template_path, body=template_body)
    response = request.execute()
    return 'Done'
