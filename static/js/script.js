        function setupDropdowns() {
            const dropdowns = [
                { toggle: 'homeToggle', menu: 'homeMenu' },
                { toggle: 'pagesToggle', menu: 'pagesMenu' }
            ];

            dropdowns.forEach(({ toggle, menu }) => {
                const toggleBtn = document.getElementById(toggle);
                const menuDiv = document.getElementById(menu);

                // Click to open/close dropdown
                toggleBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    const isActive = toggleBtn.classList.contains('active');

                    // Close all dropdowns
                    dropdowns.forEach(({ toggle: t, menu: m }) => {
                        document.getElementById(t).classList.remove('active');
                        document.getElementById(m).classList.remove('active');
                    });

                    // Toggle current dropdown
                    if (!isActive) {
                        toggleBtn.classList.add('active');
                        menuDiv.classList.add('active');
                    }
                });

                // Close dropdown when clicking menu item
                menuDiv.addEventListener('click', (e) => {
                    if (e.target.tagName === 'A') {
                        toggleBtn.classList.remove('active');
                        menuDiv.classList.remove('active');
                    }
                });
            });

            // Close all dropdowns when clicking outside
            document.addEventListener('click', (e) => {
                if (!e.target.closest('nav')) {
                    dropdowns.forEach(({ toggle, menu }) => {
                        document.getElementById(toggle).classList.remove('active');
                        document.getElementById(menu).classList.remove('active');
                    });
                }
            });
        }

        // Initialize dropdowns on page load
        setupDropdowns();

        // Contact button click handler
        document.querySelector('.contact-btn').addEventListener('click', () => {
            console.log('[v0] Contact Us button clicked');
        });