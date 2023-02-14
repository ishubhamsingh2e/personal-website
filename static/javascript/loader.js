(function ($) {
    "use strict";
    $(window).on("load", function () {
        $("body").imagesLoaded({}, function () {
            var preload = $(".preloader");
            preload.addClass("loaded");
            preload.find(".centrize").fadeOut();
            initCursor();
            $(".elementor-widget-text-editor").attr("data-animate", "active");
            $(".scroll-animate").scrolla({ once: !0, mobile: !0 });
        });
    });
    $(function () {
        "use strict";
        setHeightFullSection();
        $(window).resize(function () {
            setHeightFullSection();
        });
        $(".js-parallax").jarallax({ speed: 0.65, type: "scroll" });
        if ($(".v-line").length) {
            $(".v-line .elementor-container").append(
                '<div class="v-line-block"><span></span></div>'
            );
            $(".v-line .hero-started").append(
                '<div class="v-line-block"><span></span></div>'
            );
        }
        Splitting();
        if ($(window).width() > 1200) {
            var s = skrollr.init();
        }
        $(".subtitle.subtitle-typed").each(function () {
            var subtitleContainer = $(this);
            subtitleContainer.typed({
                stringsElement: subtitleContainer.find(".typing-title"),
                backDelay: 3500,
                typeSpeed: 0,
                loop: !0,
            });
        });
        if ($(".header").length) {
            $(window).on("scroll", function (event) {
                if ($(window).scrollTop() > 100) {
                    $(".header").addClass("sticky");
                    if (this.oldScroll < this.scrollY) {
                        $(".header").addClass("animate-in");
                    } else {
                        if ($(window).scrollTop() < 200) {
                            $(".header").addClass("animate-out");
                        }
                    }
                } else {
                    $(".header").removeClass("sticky");
                    $(".header").removeClass("animate-in");
                    $(".header").removeClass("animate-out");
                }
                this.oldScroll = this.scrollY;
            });
        }
        function checkScrollDirectionIsUp(event) {
            if (event.wheelDelta) {
                return event.wheelDelta > 0;
            }
            return event.deltaY < 0;
        }
        var skin = $.cookie("skin");
        if (skin == "light") {
            $("body").removeClass("dark-skin");
            $("body").addClass("light-skin");
        }
        if (skin == "dark") {
            $("body").removeClass("light-skin");
            $("body").addClass("dark-skin");
        }
        if ($("body").hasClass("dark-skin")) {
            $(".header .switcher-btn").addClass("active");
        }
        $(".header").on("click", ".switcher-btn", function () {
            if ($(this).hasClass("active")) {
                $(this).removeClass("active");
                $("body").removeClass("dark-skin");
                $("body").addClass("light-skin");
                $.cookie("skin", "light", { expires: 7, path: "/" });
            } else {
                $(this).addClass("active");
                $("body").removeClass("light-skin");
                $("body").addClass("dark-skin");
                $.cookie("skin", "dark", { expires: 7, path: "/" });
            }
            return !1;
        });
        $(".header").on("click", ".menu-btn", function () {
            if ($(this).hasClass("active")) {
                $(this).removeClass("active");
                $(this).addClass("no-touch");
                $(".menu-overlay").addClass("no-touch");
                $("body").removeClass("no-scroll");
                $(".menu-full-overlay").removeClass("is-open");
                $(".menu-full-overlay").removeClass("has-scroll");
                $(".menu-full-overlay").removeClass("animate-active");
                setTimeout(function () {
                    $(".menu-full-overlay").removeClass("visible");
                    $(".menu-btn").removeClass("no-touch");
                    $(".menu-overlay").removeClass("no-touch");
                }, 1);
            } else {
                $(this).addClass("active no-touch");
                $(".menu-overlay").addClass("no-touch");
                var height = $(window).height();
                $(".menu-full-overlay").css({ height: height });
                $("body").addClass("no-scroll");
                $(".menu-full-overlay").addClass("is-open visible");
                setTimeout(function () {
                    $(".menu-full-overlay").addClass(
                        "has-scroll animate-active"
                    );
                    $(".menu-btn").removeClass("no-touch");
                    $(".menu-overlay").removeClass("no-touch");
                }, 1);
            }
            return !1;
        });
        $(".menu-full-overlay").on("click", ".menu-overlay", function () {
            $(".menu-btn").removeClass("active");
            $(".menu-btn").addClass("no-touch");
            $(".menu-overlay").addClass("no-touch");
            $("body").removeClass("no-scroll");
            $(".menu-full-overlay").removeClass("is-open");
            $(".menu-full-overlay").removeClass("has-scroll");
            $(".menu-full-overlay").removeClass("animate-active");
            setTimeout(function () {
                $(".menu-full-overlay").removeClass("visible");
                $(".menu-btn").removeClass("no-touch");
                $(".menu-overlay").removeClass("no-touch");
            }, 1000);
            return !1;
        });
        $(".menu-full").on("click", "a", function () {
            if (!$(this).parent().hasClass("has-children")) {
                $(".header .menu-btn.active").trigger("click");
            }
        });
        $(".menu-full .has-children > a").append(
            '<i class="fas fa-chevron-down"></i>'
        );
        $(".menu-full").on("click", ".has-children > a", function () {
            if ($(this).closest("li").hasClass("opened")) {
                $(this).closest("li").removeClass("opened");
                $(this).closest("li").addClass("closed");
                $(this).closest("li").find("> ul").slideUp();
            } else {
                $(this)
                    .closest("ul")
                    .find("> li")
                    .removeClass("closed")
                    .removeClass("opened");
                $(this).closest("ul").find("> li").find("> ul").slideUp();
                $(this).closest("li").addClass("opened");
                $(this).closest("li").find("> ul").slideDown();
            }
            return !1;
        });
        var swiperServices = new Swiper(".js-services", {
            slidesPerView: 3,
            spaceBetween: 40,
            watchSlidesVisibility: !0,
            noSwipingSelector: "a",
            loop: !1,
            speed: 1000,
            pagination: {
                el: ".swiper-pagination",
                type: "bullets",
                clickable: !0,
            },
            navigation: !1,
            breakpoints: {
                0: { slidesPerView: 1, spaceBetween: 20 },
                767: { slidesPerView: 2, spaceBetween: 30 },
                1024: { slidesPerView: 3, spaceBetween: 40 },
            },
        });
        var swiperTestimonials = new Swiper(".js-testimonials", {
            slidesPerView: 3,
            spaceBetween: 40,
            watchSlidesVisibility: !0,
            noSwipingSelector: "a",
            loop: !1,
            speed: 1000,
            pagination: {
                el: ".swiper-pagination",
                type: "bullets",
                clickable: !0,
            },
            navigation: !1,
            breakpoints: {
                0: { slidesPerView: 1, spaceBetween: 20 },
                767: { slidesPerView: 2, spaceBetween: 30 },
                1024: { slidesPerView: 3, spaceBetween: 40 },
            },
        });
        var $container = $(".works-items");
        $container.imagesLoaded(function () {
            $container.isotope({
                itemSelector: ".works-col",
                percentPosition: !0,
            });
        });
        var $gal_container = $(".m-gallery");
        $gal_container.imagesLoaded(function () {
            $gal_container.isotope({
                itemSelector: ".col-lg-6",
                percentPosition: !0,
            });
        });
        $(".filter-links").on("click", "a", function () {
            var filterValue = $(this).attr("data-href");
            $container.isotope({ filter: filterValue });
            $(".filter-links a").removeClass("active");
            $(this).addClass("active");
            if (
                !$(filterValue)
                    .find(".scroll-animate")
                    .hasClass("animate__active")
            ) {
                $(filterValue)
                    .find(".scroll-animate")
                    .addClass("animate__active");
            }
            return !1;
        });
        $(".has-popup-video").magnificPopup({
            disableOn: 700,
            type: "iframe",
            iframe: {
                patterns: {
                    youtube_short: {
                        index: "youtu.be/",
                        id: "youtu.be/",
                        src: "https://www.youtube.com/embed/%id%?autoplay=1",
                    },
                },
            },
            removalDelay: 160,
            preloader: !1,
            fixedContentPos: !1,
            mainClass: "mfp-fade",
            callbacks: {
                markupParse: function (template, values, item) {
                    template.find("iframe").attr("allow", "autoplay");
                },
            },
        });
        $(".has-popup-audio").magnificPopup({
            disableOn: 700,
            type: "iframe",
            removalDelay: 160,
            preloader: !1,
            fixedContentPos: !1,
            mainClass: "mfp-fade",
        });
        $(".tab-menu").on("click", ".tab-btn", function () {
            var tab_bl = $(this).attr("href");
            $(this).closest(".tab-menu").find("li").removeClass("active");
            $(this).closest("li").addClass("active");
            $(this).closest(".tabs").find("> .tab-item").hide();
            $(tab_bl).fadeIn();
            return !1;
        });
        $(".lui-collapse-item").on("click", ".lui-collapse-btn", function () {
            if ($(this).closest(".lui-collapse-item").hasClass("opened")) {
                $(this).closest(".lui-collapse-item").removeClass("opened");
                $(this).removeClass("active");
            } else {
                $(this).closest(".lui-collapse-item").addClass("opened");
                $(this).addClass("active");
            }
        });
        $(".m-video-large .video").on("click", ".play, .img", function () {
            $(this).closest(".video").addClass("active");
            var iframe = $(this).closest(".video").find(".js-video-iframe");
            largeVideoPlay(iframe);
            return !1;
        });
        function largeVideoPlay(iframe) {
            var src = iframe.data("src");
            iframe.attr("src", src);
        }
        $(".header .cart-btn .cart-icon").on("click", function () {
            if ($(this).closest(".cart-btn").hasClass("opened")) {
                $(this).closest(".cart-btn").removeClass("opened");
                $(this).closest(".cart-btn").find(".cart-widget").hide();
            } else {
                $(this).closest(".cart-btn").addClass("opened");
                $(this).closest(".cart-btn").find(".cart-widget").fadeIn();
            }
            return !1;
        });
    });
    function initCursor() {
        var mouseX = window.innerWidth / 2,
            mouseY = window.innerHeight / 2;
        var cursor = {
            el: $(".cursor"),
            x: window.innerWidth / 2,
            y: window.innerHeight / 2,
            w: 30,
            h: 30,
            update: function () {
                var l = this.x - this.w / 2;
                var t = this.y - this.h / 2;
                this.el.css({
                    transform: "translate3d(" + l + "px," + t + "px, 0)",
                });
            },
        };
        $(window).mousemove(function (e) {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });
        $(
            "a, .swiper-pagination, .swiper-button-prev, .swiper-button-next, button, .button, .btn, .lnk"
        ).hover(
            function () {
                $(".cursor").addClass("cursor-zoom");
            },
            function () {
                $(".cursor").removeClass("cursor-zoom");
            }
        );
        setInterval(move, 60 / 60);
        function move() {
            cursor.x = lerp(cursor.x, mouseX, 0.1);
            cursor.y = lerp(cursor.y, mouseY, 0.1);
            cursor.update();
        }
        function lerp(start, end, amt) {
            return (1 - amt) * start + amt * end;
        }
    }
    function setHeightFullSection() {
        var width = $(window).width();
        var height = $(window).height();
        $(".error-page, .menu-full-overlay, .preloader .centrize").css({
            height: height,
        });
    }
})(jQuery);
