document.getElementById('email-btn').addEventListener('click', () => {
    showForm('email');
});

document.getElementById('linkedin-btn').addEventListener('click', () => {
    showForm('linkedin');
});

function showForm(platform) {
    const formContainer = document.getElementById('form-container');
    const emailField = document.getElementById('email-field');
    const platformInput = document.getElementById('platform');

    // Show the form
    formContainer.style.display = 'block';

    // Set the platform value
    platformInput.value = platform;

    // Show email field only for email platform
    if (platform === 'email') {
        emailField.style.display = 'block';
    } else {
        emailField.style.display = 'none';
    }
}

document.getElementById('generator-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        user_full_name: document.getElementById('user_full_name').value,
        gender: document.getElementById('gender').value,
        profession: document.getElementById('profession').value,
        recruiter_full_name: document.getElementById('recruiter_full_name').value,
        company_name: document.getElementById('company_name').value,
        recruiter_email: document.getElementById('recruiter_email').value,
        platform: document.getElementById('platform').value,
        language: document.getElementById('language').value,  // Add language
    };

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();
        document.getElementById('result').innerText = result.content || result.message;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred. Please try again.';
    }
});
