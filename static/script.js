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
        language: document.getElementById('language').value,
    };

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        // Log the raw response for debugging
        const rawResponse = await response.text();
        console.log("Raw Response:", rawResponse);

        if (!response.ok) {
            const errorData = JSON.parse(rawResponse);  // Parse the raw response
            throw new Error(errorData.message || `HTTP error! Status: ${response.status}`);
        }

        const result = JSON.parse(rawResponse);  // Parse the raw response
        document.getElementById('result').innerText = result.content || result.message;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = `An error occurred: ${error.message}`;
    }
});