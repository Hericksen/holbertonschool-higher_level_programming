## **1 Using curl to Interact with APIs**
### **1.1 Installing and Running curl**
- Install curl (`apt install curl` on Linux, `brew install curl` on MacOS, or download it for Windows).
- Verify installation with:
  ```sh
  curl --version
  ```

### **1.2 Fetching Data from an API**
Retrieve posts from JSONPlaceholder:
```sh
curl https://jsonplaceholder.typicode.com/posts
```

### **1.3 Fetching Headers Only**
```sh
curl -I https://jsonplaceholder.typicode.com/posts
```

### **1.4 Making a POST Request**
Send data to an API:
```sh
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

## **2. Conclusion**
Master **curl** for API testing and debugging. 🚀

q
