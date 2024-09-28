# import atexit
from turtle import right, width
from bottle import route, run, template, request, redirect
import os
import pandas as pd
import json
import feedparser
import requests
from bs4 import BeautifulSoup
# import webbrowser

def save_to_default_json(df):
    # Sort the DataFrame by 'label' and then by 'title'
    df_sorted = df.sort_values(by=['label', 'title'])
    # print(df)
    # print(df_sorted)
    df_sorted.to_json('default.json', orient='records')
    
# def open_browser():
#     global BROWSER_INSTANCE
#     BROWSER_INSTANCE = webbrowser.open('http://localhost:8080', new=2)

# # Function to close the browser
# def close_browser():
#     if BROWSER_INSTANCE:
#         if os.name == 'nt':  # Windows
#             os.system("taskkill /im chrome.exe /f")
#         else:  # macOS and Linux
#             os.system("pkill -f chrome")

# atexit.register(close_browser)
    
@route('/')
def home():
    filename = "default.json"
    if os.path.exists(filename):
        try:
            df = pd.read_json(filename)
            
            # Create HTML table with edit, delete, and view options
            table_rows = []
            for index, row in df.iterrows():
                table_rows.append(f'''
                    <tr>
                        <td>{row['label']}</td>
                        <td>{row['title']}</td>
                        <td>{row['URL']}</td>
                        <td>
                            <a href="/rss_single/{index}" class="button">View</a>
                            <a href="/edit_feed/{index}" class="button">Edit</a>
                            <a href="/delete_feed/{index}" class="button" onclick="return confirm('Are you sure you want to delete this feed?')">Delete</a>
                        </td>
                    </tr>
                ''')
            
            table_content = '\n'.join(table_rows)
            
            return f'''
            <html>
            <head>
                <title>CC RSS Reader</title>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 10px; background-color: #000; color: #fff; }}
                    h1 {{ color: #4CAF50; text-align: center; }}
                    .table {{ border-collapse: collapse; width: 100%; margin-top: 10px; }}
                    .table th, .table td {{ border: 1px solid #333; padding: 8px; }}
                    .table tr:nth-child(even) {{ background-color: #111; }}
                    .button {{ display: inline-block; padding: 4px 8px; background-color: #4CAF50; color: white; text-decoration: none; margin: 2px; }}
                    .action-buttons {{ text-align: center; margin-bottom: 8px; }}
                    .end-button {{ background-color: #f44336; }} /* Red color for end button */
                    a {{ color: #4CAF50; }}
                </style>
            </head>
            <body>
                <h1>RSS Feed Manager</h1>
                <div class="action-buttons">
                    <a href="/rss" class="button">All RSS</a>
                    <a href="/select_multiple_feeds" class="button">RSS by selection</a>
                    <a href="/select_labels" class="button">RSS by labels</a>
                    <a href="/find_feeds" class="button">Find RSS</a>
                    <a href="/add_feed" class="button">Add New RSS</a>
                    <a href="/end_program" class="button end-button">End Program</a>
                </div>
                <table class="table">
                    <tr>
                        <th>Label</th>
                        <th>Title</th>
                        <th>URL</th>
                        <th>Actions</th>
                    </tr>
                    {table_content}
                </table>
            </body>
            </html>
            '''
        except Exception as e:
            return f"Error processing data: {str(e)}"
    else:
        return '''
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; text-align: center; background-color: #000; color: #fff; }
                .message { font-size: 16px; margin-bottom: 10px; }
                .button { display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin: 10px; }
            </style>
        </head>
        <body>
            <div class="message">default.json does not exist. Would you like to add a new feed?</div>
            <a href="/add_feed" class="button">Add New Feed</a>
        </body>
        </html>
        '''
    # Open the browser when the program starts
# open_browser()

# Add this new route to handle ending the program
@route('/end_program')
def end_program():
    os._exit(0)  # This will immediately terminate the program

@route('/rss')
def rss():
    filename = "default.json"
    df = pd.read_json(filename)
    output = []
    
    for _, row in df.iterrows():
        url = row['URL']
        label = row['label']
        title = row['title']
        feed = feedparser.parse(url)
        
        output.append(f"<h2>{title}</h2>")
        output.append(f"<h3>{label}</h3>")
        output.append("<ul>")
        
        for entry in feed.entries[:5]:  # Limit to 5 entries per feed
            entry_output = []
            if 'title' in entry:
                entry_output.append(f"<strong>{entry.title}</strong>")
            if 'published' in entry:
                entry_output.append(f"<em>({entry.published})</em>")
            if 'link' in entry:
                entry_output.append(f'<a href="{entry.link}" target="_blank">Read more</a>')
            if 'summary' in entry:
                summary = entry.summary[:200] + '...' if len(entry.summary) > 200 else entry.summary
                entry_output.append(f"<p>{summary}</p>")
            
            output.append(f"<li>{'<br>'.join(entry_output)}</li>")
        
        output.append("</ul>")
    
    htmlstr = "\n".join(output)
    return f'''
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 10px; background-color: #000; color: #fff; }}
            h2 {{ color: #4CAF50; }}
            h3 {{ color: #999; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{ margin-bottom: 5px; border-bottom: 1px solid #333; padding-bottom: 10px; }}
            a {{ color: #4CAF50; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-bottom: 20px; }}
            img {{
                max-width: 300px;
                height: auto;
                object-fit: cover;
            }}
            .separator {{
                border-top: 1px solid #4CAF50;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <a href="/" class="button">Home</a>
        <div class="separator"></div>
        {htmlstr}
    </body>
    </html>
    '''

@route('/select_multiple_feeds')
def select_multiple_feeds():
    filename = "default.json"
    if os.path.exists(filename):
        try:
            df = pd.read_json(filename)
            
            # Create HTML table with checkboxes for multiple selection
            table_rows = []
            for index, row in df.iterrows():
                table_rows.append(f'''
                    <tr>
                        <td><input type="checkbox" name="selected_rows" value="{index}"></td>
                        <td>{row['label']}</td>
                        <td>{row['title']}</td>
                        <td>{row['URL']}</td>
                    </tr>
                ''')
            
            table_content = '\n'.join(table_rows)
            
            html_template = '''
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 10px; background-color: #000; color: #fff; }}
                    h1 {{ color: #4CAF50; text-align: center; }}
                    .table {{ border-collapse: collapse; width: 100%; }}
                    .table th, .table td {{ border: 1px solid #333; padding: 8px; }}
                    .table tr:nth-child(even) {{ background-color: #111; }}
                    .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-top: 20px; }}
                    input[type="checkbox"] {{ margin-right: 10px; }}
                    input[type="submit"] {{ background-color: #4CAF50; color: white; border: none; padding: 10px 20px; cursor: pointer; }}
                </style>
            </head>
            <body>
                <h1>Select Multiple RSS Feeds</h1>
                <form action="/view_multiple_feeds" method="post">
                    <table class="table">
                        <tr>
                            <th>Select</th>
                            <th>Label</th>
                            <th>Title</th>
                            <th>URL</th>
                        </tr>
                        {table}
                    </table>
                    <input type="submit" value="View Selected Feeds" class="button">
                </form>
                <a href="/" class="button">Home</a>
            </body>
            </html>
            '''
            return html_template.format(table=table_content)
        except Exception as e:
            return f"Error processing data: {str(e)}"
    else:
        return 'default.json does not exist'

@route('/select_labels')
def select_labels():
    filename = "default.json"
    if os.path.exists(filename):
        try:
            df = pd.read_json(filename)
            
            # Get unique labels
            labels = df['label'].unique()
            
            # Create HTML table with checkboxes for label selection
            table_rows = []
            for label in labels:
                table_rows.append(f'''
                    <tr>
                        <td><input type="checkbox" name="selected_labels" value="{label}"></td>
                        <td>{label}</td>
                    </tr>
                ''')
            
            table_content = '\n'.join(table_rows)
            
            html_template = '''
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 10px; background-color: #000; color: #fff; }}
                    h1 {{ color: #4CAF50; text-align: center; }}
                    .table {{ border-collapse: collapse; width: 100%; }}
                    .table th, .table td {{ border: 1px solid #333; padding: 8px; }}
                    .table tr:nth-child(even) {{ background-color: #111; }}
                    .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-top: 20px; }}
                    input[type="checkbox"] {{ margin-right: 10px; }}
                    input[type="submit"] {{ background-color: #4CAF50; color: white; border: none; padding: 10px 20px; cursor: pointer; }}
                </style>
            </head>
            <body>
                <h1>Select Labels</h1>
                <form action="/view_feeds_by_labels" method="post">
                    <table class="table">
                        <tr>
                            <th>Select</th>
                            <th>Label</th>
                        </tr>
                        {table}
                    </table>
                    <input type="submit" value="View Feeds" class="button">
                </form>
                <a href="/" class="button">Home</a>
            </body>
            </html>
            '''
            return html_template.format(table=table_content)
        except Exception as e:
            return f"Error processing data: {str(e)}"
    else:
        return 'default.json does not exist'

@route('/view_multiple_feeds', method='POST')
def view_multiple_feeds():
    selected_rows = request.forms.getall('selected_rows')
    if selected_rows:
        filename = "default.json"
        if os.path.exists(filename):
            try:
                df = pd.read_json(filename)
                output = []
                
                for row_index in selected_rows:
                    row = df.iloc[int(row_index)]
                    url = row['URL']
                    label = row['label']
                    title = row['title']
                    feed = feedparser.parse(url)
                    
                    output.append(f"<h2>{title}</h2>")
                    output.append(f"<h3>{label}</h3>")
                    output.append("<ul>")
                    
                    for entry in feed.entries[:5]:  # Limit to 5 entries per feed
                        entry_output = []
                        if 'title' in entry:
                            entry_output.append(f"<strong>{entry.title}</strong>")
                        if 'published' in entry:
                            entry_output.append(f"<em>({entry.published})</em>")
                        if 'link' in entry:
                            entry_output.append(f'<a href="{entry.link}" target="_blank">Read more</a>')
                        if 'summary' in entry:
                            summary = entry.summary[:200] + '...' if len(entry.summary) > 200 else entry.summary
                            entry_output.append(f"<p>{summary}</p>")
                        
                        output.append(f"<li>{'<br>'.join(entry_output)}</li>")
                    
                    output.append("</ul>")
                    output.append("<hr>")  # Add a horizontal line between feeds
                
                htmlstr = "\n".join(output)
                return f'''
                <html>
                <head>
                    <style>
                        body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 10px; background-color: #000; color: #fff; }}
                        h2 {{ color: #4CAF50; }}
                        h3 {{ color: #999; }}
                        ul {{ list-style-type: none; padding: 0; }}
                        li {{ margin-bottom: 5px; border-bottom: 1px solid #333; padding-bottom: 10px; }}
                        a {{ color: #4CAF50; text-decoration: none; }}
                        a:hover {{ text-decoration: underline; }}
                        .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-bottom: 20px; }}
                        img {{
                            max-width: 300px;
                            height: auto;
                            object-fit: cover;
                        }}
                        .separator {{
                            border-top: 1px solid #4CAF50;
                            margin: 20px 0;
                        }}
                    </style>
                </head>
                <body>
                    <a href="/" class="button">Home</a>
                    <a href="/select_multiple_feeds" class="button">Back to Selection</a>
                    <div class="separator"></div>
                    {htmlstr}
                </body>
                </html>
                '''
            except Exception as e:
                return f"Error processing data: {str(e)}"
        else:
            return 'default.json does not exist'
    else:
        return "No feeds selected. Please go back and select at least one feed."

@route('/add_feed')
def add_feed():
    return '''
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; background-color: #000; color: #fff; }
            h1 { color: #4CAF50; text-align: center; }
            form { margin: 0 auto; width: 300px; }
            label { display: block; margin-bottom: 5px; }
            input[type="text"] { width: 100%; padding: 8px; margin-bottom: 10px; }
            input[type="submit"] { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; }
            .button { display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Add New Feed</h1>
        <form action="/save_feed" method="post">
            <label for="label">Label:</label>
            <input type="text" id="label" name="label" required>
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" required>
            <label for="url">URL:</label>
            <input type="text" id="url" name="url" required>
            <input type="submit" value="Save Feed">
        </form>
        <a href="/" class="button">Home</a>
    </body>
    </html>
    '''

@route('/save_feed', method='POST')
def save_feed():
    label = request.forms.getunicode('label')
    title = request.forms.getunicode('title')
    url = request.forms.getunicode('url')
    
    filename = "default.json"
    if os.path.exists(filename):
        df = pd.read_json(filename)
    else:
        df = pd.DataFrame(columns=['label', 'title', 'URL'])
    
    new_row = pd.DataFrame({'label': [label], 'title': [title], 'URL': [url]})
    df = pd.concat([df, new_row], ignore_index=True)
    ## save json
    # df.to_json(filename, orient='records')
    save_to_default_json(df)
    
    return redirect('/')

@route('/find_feeds')
def find_feeds():
    return '''
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; background-color: #000; color: #fff; }
            h1 { color: #4CAF50; text-align: center; }
            form { margin: 0 auto; width: 300px; }
            label { display: block; margin-bottom: 5px; }
            input[type="text"] { width: 100%; padding: 8px; margin-bottom: 10px; }
            input[type="submit"] { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; }
            .button { display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Find RSS Feeds</h1>
        <form action="/list_feeds" method="post">
            <label for="site_url">Site URL:</label>
            <input type="text" id="site_url" name="site_url" required>
            <input type="submit" value="Find Feeds">
        </form>
        <a href="/" class="button">Home</a>
        {htmlstr}
    </body>
    </html>
    '''

@route('/list_feeds', method='POST')
def list_feeds():
    site_url = request.forms.get('site_url')
    resp = requests.get(site_url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    # Find all RSS or XML links
    feeds = []
    for link in soup.find_all('link', type='application/rss+xml'):
        feeds.append({'title': link.get('title', 'No title'), 'url': link.get('href')})
    for link in soup.find_all('link', type='application/atom+xml'):
        feeds.append({'title': link.get('title', 'No title'), 'url': link.get('href')})
    
    # Create HTML to list the feeds with text input fields and "Add" buttons
    feed_options = ''.join([f'''
        <tr>
            <td>{feed['title']}</td>
            <td>{feed['url']}</td>
            <td>
                <form action="/add_feed_from_list" method="post" style="display:inline;">
                    <input type="hidden" name="feed_url" value="{feed['url']}">
                    <input type="text" name="label" placeholder="Enter label" required>
                    <input type="submit" value="Add">
                </form>
            </td>
        </tr>
    ''' for feed in feeds])
    
    return f'''
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; background-color: #000; color: #fff; }}
            h1 {{ color: #4CAF50; text-align: center; }}
            form {{ margin: 0 auto; width: 600px; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ border: 1px solid #333; padding: 8px; text-align: left; }}
            th {{ background-color: #111; }}
            input[type="submit"] {{ background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; }}
            .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <h1>Select RSS Feeds</h1>
        <table>
            <tr>
                <th>Title</th>
                <th>URL</th>
                <th>Action</th>
            </tr>
            {feed_options}
        </table>
        <a href="/" class="button">Home</a>
    </body>
    </html>
    '''

@route('/add_feed_from_list', method='POST')
def add_feed_from_list():
    selected_feeds = request.forms.getall('feed_url')
    
    # Assuming you have a function to add a feed to the DataFrame
    filename = "default.json"
    if os.path.exists(filename):
        df = pd.read_json(filename)
    else:
        df = pd.DataFrame(columns=['label', 'title', 'URL'])
    
    for feed_url in selected_feeds:
        label = "New Feed"  # You can modify this to get a label from the user if needed
        title = "New Feed Title"  # You can modify this to get a title from the user if needed
        new_row = pd.DataFrame({'label': [label], 'title': [title], 'URL': [feed_url]})
        df = pd.concat([df, new_row], ignore_index=True)
    
    save_to_default_json(df)
    
    return redirect('/')

@route('/rss_single/<row_index:int>')
def rss_single(row_index):
    filename = "default.json"
    if os.path.exists(filename):
        try:
            df = pd.read_json(filename)
            if row_index < 0 or row_index >= len(df):
                return f"Invalid row index. Please provide a number between 0 and {len(df) - 1}."
            
            row = df.iloc[row_index]
            url = row['URL']
            label = row['label']
            title = row['title']
            feed = feedparser.parse(url)
            
            output = [f"<h2>{title}</h2>", f"<h3>{label}</h3>", "<ul>"]
            
            for entry in feed.entries[:10]:  # Limit to 10 entries
                entry_output = []
                if 'title' in entry:
                    entry_output.append(f"<strong>{entry.title}</strong>")
                if 'link' in entry:
                    entry_output.append(f'<span style="float: right;"><a href="{entry.link}" target="_blank">Read more</a></span>')
                if 'published' in entry:  # Corrected typo from 'publi8shed' to 'published'
                    entry_output.append(f"<em>({entry.published})</em>")
                if 'summary' in entry:
                    summary = entry.summary[:200] + '...' if len(entry.summary) > 200 else entry.summary
                    entry_output.append(f"<p>{summary}</p>")
                
                output.append(f"<li>{'<br>'.join(entry_output)}</li>")
            
            output.append("</ul>")
            
            htmlstr = "\n".join(output)
            return f'''
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 10px; background-color: #000; color: #fff; }}
                    h2 {{ color: #4CAF50; }}
                    h3 {{ color: #999; }}
                    ul {{ list-style-type: none; padding: 0; }}
                    li {{ margin-bottom: 5px; border-bottom: 1px solid #333; padding-bottom: 10px; }}
                    a {{ color: #4CAF50; text-decoration: none; }}
                    a:hover {{ text-decoration: underline; }}
                    .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-bottom: 20px; }}
                    img {{
                        max-width: 300px;
                        height: auto;
                        object-fit: cover;
                    }}
                    .separator {{
                        border-top: 1px solid #4CAF50;
                        margin: 20px 0;
                    }}
                </style>
            </head>
            <body>
                <a href="/" class="button">Home</a>
                <div class="separator"></div>
                {htmlstr}
            </body>
            </html>
            '''
        except Exception as e:
            return f"Error processing data: {str(e)}"
    else:
        return 'default.json does not exist'

@route('/view_selected_feed', method='POST')
def view_selected_feed():
    selected_row = request.forms.get('selected_row')
    if selected_row is not None:
        return redirect(f'/rss_single/{selected_row}')
    else:
        return "No feed selected. Please go back and select a feed."

@route('/manage_feeds')
def manage_feeds():
    filename = "default.json"
    if os.path.exists(filename):
        try:
            df = pd.read_json(filename)
            
            # Create HTML table with edit and delete options
            table_rows = []
            for index, row in df.iterrows():
                table_rows.append(f'''
                    <tr>
                        <td>{row['label']}</td>
                        <td>{row['title']}</td>
                        <td>{row['URL']}</td>
                        <td>
                            <a href="/edit_feed/{index}">Edit</a> |
                            <a href="/delete_feed/{index}">Delete</a>
                        </td>
                    </tr>
                ''')
            
            table_content = '\n'.join(table_rows)
            
            html_template = '''
            <html>
            <head>
                <style>
                    .table {{ border-collapse: collapse; width: 100%; }}
                    .table th, .table td {{ border: 1px solid #ddd; padding: 8px; }}
                    .table tr:nth-child(even) {{ background-color: #f2f2f2; }}
                    .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-bottom: 20px; }}
                </style>
            </head>
            <body>
                <a href="/" class="button">Home</a>
                <br>
                <table class="table">
                    <tr>
                        <th>Label</th>
                        <th>Title</th>
                        <th>URL</th>
                        <th>Action</th>
                    </tr>
                    {table}
                </table>
            </body>
            </html>
            '''
            return html_template.format(table=table_content)
        except Exception as e:
            return f"Error processing data: {str(e)}"
    else:
        return 'default.json does not exist'

@route('/edit_feed/<row_index:int>')
def edit_feed(row_index):
    filename = "default.json"
    if os.path.exists(filename):
        try:
            df = pd.read_json(filename)
            if row_index < 0 or row_index >= len(df):
                return f"Invalid row index. Please provide a number between 0 and {len(df) - 1}."
            
            row = df.iloc[row_index]
            label = row['label']
            title = row['title']
            url = row['URL']
            
            html_template = f'''
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 10px; text-align: center; }}
                    form {{ max-width: 500px; margin: 0 auto; }}
                    label {{ display: block; margin-top: 10px; }}
                    input[type="text"] {{ width: 100%; padding: 5px; margin-top: 5px; }}
                    input[type="submit"] {{ display: block; width: 100%; padding: 10px; background-color: #4CAF50; color: white; border: none; cursor: pointer; margin-top: 20px; }}
                    .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-top: 20px; }}
                </style>
            </head>
            <body>
                <h1>Edit RSS Feed</h1>
                <form action="/update_feed/{row_index}" method="post">
                    <label for="label">Label:</label>
                    <input type="text" id="label" name="label" value="{label}" required>
                    
                    <label for="title">Title:</label>
                    <input type="text" id="title" name="title" value="{title}" required>
                    
                    <label for="url">URL:</label>
                    <input type="text" id="url" name="url" value="{url}" required>
                    
                    <input type="submit" value="Update Feed">
                </form>
                <a href="/" class="button">Home</a>
            </body>
            </html>
            '''
            return html_template
        except Exception as e:
            return f"Error processing data: {str(e)}"
    else:
        return 'default.json does not exist'

@route('/update_feed/<row_index:int>', method='POST')
def update_feed(row_index):
    filename = "default.json"
    if os.path.exists(filename):
        try:
            df = pd.read_json(filename)
            if row_index < 0 or row_index >= len(df):
                return f"Invalid row index. Please provide a number between 0 and {len(df) - 1}."
            
            label = request.forms.getunicode('label')
            title = request.forms.getunicode('title')
            url = request.forms.getunicode('url')
            
            df.at[row_index, 'label'] = label
            df.at[row_index, 'title'] = title
            df.at[row_index, 'URL'] = url
            
            # df.to_json(filename, orient='records')
            save_to_default_json(df)
            
            return '''
            <html>
            <head>
                <style>
                    body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; text-align: center; }
                    .message { font-size: 18px; margin-bottom: 20px; }
                    .button { display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin: 10px; }
                </style>
            </head>
            <body>
                <div class="message">Feed updated successfully!</div>
                <a href="/" class="button">Home</a>
            </body>
            </html>
            '''
        except Exception as e:
            return f"Error processing data: {str(e)}"
    else:
        return 'default.json does not exist'

@route('/delete_feed/<row_index:int>')
def delete_feed(row_index):
    filename = "default.json"
    if os.path.exists(filename):
        try:
            df = pd.read_json(filename)
            if row_index < 0 or row_index >= len(df):
                return f"Invalid row index. Please provide a number between 0 and {len(df) - 1}."
            
            df = df.drop(df.index[row_index])
            # df.to_json(filename, orient='records')
            save_to_default_json(df)
            
            return '''
            <html>
            <head>
                <style>
                    body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; text-align: center; }
                    .message { font-size: 18px; margin-bottom: 20px; }
                    .button { display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin: 10px; }
                </style>
            </head>
            <body>
                <div class="message">Feed deleted successfully!</div>
                <a href="/" class="button">Home</a>
            </body>
            </html>
            '''
        except Exception as e:
            return f"Error processing data: {str(e)}"
    else:
        return 'default.json does not exist'

@route('/select_labels')
def select_labels():
    filename = "default.json"
    if os.path.exists(filename):
        try:
            df = pd.read_json(filename)
            
            # Get unique labels
            labels = df['label'].unique()
            
            # Create HTML table with checkboxes for label selection
            table_rows = []
            for label in labels:
                table_rows.append(f'''
                    <tr>
                        <td><input type="checkbox" name="selected_labels" value="{label}"></td>
                        <td>{label}</td>
                    </tr>
                ''')
            
            table_content = '\n'.join(table_rows)
            
            html_template = '''
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 10px; background-color: #000; color: #fff; }}
                    h1 {{ color: #4CAF50; text-align: center; }}
                    .table {{ border-collapse: collapse; width: 100%; }}
                    .table th, .table td {{ border: 1px solid #333; padding: 8px; }}
                    .table tr:nth-child(even) {{ background-color: #111; }}
                    .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-top: 20px; }}
                    input[type="checkbox"] {{ margin-right: 10px; }}
                    input[type="submit"] {{ background-color: #4CAF50; color: white; border: none; padding: 10px 20px; cursor: pointer; }}
                </style>
            </head>
            <body>
                <h1>Select Labels</h1>
                <form action="/view_feeds_by_labels" method="post">
                    <table class="table">
                        <tr>
                            <th>Select</th>
                            <th>Label</th>
                        </tr>
                        {table}
                    </table>
                    <input type="submit" value="View Feeds" class="button">
                </form>
                <a href="/" class="button">Home</a>
            </body>
            </html>
            '''
            return html_template.format(table=table_content)
        except Exception as e:
            return f"Error processing data: {str(e)}"
    else:
        return 'default.json does not exist'

@route('/view_feeds_by_labels', method='POST')
def view_feeds_by_labels():
    selected_labels = request.forms.getall('selected_labels')
    if selected_labels:
        filename = "default.json"
        if os.path.exists(filename):
            try:
                df = pd.read_json(filename)
                output = []
                
                for label in selected_labels:
                    label_df = df[df['label'] == label]
                    
                    # Extract the title for the current label
                    title = label_df['title'].values[0] if not label_df.empty else 'No title found'
                    
                    output.append(f"<h2>{label}</h2>")
                    output.append(f"<h3>{title}</h3>")
                    output.append("<ul>")
                    
                    for _, row in label_df.iterrows():
                        url = row['URL']
                        title = row['title']
                        output.append(f"<h4>{title}</h4>")
                        feed = feedparser.parse(url)
                        
                        for entry in feed.entries[:5]:  # Limit to 5 entries per feed
                            entry_output = []
                            if 'title' in entry:
                                entry_output.append(f"<strong>{entry.title}</strong>")
                            if 'published' in entry:
                                entry_output.append(f"<em>({entry.published})</em>")
                            if 'link' in entry:
                                entry_output.append(f'<a href="{entry.link}" target="_blank">Read more</a>')
                            if 'summary' in entry:
                                summary = entry.summary[:200] + '...' if len(entry.summary) > 200 else entry.summary
                                entry_output.append(f"<p>{summary}</p>")
                            
                            output.append(f"<li>{'<br>'.join(entry_output)}</li>")
                    
                    output.append("</ul>")
                    output.append("<hr>")  # Add a horizontal line between feeds
                
                htmlstr = "\n".join(output)
                return f'''
                <html>
                    <head>
                        <style>
                            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 10px; background-color: #000; color: #fff; }}
                            h2 {{ color: #4CAF50; }}
                            h3, h4 {{ color: #8BC34A; }}
                            ul {{ list-style-type: none; padding: 0; }}
                            li {{ margin-bottom: 5px; border-bottom: 1px solid #333; padding-bottom: 10px; }}
                            a {{ color: #4CAF50; text-decoration: none; }}
                            a:hover {{ text-decoration: underline; }}
                            .button {{ display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; margin-bottom: 20px; }}
                            img {{
                                max-width: 300px;
                                height: auto;
                                object-fit: cover;
                            }}
                            .separator {{
                                border-top: 1px solid #4CAF50;
                                margin: 20px 0;
                            }}
                            hr {{
                                border: 0;
                                border-top: 1px solid #333;
                                margin: 20px 0;
                            }}
                        </style>
                    </head>
                    <body>
                        <a href="/" class="button">Home</a>
                        <a href="/select_labels" class="button">Back to Labels</a>
                        <div class="separator"></div>
                        {htmlstr}
                    </body>
                </html>
                '''
            except Exception as e:
                return f"Error processing data: {str(e)}"
        else:
            return 'default.json does not exist'
    else:
        return "No labels selected. Please go back and select at least one label."


if __name__ == '__main__':
    
    run(host='localhost', port=8080, debug=True)