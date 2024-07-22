fetch('https://disease.sh/v3/covid-19/countries/india')
.then((response) => {
  return response.json();
})
.then((data) => {
  console.log(data);
    document.getElementById("active").innerHTML = data.active.toLocaleString();
    document.getElementById("total").innerHTML = data.cases.toLocaleString();
    document.getElementById("deaths").innerHTML = data.deaths.toLocaleString();
    document.getElementById("recovered").innerHTML = data.recovered.toLocaleString();
});

function remClass(x, str){
  x.classList.remove("bg-dark");
  x.classList.remove("text-light");
  x.classList.add(str);
}
function adClass(x, str){
  x.classList.remove(str);
  x.classList.add("bg-dark");
  x.classList.add("text-light");

}


// Scrolll TO Top
$(document).ready(function(){
	$(window).scroll(function () {
			if ($(this).scrollTop() > 50) {
				$('#back-to-top').fadeIn();
			} else {
				$('#back-to-top').fadeOut();
			}
		});
		// scroll body to 0px on click
		$('#back-to-top').click(function () {
			$('body,html').animate({
				scrollTop: 0
			}, 100);
			return false;
		});
});

$(document).ready(function(){
	$('.toggle').click(function(){
	  $('.sidebar-contact').toggleClass('active')
	  $('.toggle').toggleClass('active')
	})
  })
