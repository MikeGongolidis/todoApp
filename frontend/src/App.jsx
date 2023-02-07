import { useState, useEffect } from "react";

import {ErrorBox} from "./components/ErrorBox";
import { AddTaskForm } from "./components/AddTaskForm";
const backend = 'http://localhost:8000/items/user_id'

function App() {

  const [user,setUser] = useState(1);
  const [data,setData] = useState()
  const [loading,setLoading] = useState(true)
  const [error,setError] = useState()

  useEffect( ()=>{
    fetch(backend.replace('user_id',user))
    .then(response=>{
      if(response.ok){
        return response.json()
      }
      throw response;
    })
    .then(dd => {
      setData(dd)
    })
    .catch( error => {
      setError(error)
    })
    .finally( () => {
      setLoading(false)
    })
  },[])

  if(loading) return "Loading...."
  if(error) return <ErrorBox error={error}/>

  return (
      <>
      <div className="flex items-center justify-center ">
        <button onClick={()=> setUser(1)}>User 1</button>
        <button onClick={()=> setUser(2)}>User 2</button>
      </div>
      <div className="flex flex-col items-center justify-center h-screen">
        <div className="text-xl underline"> The list is here</div>
        
        <AddTaskForm user={user} data={data} setData={setData}/>
        <h1 className="text-lr ">
          <ul>
            {data.map((d) => (
              <li key={d.id}> 
                <p>{d.title}</p>
              </li>
            ))
            }
          </ul>
        </h1>  
      </div>
      </>
  )
}

export default App
