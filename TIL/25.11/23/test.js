const persons = [
    {name: 'tt', age: 1},
    {name: 'ww', age: 2},
]

const result = persons.map(function(person){
    return person.name
})

console.log(result)