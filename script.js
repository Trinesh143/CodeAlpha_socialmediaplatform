const postForm = document.getElementById('post-form');
const postContent = document.getElementById('post-content');
const postList = document.getElementById('post-list');

// Fetch and display posts
async function fetchPosts() {
    const response = await fetch('http://127.0.0.1:5000/posts');
    const posts = await response.json();
    postList.innerHTML = '';
    posts.forEach(post => {
        const postDiv = document.createElement('div');
        postDiv.classList.add('post');
        postDiv.textContent = post.content;
        postList.appendChild(postDiv);
    });
}

// Handle form submission
postForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const content = postContent.value;

    if (content.trim() === '') return;

    await fetch('http://127.0.0.1:5000/posts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content }),
    });

    postContent.value = '';
    fetchPosts(); // Refresh posts
});

// Initial fetch
fetchPosts();
