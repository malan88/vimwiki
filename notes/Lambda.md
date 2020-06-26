- You have to package your installed dependencies alongside your own code
    - Boto3, for accessing dynamodb is automatically included
    - urllib3 is included (requests is deprecated)
- to deploy, package everything as a zip file and deploy it using the following
  command to the aws cli:
  `aws lambda update-function-code --function-name john-and-abigail --zip-file fileb://lambda.zip`
- Permissions have to be granted to access any other services, just like any
  other aws service.
- Triggers can be almost anything. For time triggers, use cloudwatch events
- logging is automatic
- You can run an absurd amount of times for dirt freaking cheap.
