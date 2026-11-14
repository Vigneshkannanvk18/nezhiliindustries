import subprocess

code = '''
const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Mock window, document
global.window = {
  addEventListener: () => {},
  innerWidth: 375,
  scrollY: 0,
};
global.document = {
  getElementById: (id) => {
    console.log('getElementById:', id);
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
        }),
        style: {},
        value: '',
      };
    }
    return null;
  },
  querySelectorAll: (sel) => {
    console.log('querySelectorAll:', sel);
    return [];
  },
  addEventListener: (evt, fn) => {
    console.log('document.addEventListener:', evt);
    if (evt === 'DOMContentLoaded') {
      fn();
    }
  },
  body: {
    classList: { add: () => {}, remove: () => {} }
  }
};

try {
  require('./js/app.js');
  console.log('SUCCESS: app.js loaded without throwing!');
} catch (e) {
  console.error('ERROR in app.js:', e);
}
'''

with open('scripts/test_app_js.js', 'w', encoding='utf-8') as f:
    f.write(code)

