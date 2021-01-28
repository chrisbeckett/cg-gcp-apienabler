## Tool for checking GCP permissions for a Service Account

## You must set the environment variable for the credentials file.
## Example: GOOGLE_APPLICATION_CREDENTIALS='mycredfile.json'

from google.cloud import resource_manager
import sys
import os
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2 import service_account
from pprint import pprint

from pyasn1_modules.rfc2459 import Name

creds_file = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
gcp_client = resource_manager.Client()
gcp_creds = service_account.Credentials.from_service_account_file(creds_file)

service = googleapiclient.discovery.build('cloudresourcemanager', 'v1', credentials=gcp_creds)
service_usage = googleapiclient.discovery.build('serviceusage', 'v1', credentials=gcp_creds)

def enable_gcp_apis():
    try:
        request = service.projects().list()
        response = request.execute()

        for project in response.get('projects', []):
            projname=project['name']
            projid=project['projectId']
            print(f'Project found: {projname}')
            projurl = "projects/" + projid + "/services/"
            
            # Enable the Cloud API
            enable_cloud_api_url = "projects/" + projid + "/services/cloudapis.googleapis.com"
            enable_cloud_api = service_usage.services().enable(name=enable_cloud_api_url).execute()
            enable_cloud_api_status = enable_cloud_api.get("done")
            while enable_cloud_api_status is False:
                print(f"Enabling GCP Cloud API...")
                enable_rm_api_status = enable_cloud_api.get("done")
            
            print(f" {projname} : Cloud API Successfully Enabled")

            # Enable Compute Engine API
            enable_compute_api_url = "projects/" + projid + "/services/compute.googleapis.com"
            enable_compute_api = service_usage.services().enable(name=enable_compute_api_url).execute()
            enable_compute_api_status = enable_compute_api.get("done")
            while enable_compute_api_status is False:
                print(f"Enabling Compute Engine API...")
                enable_compute_api_status = enable_compute_api.get("done")
            
            print(f" {projname} : Compute Engine API Successfully Enabled")

            #Enable Resource Manager API
            enable_rm_api_url = "projects/" + projid + "/services/cloudresourcemanager.googleapis.com"
            enable_rm_api = service_usage.services().enable(name=enable_rm_api_url).execute() #dict
            enable_rm_api_status = enable_rm_api.get("done")
            while enable_rm_api_status is False:
                print(f"Enabling Resource Manager API...")
                enable_rm_api_status = enable_rm_api.get("done")
            
            print(f" {projname} : Resource Manager API Successfully Enabled")
            
            if enable_rm_api_status is False:
                print(f" {projid} : Resource Manager API was not enabled")
            
    except (googleapiclient.errors.HttpError, googleapiclient.errors.InvalidJsonError, googleapiclient.errors.UnknownApiNameOrVersion, googleapiclient.errors.UnexpectedBodyError) as e:
        print("Error : ", e)

if __name__ == "__main__":
    enable_gcp_apis()
