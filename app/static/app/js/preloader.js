// preloader
(function () {

	init();
	function init() {
		// disable scrolling
		window.addEventListener("scroll", noscroll);

		// initial animation
	}

	show_homepage();

	function show_homepage() {
		if (isMobile() == true) {
			$("html").addClass("is-mobile");
		} else {
			$("html").addClass("desktop");
		}
		setTimeout(function () {
			window.removeEventListener("scroll", noscroll);
		}, 2000);
		if (getOS() == "Windows") {
			$("html").addClass("windows");
		} else {
			$("html").addClass("notWindows");
		}
		setTimeout(() => {
			locomotiveScroll();
		}, 1000);
	}

	function noscroll() {
		window.scrollTo(0, 0);
	}
})();


// Detect Windows
function getOS() {
	var userAgent = window.navigator.userAgent,
		platform = window.navigator.platform,
		macosPlatforms = ["Macintosh", "MacIntel", "MacPPC", "Mac68K"],
		windowsPlatforms = ["Win32", "Win64", "Windows", "WinCE"],
		iosPlatforms = ["iPhone", "iPad", "iPod"],
		os = null;

	if (macosPlatforms.indexOf(platform) !== -1) {
		os = "Mac OS";
	} else if (iosPlatforms.indexOf(platform) !== -1) {
		os = "iOS";
	} else if (windowsPlatforms.indexOf(platform) !== -1) {
		os = "Windows";
	} else if (/Android/.test(userAgent)) {
		os = "Android";
	} else if (!os && /Linux/.test(platform)) {
		os = "Linux";
	}
	return os;
}

// Check resolution

var viewport = $(window).width();
function isMobile() {
	viewport = $(window).width();
	var isMobile;
	if (viewport < 1023) {
		isMobile = true;
	} else {
		isMobile = false;
	}
	return isMobile;
}

// locomotive-scroll init
function locomotiveScroll() {
	if ($("html").hasClass("windows")) {
		this.scroll = new LocomotiveScroll({
			el: document.querySelector("[data-scroll-container]"),
			smooth: true,
			class: "is-inview",
			getDirection: true,
		});
	} else {
		this.scroll = new LocomotiveScroll({
			el: document.querySelector("[data-scroll-container]"),
			class: "is-inview",
			getDirection: true,
		});
	}

	// show / hide nav on scroll
	scroll.on("scroll", (instance) => {
		document.documentElement.setAttribute("data-direction", instance.direction);
	});

	scroll.on("scroll", ({ limit, scroll }) => {				
		if (scroll.y > 400) {			
			$(".trowel-img").addClass("anim");
		} else {
			$(".trowel-img").removeClass("anim");
		}
	});

	// refresh website or update scroll scripts on window resize
	$(window).resize(function () {
		windowResizer();
	});

	function windowResizer() {
		// Check if the window width has actually changed and it's not just iOS triggering a resize event on scroll
		if ($(window).width() != viewport) {
			// Update the window width for next time
			viewport = $(window).width();
			if (isMobile() == true) {
				if (!$("html").hasClass("is-mobile")) {
					window.location.reload();
				} else {
					this.scroll.update();
				}
			} else {
				if ($("html").hasClass("is-mobile")) {
					window.location.reload();
				} else {
					this.scroll.update();
				}
			}
		}
	}
}