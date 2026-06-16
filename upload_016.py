import json, mimetypes, os, re, subprocess, urllib.request, urllib.error

def main():
    url = subprocess.check_output(["git", "config", "remote.origin.url"]).decode().strip()
    match = re.search(r"https://[^:]+:([^@]+)@github\.com", url)
    if not match:
        raise Exception("Could not extract token from git remote URL: " + url)
    token = match.group(1)

    repo = 'nexusrouters/nexus-code'
    tag = 'v0.1.6'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    print("Checking if release exists...")
    try:
        req = urllib.request.Request(f'https://api.github.com/repos/{repo}/releases/tags/{tag}', headers=headers)
        rel = json.load(urllib.request.urlopen(req))
        print("Release exists.")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
        print("Creating release...")
        data = json.dumps({
            'tag_name': tag,
            'name': tag,
            'target_commitish': 'main',
            'draft': False,
            'prerelease': False
        }).encode()
        req = urllib.request.Request(
            f'https://api.github.com/repos/{repo}/releases',
            data=data,
            headers={**headers, 'Content-Type': 'application/json'},
            method='POST'
        )
        rel = json.load(urllib.request.urlopen(req))
        print("Release created.")

    upload_url = rel['upload_url'].split('{', 1)[0]

    for a in rel.get('assets', []):
        print(f"Deleting existing asset: {a['name']}")
        try:
            dreq = urllib.request.Request(
                f"https://api.github.com/repos/{repo}/releases/assets/{a['id']}",
                headers=headers,
                method='DELETE'
            )
            urllib.request.urlopen(dreq).read()
        except Exception as e:
            print("Failed to delete asset:", e)

    for asset in ['nexus-code-windows-x64.zip', 'nexus-code-linux-x64.tar.gz']:
        if not os.path.exists(asset):
            print(f"Skipping missing asset: {asset}")
            continue
        print(f"Uploading {asset}...")
        with open(asset, 'rb') as f:
            body = f.read()
        ctype = mimetypes.guess_type(asset)[0] or 'application/octet-stream'
        ureq = urllib.request.Request(
            f'{upload_url}?name={asset}',
            data=body,
            headers={
                **headers,
                'Content-Type': ctype,
                'Content-Length': str(len(body))
            },
            method='POST'
        )
        up = json.load(urllib.request.urlopen(ureq))
        print("Uploaded:", up['browser_download_url'])

if __name__ == '__main__':
    main()
