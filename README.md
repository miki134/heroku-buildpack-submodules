# heroku-buildpack-submodules

# Usage
## Prerequisites
Heroku CLI Installed: Ensure you have the Heroku CLI installed on your system.
Environment Variable for Authentication (if needed):
Set up the ```GITHUB_AUTH_KEY``` environment variable with your personal access token or SSH key.
Adding the Buildpack to Your App
Add this buildpack to your Heroku application:

``` 
heroku buildpacks:add https://github.com/your-repo heroku-buildpack-submodules.git
```

Push your code to Heroku:

```
git push heroku main
```
The buildpack will automatically initialize and clone the submodules during the build process.

## Environment Variable
```GITHUB_AUTH_KEY```: (Optional) Used for private submodules.
This key will be injected into submodule URLs during cloning.

Example: If a submodule URL is https://github.com/user/repo.git, and ```GITHUB_AUTH_KEY``` is your-token, the URL becomes:

```
https://GITHUB_AUTH_KEY@github.com/user/repo.git
```

Set the key with:

```
heroku config:set GITHUB_AUTH_KEY="<your-key>"
```

## Troubleshooting
Common Issues
### Missing .gitmodules:

- Ensure your repository includes a .gitmodules file that lists all submodules.

### Authentication Errors:

- Verify that the GITHUB_AUTH_KEY is set and has sufficient permissions to access private submodules.

### Git Not Found:
- Ensure Git is installed and accessible during the build process.
- Install Git with https://github.com/heroku/heroku-buildpack-apt.git