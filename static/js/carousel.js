$(document).ready(function(){

$('.items').slick({
arrows:false,
infinite: true,
speed: 1000,
autoplay: true,
autoplaySpeed: 2000,
slidesToShow: 4,
slidesToScroll: 1,
responsive: [
{
breakpoint: 1024,
settings: {
slidesToShow: 3,
slidesToScroll: 3,
infinite: true,
dots: true
}
},
{
breakpoint: 600,
settings: {
slidesToShow: 2,
slidesToScroll: 2
}
},
{
breakpoint: 480,
settings: {
slidesToShow: 1,
slidesToScroll: 1
}
}

]
});
});
