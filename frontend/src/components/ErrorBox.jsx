


export function ErrorBox({error}){

    return(
        <div>
        <p>Code: ${error.status}</p>
        <p>Message: ${error.statusText}</p>
        </div>
    )

}

