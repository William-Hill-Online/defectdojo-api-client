## Updating library from swagger

```
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate \
    -i /local/swagger.json \
    -l python \
    -o /local/ \
    -DpackageName=defectdojo_api_swagger
```

There a bug running swaggerapi/swagger-codegen-cli https://github.com/swagger-api/swagger-codegen/issues/9538. 
So we need replace double backslash by single backslash in regex

Files:
- defectdojo_api_swagger/models/finding.py
- defectdojo_api_swagger/models/finding_create.py
- defectdojo_api_swagger/models/finding_template.py
- defectdojo_api_swagger/models/user.py