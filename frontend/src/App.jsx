import { useState, useEffect } from "react";
import useFetch from "react-fetch-hook";

import {ErrorBox} from "./components/ErrorBox";

const backend = 'http://localhost:8000/items/1'

function App() {

  const { isLoading, data, error} = useFetch(backend);

  if(isLoading) return "Loading...."
  if(error) return <ErrorBox error={error}/>

  console.log(data)
  return (
      <div className="flex flex-col items-center justify-center h-screen">
        <div className="text-xl underline"> The list is here</div>
        <h1 className="text-lr ">
          <ul>
            {data.map((data) => (
              <li key={data.id}> 
                <p>{data.title}</p>
              </li>
            ))}
          </ul>
        </h1>
      
      </div>
  )
}

export default App
