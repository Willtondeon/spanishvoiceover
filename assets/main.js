// spanishvoiceover.net — Main JS

(function() {
  'use strict';

  // ── Page Loader ──
  var loader = document.getElementById('pageLoader');
  function dismissLoader() {
    if (loader) { setTimeout(function() { loader.classList.add('loaded'); }, 300); }
  }
  if (document.readyState === 'complete') { dismissLoader(); }
  else { window.addEventListener('load', dismissLoader); }

  // ── Lenis Smooth Scroll ──
  var lenis;
  if (typeof Lenis !== 'undefined') {
    lenis = new Lenis({
      duration: 1.2,
      easing: function(t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      touchMultiplier: 2,
      infinite: false
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
  }

  // ── Custom Cursor ──
  var cursor = document.getElementById('customCursor');
  if (cursor && window.matchMedia('(hover: hover)').matches) {
    var cx = -100, cy = -100;
    document.addEventListener('mousemove', function(e) {
      cx = e.clientX; cy = e.clientY;
      cursor.style.transform = 'translate(' + cx + 'px,' + cy + 'px)';
    });
    document.querySelectorAll('a, button, [role=button], .service-card, .faq-item summary').forEach(function(el) {
      el.addEventListener('mouseenter', function() { cursor.classList.add('cursor-hover'); });
      el.addEventListener('mouseleave', function() { cursor.classList.remove('cursor-hover'); });
    });
  }

  // ── Mobile Navigation ──
  var toggle = document.querySelector('.mobile-toggle');
  var nav = document.querySelector('.main-nav');
  var overlay;

  if (toggle && nav) {
    overlay = document.createElement('div');
    overlay.className = 'mobile-overlay';
    document.body.appendChild(overlay);

    toggle.addEventListener('click', function() {
      var isOpen = nav.classList.contains('open');
      nav.classList.toggle('open');
      overlay.classList.toggle('open');
      toggle.setAttribute('aria-expanded', !isOpen);
      if (!isOpen) {
        toggle.children[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        toggle.children[1].style.opacity = '0';
        toggle.children[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        toggle.children[0].style.transform = '';
        toggle.children[1].style.opacity = '';
        toggle.children[2].style.transform = '';
      }
    });

    overlay.addEventListener('click', function() {
      nav.classList.remove('open');
      overlay.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.children[0].style.transform = '';
      toggle.children[1].style.opacity = '';
      toggle.children[2].style.transform = '';
    });
  }

  // ── Mobile dropdown toggle ──
  var dropdownToggle = document.querySelector('.dropdown-toggle');
  if (dropdownToggle) {
    dropdownToggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      var dropdown = this.parentElement.querySelector('.dropdown');
      var isOpen = dropdown.classList.contains('mobile-open');
      dropdown.classList.toggle('mobile-open');
      this.classList.toggle('open');
      this.setAttribute('aria-expanded', !isOpen);
    });
  }

  // ── Lazy load Vimeo iframes ──
  var vimeoFrames = document.querySelectorAll('.video-embed iframe');
  if ('IntersectionObserver' in window && vimeoFrames.length) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var iframe = entry.target;
          if (iframe.dataset.src) { iframe.src = iframe.dataset.src; }
          observer.unobserve(iframe);
        }
      });
    }, { rootMargin: '200px' });

    vimeoFrames.forEach(function(iframe) {
      if (iframe.src && !iframe.dataset.src) {
        iframe.dataset.src = iframe.src;
        iframe.removeAttribute('src');
      }
      observer.observe(iframe);
    });
  }

  // ── Smooth scroll for anchor links (via Lenis) ──
  document.querySelectorAll('a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var href = this.getAttribute('href');
      var target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        if (lenis) { lenis.scrollTo(target); }
        else { target.scrollIntoView({ behavior: 'smooth' }); }
      }
    });
  });

  // ── GSAP ScrollTrigger ──
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    // Connect Lenis to ScrollTrigger
    if (lenis) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(function(time) { lenis.raf(time * 1000); });
      gsap.ticker.lagSmoothing(0);
    }

    // Reveal sections on scroll
    gsap.utils.toArray('.section').forEach(function(section) {
      gsap.from(section, {
        opacity: 0, y: 40,
        duration: 0.8, ease: 'power2.out',
        scrollTrigger: { trigger: section, start: 'top 85%', toggleActions: 'play none none none' }
      });
    });

    // Word-by-word animation
    document.querySelectorAll('.animate-words').forEach(function(el) {
      var text = el.textContent.trim();
      var words = text.split(/\s+/);
      el.innerHTML = words.map(function(w) { return '<span class="word">' + w + '</span>'; }).join(' ');
      gsap.from(el.querySelectorAll('.word'), {
        opacity: 0, y: 20, filter: 'blur(4px)',
        duration: 0.6, ease: 'power2.out',
        stagger: 0.08,
        scrollTrigger: { trigger: el, start: 'top 80%', toggleActions: 'play none none none' }
      });
    });

    // Parallax on images
    gsap.utils.toArray('.parallax-img').forEach(function(img) {
      gsap.fromTo(img,
        { y: -30 },
        { y: 30, ease: 'none',
          scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: true }
        }
      );
    });

    // Video embeds reveal
    gsap.utils.toArray('.video-embed').forEach(function(vid) {
      gsap.from(vid, {
        opacity: 0, scale: 0.95,
        duration: 0.6, ease: 'power2.out',
        scrollTrigger: { trigger: vid, start: 'top 85%', toggleActions: 'play none none none' }
      });
    });

    // CTA section entrance
    var ctaSection = document.querySelector('.cta-section');
    if (ctaSection) {
      gsap.from(ctaSection.querySelectorAll('h2, p, .btn'), {
        opacity: 0, y: 30,
        duration: 0.7, ease: 'power2.out',
        stagger: 0.15,
        scrollTrigger: { trigger: ctaSection, start: 'top 80%', toggleActions: 'play none none none' }
      });
    }

    // FAQ cascade reveal
    gsap.utils.toArray('.faq-item').forEach(function(item, i) {
      gsap.from(item, {
        opacity: 0, x: -20,
        duration: 0.5, ease: 'power2.out',
        delay: i * 0.05,
        scrollTrigger: { trigger: item, start: 'top 90%', toggleActions: 'play none none none' }
      });
    });

    // Service cards stagger
    gsap.utils.toArray('.service-card').forEach(function(card, i) {
      gsap.from(card, {
        opacity: 0, y: 30,
        duration: 0.6, ease: 'power2.out',
        delay: i * 0.08,
        scrollTrigger: { trigger: card, start: 'top 88%', toggleActions: 'play none none none' }
      });
    });

    // Studio gallery items
    gsap.utils.toArray('.studio-gallery-item').forEach(function(item, i) {
      gsap.from(item, {
        opacity: 0, scale: 0.9,
        duration: 0.8, ease: 'power2.out',
        delay: i * 0.15,
        scrollTrigger: { trigger: item, start: 'top 85%', toggleActions: 'play none none none' }
      });
    });
  }

  // ── Header hide/show on scroll ──
  var header = document.querySelector('.site-header');
  if (header && lenis) {
    var lastScroll = 0;
    lenis.on('scroll', function(e) {
      var currentScroll = e.animatedScroll;
      if (currentScroll > 100) {
        if (currentScroll > lastScroll) {
          header.classList.add('header-hidden');
        } else {
          header.classList.remove('header-hidden');
        }
      } else {
        header.classList.remove('header-hidden');
      }
      lastScroll = currentScroll;
    });
  }

})();
