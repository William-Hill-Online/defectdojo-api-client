## Updating library from swagger

```
export VERSION=<DefectDojo version>
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/swagger.json \
    -g python \
    -o /local \
    --additional-properties packageName=defectdojo_api_client \
    --additional-properties packageVersion=$VERSION \
    --additional-properties projectName=defectdojo-api-client
```
