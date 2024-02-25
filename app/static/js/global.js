const toggle = button => {
    fetch('/create/' + button.innerHTML)
        .then(res => res.json())
        
    fetch('/toggle/' + button.innerHTML)
        .then(res => res.json())
        .then(item => {
            const itemElement = document.querySelector(`[data-item-index="${item.index}"]`)
            itemElement.style.backgroundColor = 'green';
    })
}

// Get pool of items and dispaly in display element
const getPool = () => {
    fetch('/getPool')
        .then(res => res.json())
        .then(pool => {
            const display = document.querySelector('.display');

            let index = 0;
            for(const item of pool){
                item_element = document.createElement('p');
                item_element.innerHTML = item.name;
                item_element.classList.add(item.status);
                item_element.setAttribute('data-item-index', index)
                index++;
                display.appendChild(item_element);
            }
        })
}