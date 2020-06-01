## Updating library from swagger

```
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate \
    -i /local/swagger.yaml \
    -l python \
    -o /local/ \
    -DpackageName=defectdojo_api_swagger
```