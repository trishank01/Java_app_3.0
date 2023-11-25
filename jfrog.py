#!/usr/bin/env python3


import requests
import subprocess

def jfrogUpload():
    #Define the URL, file path , and auth credentials
    url = '',
    file_path = '',
    username = '',
    password = '',

   # Send the PUT request with auth and file upload
   with open(file_path , 'rb') as file:
    response = requests.put(url , auth=(username , password) , data=file)

   # check the response status code
   if response.status_code == 201:
        print("\nPUT request was successful!")
   else: 
         print(f"PUT request failed with status code {response.status_code}")
         print("Response content")

def mvnBuild():
      maven_command = "mvn clean install -DskipTests"

      try:
            subprocess.run(maven_command , check=True , text=True , shell=True)
            print("\nMaven build completed successfully")
      except subprocess.CalledProcessError as e:
            print(f"Error: Maven build failed with exit code {e.returncode}")


def main():
      jfrogUpload()

if __name__ == "__main__":
      main()