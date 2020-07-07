## Updating library from swagger

```
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/swagger.json \
    -g python \
    -o /local \
    --additional-properties packageName=defectdojo_api_client \
    packageVersion=$VERSION projectName=defectdojo-api-client generateSourceCodeOnly=true
```
