# Updating python code for OpenAPI specs with Kong Annotations

Adding [Correlation ID](https://developer.konghq.com/plugins/correlation-id/) plugin to a route
![alt text](<img/Screenshot 2025-10-25 at 8.53.15 AM.png>) 

Adding a class for Json body validations
![alt text](<img/Screenshot 2025-10-25 at 9.20.34 AM.png>) 

Adding Dynamic [request-validator plugin](https://developer.konghq.com/plugins/request-validator/) configuration to a route

![alt text](<img/Screenshot 2025-10-25 at 9.21.01 AM.png>) 

The class results into a component.schema
![alt text](<img/Screenshot 2025-10-25 at 9.22.00 AM.png>) 

... referenced by the requestBody 
![alt text](<img/Screenshot 2025-10-25 at 9.23.32 AM.png>) 
... also, the oas contains the kong plugin 

The kong.yaml with plugin
![alt text](<img/Screenshot 2025-10-25 at 9.25.34 AM.png>) 

Request validation plugin in action ...
![alt text](<img/Screenshot 2025-10-25 at 9.26.49 AM.png>)