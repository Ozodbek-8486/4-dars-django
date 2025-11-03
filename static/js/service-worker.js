const CACHE_NAME = 'django-offline-cache';
const OFFLINE_URL = '/offline/';

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll([
            '/',
            OFFLINE_URL,
            '/static/css/style.css', // statik fayllar
            '/static/js/app.js',
        ]))
    );
    self.skipWaiting();
});

self.addEventListener('fetch', event => {
    event.respondWith(
        fetch(event.request).catch(() => caches.match(OFFLINE_URL))
    );
});
