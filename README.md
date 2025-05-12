# FastAPI Production App



# how  to  run
1- Build   the  docker  image:
....bash  and  tranmnal  for   vs code
docker build -t prodution-app-fastapi:latest .

2- run  rhe  docker  iamge
....bash  and  tranmnal  for   vs code
docker run -p 80:80 prodution-app-fastapi:latest


# Dependencies  

.( Docker ,  DB  ,  Redis  ,fastapi ,  nginx )

- Docker  ( compose ,   dockerfile  )
- Postgresql  database
- Redis  (optional for  caching )  
-nginx ( reverse proxy  )

## 📊 Architecture Diagram
```mermaid
flowchart LR
    User -->|HTTP| NGINX
    NGINX -->|Forward| FastAPI
    FastAPI -->|Queries| PostgreSQL

## 🛡️ Security Scan (Trivy)

...  run  trivy  
trivy image prodution-app-fastapi:latest


