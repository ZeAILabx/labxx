import React, { useEffect, useRef } from 'react';
import { useLocation } from 'react-router-dom';
import './CipherScreen.css';

const visited = new Set();
const symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#%';

export const CipherScreen = ({ children }) => {
  const root = useRef(null);
  const { pathname } = useLocation();

  useEffect(() => {
    const key = `labx:screen-reveal:${pathname}`;
    let seen = visited.has(key);
    try { seen ||= sessionStorage.getItem(key) === '1'; } catch { /* Storage may be unavailable. */ }
    if (seen || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    let interval;
    let finished;
    let started = false;
    const targets = [];
    const restore = () => targets.forEach(element => {
      element.classList.remove('screen-decoding');
      element.removeAttribute('data-cipher');
    });
    const begin = () => {
      if (started || !root.current) return;
      const headings = root.current.querySelectorAll('h1, h2, h3');
      if (!headings.length) return; // Wait for lazy routes and their initial data.
      started = true;
      observer.disconnect();
      targets.push(...root.current.querySelectorAll('h1, h2, h3, label, button'));
      const entries = targets.filter(element => element.textContent.trim() && !element.closest('.floating-xp'))
        .map(element => [element, element.textContent.trim()]);
      const start = performance.now();
      const frame = () => {
        const progress = Math.min(1, (performance.now() - start) / 1200);
        entries.forEach(([element, text]) => {
          element.setAttribute('data-cipher', [...text].map((char, index) =>
            index < Math.floor(progress * text.length) || !/[a-z0-9]/i.test(char)
              ? char : symbols[Math.floor(Math.random() * symbols.length)]
          ).join(''));
          element.classList.add('screen-decoding');
        });
      };
      frame();
      interval = window.setInterval(frame, 55);
      finished = window.setTimeout(() => {
        window.clearInterval(interval);
        restore();
        visited.add(key);
        try { sessionStorage.setItem(key, '1'); } catch { /* Keep in-memory tracking. */ }
      }, 1250);
    };
    const observer = new MutationObserver(begin);
    observer.observe(root.current, { childList: true, subtree: true });
    begin();
    return () => {
      observer.disconnect();
      window.clearInterval(interval);
      window.clearTimeout(finished);
      restore();
    };
  }, [pathname]);

  return <div ref={root} className="cipher-screen">{children}</div>;
};
