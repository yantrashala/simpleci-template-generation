# simpleci-template-generation

#Docker build 
docker build -t simpleci-template-generation:1.0 . 

# Docker Run command 
docker run -d -p 0.0.0.0:8000:8000 -v /opt:/opt/output simpleci-template-generation:1.0

# Access http://127.0.0.1:8000/