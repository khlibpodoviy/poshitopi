import os
from datetime import datetime
import pytumblr # pip install pytumblr

# You'll need API keys from api.tumblr.com/console
client = pytumblr.TumblrRestClient(
    'YOUR_CONSUMER_KEY',
    'YOUR_CONSUMER_SECRET',
    'YOUR_OAUTH_TOKEN',
    'YOUR_OAUTH_SECRET'
)

def fetch_and_format_tumblr(post_url, category="art"):
    # Extract blog name and post ID from your pasted URL
    # (Simplified for example: assume we parsed it to blog_name and post_id)
    blog_name = "example-blog"
    post_id = "123456789"
    
    post_data = client.posts(blog_name, id=post_id)['posts'][0]
    
    title = post_data.get('summary', 'Untitled')
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename = f"{date_str}-{title.replace(' ', '-').lower()[:20]}.html"
    
    # Preserve the raw HTML formatting exactly as Tumblr outputs it
    raw_html_content = post_data.get('body', '')
    
    # Jekyll Front Matter (This categorizes it automatically)
    front_matter = f"""---
layout: default
title: "{title}"
date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
categories: {category}
---

<div class="tumblr-repost">
    {raw_html_content}
</div>
"""
    
    # Save directly to the _posts directory
    file_path = os.path.join('_posts', filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(front_matter)
        
    print(f"Successfully created {file_path}!")

# Example usage:
# fetch_and_format_tumblr("https://example.tumblr.com/post/12345", "art")
