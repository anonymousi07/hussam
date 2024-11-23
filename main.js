var typed = new Typed(".text", {
    strings: ["Front-End Developer", "Engineer", "Web Developer"],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});



    window.addEventListener('load', function() {
        const bars = document.querySelectorAll('.progress-line span');
        bars.forEach(bar => {
            const finalWidth = bar.dataset.percentage;

            // Reset the width to 0 to trigger the animation
            bar.style.width = '0';

            // Set the CSS variable for the final width
            bar.style.setProperty('--final-width', finalWidth);

            // Display the percentage on the bar
            bar.setAttribute('data-percentage', finalWidth);

            // Use setTimeout to apply the final width and trigger animation
            setTimeout(() => {
                bar.style.width = finalWidth;

                // After the animation duration, make the percentage visible
                setTimeout(() => {
                    bar.classList.add('filled');
                }, 2000); // Adjust timing to match your animation duration
            }, 100); // Delay to ensure reset width applies before animation
        });
    });



