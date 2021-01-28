# CloudGuard GCP API Enabler Tool

## What does it do?

In order to onboard GCP projects into CloudGuard (formerly Dome9), there are some pre-requisites around enabling APIs in the project environment. This enables both this tool and the onboarder tool to access the project properly and onboard it into CloudGuard.

## Which APIs are enabled?

The following APIs are enabled :-

  - Compute Engine
  - Resource Management
  - Cloud API
  
All three are required, regardless of whether or not you use the Compute Engine service. This is a design constraint on the GCP side as has nothing to do with CloudGuard.

## How do I use the API Enabler?

1. Download, install and configure **Python (3.8 or higher)**
2. Download and install **git**
3. Run **git clone https://github.com/chrisbeckett/cg-gcp-apienabler.git**
4. Run **python3 -m venv cg-gcp-apienabler**
5. Run **cd cg-gcp-apienabler**
6. Run **python3 cg-gcp-apienabler**
7. Feel good

## Can/should I use this in conjunction with the onboarding tool?

**Absolutely.** You can run this tool as a Google Function and schedule it to run prior to the scheduled Onboarder tool run. This way, any new projects created in the G-Suite Organisation have the required APIs enabled prior to the automated onboarding process. It is not currently a consolidated tool as the Compute Engine API can sometimes take a couple of minutes to enable and this caused race conditions in testing. Further down the line, I intend to merge the two tools.
