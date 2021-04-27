$(window).on("load", function () {
	if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
		$("body").addClass("ios");
	} else {
		$("body").addClass("web");
	}

	var isshow = localStorage.getItem("isshow");
	if (isshow == null) {
		localStorage.setItem("isshow", 1);
		$(".popup-cookies").addClass("active");
	}

	var counter = 0;
	var count = 0;
	var i = setInterval(function () {
		$(".load-screen__count").html(count);
		$(".load-screen__line").css("width", count + "%");
		counter++;
		count++;
		if (counter > 5) {
			$(".load-screen__wr").addClass("active");
		}
		if (counter == 101) {
			$(".load-screen__line").fadeOut(500);
			$("body").removeClass("loaded");
			$("body").addClass("load");
			clearInterval(i);
		}
	}, 10);

});

/* viewport width */
function viewport() {
	var e = window,
		a = "inner";
	if (!("innerWidth" in window)) {
		a = "client";
		e = document.documentElement || document.body;
	}
	return { width: e[a + "Width"], height: e[a + "Height"] };
}
/* viewport width */

$(function () {
	/* placeholder*/
	$("input, textarea").each(function () {
		var placeholder = $(this).attr("placeholder");
		$(this).focus(function () {
			$(this).attr("placeholder", "");
		});
		$(this).focusout(function () {
			$(this).attr("placeholder", placeholder);
		});
	});

	/*button open main nav*/
	$(".js-button-menu").toggle(
		function () {
			$(this).addClass("active");
			$(".menu").addClass("show");
		},
		function () {
			$(this).removeClass("active");
			$(".menu").removeClass("show");
			$("html").removeClass("noscroll");
		}
	);

	/*scroll id*/
	$(".js-anchor-id").click(function () {
		$(".js-button-menu").click();
		$("html").removeClass("noscroll");
		return false;
	});

	$(".js-scroll-id").click(function () {
		var targetId = $(this).attr("href");
		$("html, body").animate(
			{
				scrollTop: $(targetId).offset().top - 10,
			},
			500
		);
		return false;
	});

	/*form submit show thank popup*/
	$("#form-callback").submit(function () {
		$(this).parents(".fancybox-wrap").find(".fancybox-close").click();
		$(".js-callback-thank").click();
		return false;
	});
	$("#form-reviews").submit(function () {
		$(this).parents(".fancybox-wrap").find(".fancybox-close").click();
		$(".js-reviews-popup-thank").click();

		return false;
	});
	$("#form-subscribe").submit(function () {
		$(".subscribe-link").click();
		return false;
	});
	$("#form-subscribe-1").submit(function () {
		$(".subscribe-link").click();
		return false;
	});

	/*close popup in popup*/
	$(".js-close-popup").click(function () {
		$(this).parents(".fancybox-wrap").find(".fancybox-close").click();
		return false;
	});

	/*scroll top page*/
	$(".js-top").click(function () {
		window.scrollTo( 0, 0 );
		return false;
	});

	/*close cookies popup*/
	$(".js-cookies-close").click(function () {
		$(".popup-cookies").removeClass("active");
		return false;
	});

	/*show popup map*/
	$(".port-list__link").click(function () {
		$(".map-tooltip").removeClass("active");
		$(".map-tooltip-mask").addClass("active");
		$(this).parent().find(".map-tooltip").addClass("active");
		return false;
	});
	$(".stock-list__link").click(function () {
		$(".map-tooltip").removeClass("active");
		$(".map-tooltip-mask").addClass("active");
		$(this).parent().find(".map-tooltip").addClass("active");
		return false;
	});
	$(".map-tooltip__close").click(function () {
		$(".map-tooltip-mask").removeClass("active");
		$(this).parents(".map-tooltip").removeClass("active");
		return false;
	});
	$(".map-tooltip-mask").click(function () {
		$(".map-tooltip-mask").removeClass("active");
		$(".map-tooltip").removeClass("active");
		return false;
	});

	if ($(".file-img").length) {
		function readURL(input) {
			if (input.files && input.files[0]) {
				var holder = document.getElementById("holder");
				var reader = new FileReader();
				reader.onload = function (e) {
					holder.style.backgroundImage = "url(" + e.target.result + ")";
					$("#holder").addClass("img-active");
				};
				reader.readAsDataURL(input.files[0]);
			}
		}
		$("#imgInp").change(function () {
			readURL(this);
		});
		var holder = $("#holder");
		holder.ondrop = function (e) {
			this.classList.add("img-active");
			e.preventDefault();
			var file = e.dataTransfer.files[0],
				reader = new FileReader();
			reader.onload = function (event) {
				holder.style.backgroundImage = "url(" + event.target.result + ")";
			};
			reader.readAsDataURL(file);
			return false;
		};
	}

	/* components begin*/
	/*TweenLite.defaultEase = Linear.easeNone;
	var controller = new ScrollMagic.Controller();
	var tl = new TimelineMax();
	tl.fromTo(".trowel-img", 1, { x: 0, y: 0 }, { x: -429, y: 100 }, "+=1");
	var scene = new ScrollMagic.Scene({
		triggerElement: "#stage",
		triggerHook: 0.4,
		duration: "100%",
	})
		.setTween(tl)
		.addTo(controller);
*/
	/* products slider */
	if ($(".js-products-slider").length) {
		$(".js-products-slider").slick({
			dots: false,
			infinite: true,
			speed: 300,
			slidesToShow: 3,
			slidesToScroll: 1,
			arrows: true,
			prevArrow: '<button type="button" data-role="none" class="slick-prev" aria-label="Previous" tabindex="0" role="button"><i class="icon-arr-left"></i></button>',
			nextArrow: '<button type="button" data-role="none" class="slick-next" aria-label="Next" tabindex="0" role="button"><i class="icon-arr-right"></i></button>',
			responsive: [
				{
					breakpoint: 1023,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 1,
						arrows: false,
						variableWidth: true,
						centerMode: true,
					},
				},
				{
					breakpoint: 480,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
						arrows: false,
						variableWidth: true,
						centerMode: true,
						dots: true,
					},
				},
			],
		});
	}
	/* steps slider */
	if ($(".js-steps-slider").length) {
		$(".js-steps-slider").slick({
			dots: false,
			infinite: false,
			speed: 300,
			arrows: false,
			responsive: [
				{
					breakpoint: 6000,
					settings: "unslick",
				},
				{
					breakpoint: 1023,
					settings: {
						slidesToShow: 3,
						arrows: false,
						variableWidth: true,
					},
				},
				{
					breakpoint: 480,
					settings: {
						slidesToShow: 1,
						arrows: false,
						variableWidth: true,
						centerMode: true,
					},
				},
			],
		});
	}
	/*reviews slider*/
	if ($(".reviews-slider").length) {
		$(".js-reviews-img").slick({
			arrows: false,
			slidesToShow: 5,
			asNavFor: ".js-reviews-cont",
			infinite: true,
		});
		$(".js-reviews-cont").slick({
			slidesToShow: 1,
			infinite: true,
			fade: true,
			asNavFor: ".js-reviews-img",
			prevArrow: '<button type="button" data-role="none" class="slick-prev" aria-label="Previous" tabindex="0" role="button"><i class="icon-arr-left"></i></button>',
			nextArrow: '<button type="button" data-role="none" class="slick-next" aria-label="Next" tabindex="0" role="button"><i class="icon-arr-right"></i></button>',
			responsive: [
				{
					breakpoint: 767,
					settings: {
						arrows: false,
					},
				},
			],
		});
	}
	/*popup*/
	if ($(".js-fancybox").length) {
		$(".js-fancybox").fancybox({
			margin: 0,
			padding: 0,
			beforeShow: function () {
				if ($(document).height() > $(window).height()) {
					var scrollTop = $("html").scrollTop() ? $("html").scrollTop() : $("body").scrollTop();
					$("html").addClass("noscroll").css("top", -scrollTop);
				}
				$("body").addClass("show-popup");
			},
			afterClose: function () {
				$("html").removeClass("noscroll");
				var scrollTop = parseInt($("html").css("top"));
				$("html,body").scrollTop(-scrollTop);
				$("body").removeClass("show-popup");
				$(".popup-window-cont").removeClass("hidden");
				$(".popup-window-thank").removeClass("active");
				$("#form-callback")[0].reset();
				$("#form-reviews")[0].reset();
				$("#form-subscribe")[0].reset();
			},
		});
	}
	/*styled scroll*/
	if ($(".js-scroll").length) {
		$(".js-scroll").mCustomScrollbar({
			axis: "y",
			theme: "dark-thin",
			autoExpandScrollbar: true,
			advanced: { autoExpandHorizontalScroll: true },
		});
	}

	/*add rating in review form*/
	if ($(".js-rating").length) {
		$(".js-rating").addRating();
	}

	/* components end*/
});

var handler = function () {
	var height_footer = $("footer").height();
	var height_header = $("header").height();
	//$('.content').css({'padding-bottom':height_footer+40, 'padding-top':height_header+40});

	var viewport_wid = $(window).width();
	var viewport_height = $(window).height();

	if (viewport_wid <= 1023) {
		if ($(".js-steps-slider").length) {
			$(".js-steps-slider").slick("getSlick").refresh();
		}
	}
};
$(window).bind("load", handler);
$(window).bind("resize", handler);

$('#form-callback').submit(function(event) {
	event.preventDefault();
	let data = $(this).serializeArray()
	if (data[0].value == "" || data[1].value == ""){}
	else{
		// var count_product = $('.irs-single').text()
		// data['4'] = {'name':'count_product', 'value': count_product}
		let url = this.action

		// fbq('track', 'Lead', {
		// 	value: data[4]["value"],
		// 		product_type_id: [data[6]['value']],
		// 	name: data[1]["value"],
		// 	phone_number: data[2]["value"]
		// });

		$.post(url, data, function(data) {})
	}
	});

// $('#review-form').submit(function(event) {
// 		event.preventDefault();
//
// 		var stars_container = $('#rating_feedback_container').children('span').children('span').text()
// 		if (stars_container == '-') {stars_container = 0}
// 		var data = $(this).serializeArray()
// 		data[3]['name'] = 'rating'
// 		data[3]['value'] = stars_container
// 		var url = this.action
// 		//$.post(url,data, function(data) {})
// 		$.ajaxSetup({
// 		  url: url,
// 		  type: 'POST',
// 		  dataType: 'json',
// 		  beforeSend: function(){},
// 		  error: function(req, text, error){},
// 		  complete: function(){}
// 		});
// 	    var $that = $(this),
// 	    formData = new FormData($that.get(0));
// 	    formData.append('rating', stars_container)
// 	    $.ajax({
// 	      	contentType: false,
// 	      	processData: false,
// 	      	data: formData,
// 	      	success: function(json){
// 	        	if(json){
// 	        	}
// 	      	}
// 	    });
//
// 	});

$('#form-comments').submit(function(event) {
	event.preventDefault();
	// const data = $(this).serializeArray()
	const rating = $(".icon-star.active").length
	// data.push({"name": "rating", "value": rating})
	let url = this.action
	$.ajaxSetup({
		  url: url,
		  type: 'POST',
		  dataType: 'json',
		  beforeSend: function(){},
		  error: function(req, text, error){},
		  complete: function(){}
		});
	var $that = $(this)
	formData = new FormData($that.get(0));
	formData.append('rating', rating)
	// $.post(url, data, function(data) {})
	$.ajax({
	      	contentType: false,
	      	processData: false,
	      	data: formData,
	      	success: function(json){
	        	if(json){
	        	}
	      	}
	    });
	});