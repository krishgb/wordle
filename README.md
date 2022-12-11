# wordle

Extracts the solution data for wordle game ( requires [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi) extension )

The code is 
```js
  for(let i of $r.hooks) 
    if(!i.name.length) {
      console.log(i.subHooks[1].subHooks[4].value.api.solution.data.solution)
      break
    }
```


#### Run it on Console window
- wordle.py will automatically send the solution to a Whatsapp group ( They banned me )
- It will work on your system but you should give the correct dimensions to the python code
  - React component position
  - In components, Ki component position
  - Web Whatsapp pinned chat position
