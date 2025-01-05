document.getElementById('generator-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Collect form data
    const formData = {
        user_full_name: document.getElementById('user_full_name').value,
        gender: document.getElementById('gender').value,
        profession: document.getElementById('profession').value,
        recruiter_full_name: document.getElementById('recruiter_full_name').value,
        company_name: document.getElementById('company_name').value,
        recruiter_email: document.getElementById('recruiter_email').value,
        platform: document.getElementById('platform').value,
        language: document.getElementById('language').value,
    };

    // Validate required fields
    if (!formData.user_full_name || !formData.gender || !formData.profession) {
        alert('Please fill out all required fields.');
        return;
    }

    // Show loading indicator
    document.getElementById('result').innerText = 'Loading...';

    try {
        // Send POST request
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        // Log raw response for debugging
        const rawResponse = await response.text();
        console.log("Raw Response:", rawResponse);

        // Handle non-OK responses
        if (!response.ok) {
            const errorData = JSON.parse(rawResponse);
            throw new Error(errorData.message || `HTTP error! Status: ${response.status}`);
        }

        // Parse and display the result
        const result = JSON.parse(rawResponse);
        document.getElementById('result').innerText = result.content || result.message;

        // Clear form after successful submission
        document.getElementById('generator-form').reset();
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = `An error occurred: ${error.message}`;
    }
});