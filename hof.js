// let arr=[1,2,3,4,5,6,7]
// const arr2=arr.map((i) =>{
//     return Math.pow(i,2)
// })
// console.log(arr2)

const Object1 = {
    "name": "A",
    "id": 1
}
const Object2 = {
    "name": "B",
    "id": 2
}
const Object3 = {
    "name": "C",
    "id": 3
}
const Object4 = {
    "name": "D",
    "id": 4
}
const Object5 = {
    "name": "E",
    "id": 5
}
const object6 = { ...Object5, id: Object5.id+9}
console.log(object6);
const sub =(e)=>{
    console.log(e.target.value);
}
// arr.push(Object1)
// arr.push(Object2)
// arr.push(Object3)
// arr.push(Object4)
// arr.push(Object5)
// console.log(arr);

