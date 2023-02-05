


export function ErrorBox({error}){

    return(
        <div>
            <p>Error while trying to connect!</p>
            <p>Code: ${error.status}</p>
            <p>Message: ${error.statusText}</p>
        </div>
    )

}

