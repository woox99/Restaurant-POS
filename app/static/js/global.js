const toggle = button => {
    // console.log(button.innerHTML)
    fetch('/create/' + button.innerHTML)
        .then(res => res.json())
}

const getPool = () => {
    fetch('/getPool')
        .then(res => res.json())
        .then(pool => {
            console.log(pool)
            
            // Create item elements here
        })
}