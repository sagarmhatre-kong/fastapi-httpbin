
# FastAPI Httpbin + OpenAPI specifications generation with Kong specific annotations

## Adding Server

- The code  [Adding servers to the openapi spec](https://github.com/sagarmhatre-kong/fastapi-httpbin/commit/2b22982222c153be2c13a70ff48aeafa5787f2f9) will generate an openapi spec which the [deck file `openapi2kong` ](./openapi-spec/deck.sh) command will translate to one service with the upstream url  in the specification

```yaml
servers:
- description: Local server
  url: http://host.docker.internal:8080
```

## Adding plugins

`openapi2kong` allows you to configure plugins directly in your OpenAPI specification by providing an `x-kong-plugin-PLUGIN-NAME` annotation at the root level to add it to the Service, at the path level to add it to all Routes on that path, or on an operation to add it to a specific Route.

To understand how to modify your python code to generate these annotations, refer the below commits : 
- Adding [Correlation ID](https://developer.konghq.com/plugins/correlation-id/) plugin [to a route](https://github.com/sagarmhatre-kong/fastapi-httpbin/commit/afeb80688659bf3c7d35cfe66848b795caf0c5b8) 
- Adding Dynamic [request-validator plugin](https://developer.konghq.com/plugins/request-validator/) configuration [to a route ](https://github.com/sagarmhatre-kong/fastapi-httpbin/commit/aeefe8277ba9a4b2c2ee3a3f01b66820a121cfd8#diff-979f6e33a76c7421322f1141e867057d533ed44cbddaa8d901dd6b5fa4c07066R13-R60)
  - this tells openapi2kong to automatically inject the schema for the current endpoint when generating a Kong Gateway declarative configuration file so that the plugin applies the validation appropriately for each request 

## Further Reading
- [Adding plugins](https://developer.konghq.com/deck/file/openapi2kong/#adding-plugins)

## Acknowledgements

This code has been forked from https://github.com/dmuth/fastapi-httpbin