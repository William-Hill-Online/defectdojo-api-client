## Updating library from swagger

```
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/swagger.json \
    -g python \
    -o /local \
    --additional-properties packageName=defectdojo_openapi
```
