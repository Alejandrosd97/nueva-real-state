console.log('hola')
var contactFormMessage = document.getElementById('owner-contact-form')

function messageConfirmation(){
    alert('The message has been sent to the owner');
    console.log('mensaje confirmado')
}

contactFormMessage.addEventListener('submit', messageConfirmation)


var myLatlng = new google.maps.LatLng(-25.363882,131.044922);
var mapOptions = {
  zoom: 4,
  center: myLatlng
}
var map = new google.maps.Map(document.getElementById("map"), mapOptions);
// Place a draggable marker on the 
console.log(map)
var marker = new google.maps.Marker({
    position: myLatlng,
    map: map,
    draggable:true,
    title:"Drag me!"
});



const showCarouselButton = document.getElementById('show-carousel')
const carousel = document.getElementById('carousel')
const arrows = document.getElementById('arrows')


function showCarousel(){
    console.log(1111)
    carousel.classList.remove('hidden')
    arrows.classList.remove('hidden')
    console.log(2222)
}

showCarouselButton.addEventListener('click', showCarousel)




const likeButton = document.getElementById('like-button')

likeButton.value = 'like'




