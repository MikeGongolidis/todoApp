import React, {useState} from 'react';

const initialFormState = {
    taskName: ""
}

const requestOptions = {

}

export function AddTaskForm({ userId, data, setData}){

    const [formState,setFormState] = useState(initialFormState);
    
    const handleChange = (event) => {
        setFormState({
            ...formState,
            [event.target.id]:event.target.value,
        })
    }

    const handleSubmit = (event) => {
        event.preventDefault();

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify( { id: userId, title: formState.taskName})
        };
        
        fetch('http://localhost:8000/items/user_id'.replace('user_id',userId), requestOptions)
            .then(response => response.json())
            .then(dd =>  {
                setData([
                    dd
                ]);
            }
            );

        setFormState(initialFormState);
    };

    return (
        <form onSubmit={handleSubmit}>
        <div>
            <label htmlFor="taskName">Task Name:</label>
            <input id="taskName" type="text" onChange={handleChange}/>
        </div>
        <button type="submit">Submit</button>
        </form>
    );
};
