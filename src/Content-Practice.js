
import React from 'react'
import { useState } from 'react';

const Content = () => {

  const [name, setName] = useState('Abhi')
  const [count, setCount] = useState(0)

  const increaceCount=()=>{
    let temp = count
    temp+=1
    setCount(temp)
  }
  const decreaseCount=()=>{
    let temp = count
    temp-=1
    setCount(temp)
  }

    const handleNameChange = ()=>{
        const names= ['Bob', 'kevin', 'dave'];
        const int = Math.floor(Math.random()*3)
        setName(names[int])
      }

      const handleClick=()=>{
        console.log('Youc Clicked');
      }
      const handleClick2=(name)=>{
        console.log(`${name} was clicked`);
      }
      const handleClick3=(e)=>{
        console.log(e.target.innerText);
      }

  return (
    <main>
        <p onDoubleClick={handleClick}>Hello {name}</p>
        <p onDoubleClick={handleClick}>count is: {count}</p>
        <button onClick={handleNameChange}>Click</button>
        <button onClick={increaceCount}>Increase</button>
        <button onClick={decreaseCount}>Decrease</button>
        <button onClick={()=>handleClick2('dave')}>Click</button>
        <button onClick={(e)=>handleClick3(e)}>Click</button>
    </main>
  )
}

export default Content