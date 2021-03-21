const clientId = config.clientId;
const query = "day"
const url = `https://api.unsplash.com/search/photos?client_id=${clientId}&query=${query}`
const body = document.querySelector('body')

const bgScore =document.querySelector('.bgScore');


async function getPhoto(url){
    const request = await fetch(url);
    const response = await request.json();
    const len = response.results.length;
    const index = Math.floor(Math.random() * Math.floor(len));
    const imgUrl = response.results[index].urls.regular;
    console.log(imgUrl)
    body.style.backgroundImage = `url(${imgUrl})`;
    
}

getPhoto(url);
bgScore.volume = 0.1;


