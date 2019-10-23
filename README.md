# howtographql tutorial

https://www.howtographql.com/graphql-python/1-getting-started/

```js

query listUsers{
    users{
      id
      password
      lastLogin
      isSuperuser
      username
      firstName
      lastName
      email
      isStaff
      isActive
      dateJoined
    }
}
```

```js
query listUsers{
    users{
      id
      password
      lastLogin
      isSuperuser
      username
      firstName
      lastName
      email
      isStaff
      isActive
      dateJoined
    }
}
```

```js
mutation createUser {
  createUser(email:"airat2@info.ru", password: "Qwerty03", username: "airat2"){
    user{
      id
      password
      lastLogin
      isSuperuser
      username
      firstName
      lastName
      email
      isStaff
      isActive
      dateJoined
    }
  }
}
```

```js
mutation myFistmutation {
  createLink(url:"url link fake2", description: "fake description2"){
    id
    url
    description
  }
}
```

```js
query myFirst {
  links {
    id
    url
    description
  }
}
```

```js
mutation createUser {
  createUser(email:"airat2@info.ru", password: "Qwerty03", username: "airat2"){
    user{
      id
      password
      lastLogin
      isSuperuser
      username
      firstName
      lastName
      email
      isStaff
      isActive
      dateJoined
    }
  }
}
```

```js
mutation myFistmutation {
  createLink(url:"url link fake2", description: "fake description2"){
    id
    url
    description
  }
}
```

```js
query myFirst {
  links {
    id
    url
    description
  }
}
```

