const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

global.requestAnimationFrame = (fn) => setTimeout(fn, 16);
global.cancelAnimationFrame = (id) => clearTimeout(id);

global.window = {
  addEventListener: () => {},
  innerWidth: 375,
  scrollY: 0,
};
global.document = {
  getElementById: (id) => {
    if (html.includes('id="' + id + '"') || html.includes("id='" + id + "'")) {
      return {
        addEventListener: (evt, fn) => { console.log('  -> attached', evt, 'to', id); },
        classList: {
          add: () => {},
          remove: () => {},
          contains: () => false,
          toggle: () => {},
        },
        setAttribute: () => {},
        getBoundingClientRect: () => ({ top: 100, bottom: 500, height: 400 }),
        offsetTop: 200,
        getContext: () => ({
          clearRect: () => {},
          save: () => {},
          restore: () => {},
          beginPath: () => {},
          moveTo: () => {},
          lineTo: () => {},
          stroke: () => {},
          fill: () => {},
          fillRect: () => {},
          arc: () => {},
          strokeRect: () => {},
          fillText: () => {},
          setLineDash: () => {},
          createLinearGradient: () => ({ addColorStop: () => {} }),
          createRadialGradient: () => ({ addColorStop: () => {} }),
        }),
        style: {},
        value: '',
      };
    }
    console.log('MISSING getElementById:', id);
    return null;
  },
  querySelectorAll: (sel) => {
    return [];
  },
  addEventListener: (evt, fn) => {
    if (evt === 'DOMContentLoaded') {
      fn();
    }
  },
  body: {
    classList: { add: () => {}, remove: () => {} }
  }
};

try {
  require('../js/app.js');
  console.log('SUCCESS: app.js loaded without throwing!');
} catch (e) {
  console.error('ERROR in app.js:', e);
}
