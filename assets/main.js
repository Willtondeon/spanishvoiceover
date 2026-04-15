// spanishvoiceover.net — Main JS

(function() {
  'use strict';

  // ── Mobile Navigation ──
  const toggle = document.querySelector('.mobile-toggle');
  const nav = document.querySelector('.main-nav');
  let overlay;

  if (toggle && nav) {
    // Create overlay
    overlay = document.createElement('div');
    overlay.className = 'mobile-overlay';
    document.body.appendChild(overlay);

    toggle.addEventListener('click', function() {
      const isOpen = nav.classList.contains('open');
      nav.classList.toggle('open');
      overlay.classList.toggle('open');
      toggle.setAttribute('aria-expanded', !isOpen);
      
      // Animate hamburger
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

  // ── Lazy load Vimeo iframes ──
  const vimeoFrames = document.querySelectorAll('.video-embed iframe');
  if ('IntersectionObserver' in window && vimeoFrames.length) {
    const observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          const iframe = entry.target;
          if (iframe.dataset.src) {
            iframe.src = iframe.dataset.src;
          }
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

  // ── Smooth scroll for anchor links ──
  document.querySelectorAll('a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // ── Subtle fade-in on scroll ──
  if ('IntersectionObserver' in window) {
    const fadeObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          fadeObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.service-card, .video-embed, .contact-item').forEach(function(el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(16px)';
      el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      fadeObserver.observe(el);
    });
  }
})();
