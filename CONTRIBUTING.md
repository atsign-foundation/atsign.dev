<img width=250px src="https://atsign.dev/assets/img/atPlatform_logo_gray.svg?sanitize=true">

# Contributing guidelines

We :heart: [Pull Requests](https://help.github.com/articles/about-pull-requests/)
for fixing issues or adding features. Thanks for your contribution!

Please read our [code of conduct](code_of_conduct.md), which is based on
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct.md)

For small changes, especially documentation, you can simply use the "Edit" button
to update the Markdown file, and start the
[pull request](https://help.github.com/articles/about-pull-requests/) process.
Use the preview tab in GitHub to make sure that it is properly
formatted before committing.
A pull request will cause integration tests to run automatically, so please review
the results of the pipeline and correct any mistakes that are reported.

If you plan to contribute often or have a larger change to make, it is best to
setup an environment for contribution, which is what the rest of these guidelines
describe.

## Development Environment Setup

### 1. Local Hugo Installation

*Install Hugo Extended directly onto your local machine*

Take a look at the [Working With Hugo](./content/en/docs/guides/getting-started-with-hugo.md)
guide for some background on the Hugo static site generator used to build this
site.

### 2. Local devcontainer

*Easy installation of a docker container with the environment preconfigured*

In Visual Studio Code, install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension offered by Microsoft, and install Docker using [their guides](https://docs.docker.com/get-docker/)

To open your development environment:

1. Start Docker if it isn't already started
1. Click on the "Open a Remote Window" in the bottom left corner of Visual Studio Code
   1. If you already have the project folder open, select "Reopen in Container"
   1. Otherwise, select "Open Folder in Container..." and choose the project folder
1. Visual Studio Code will setup the environment in a docker container and spin up a hugo server for you
1. Open http://localhost:1313 in the browser, and begin coding!

If you are on Windows and using the WSL2 Engine for Docker, you will have to clone the project to you WSL filesystem to take advantage of Hugo's live reloading features.

### 3. Github Codespaces

*Setup a devcontainer in the cloud with github codespaces*

Take a look at the [Creating a codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace) and [Developing in a codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/developing-in-a-codespace) guides on GitHub.

### GitHub Repository Clone

To prepare your dedicated GitHub repository:

1. Fork in GitHub https://github.com/atsign-foundation/atsign.dev
2. Clone *your forked repository* (e.g., `git clone --recursive git@github.com:yourname/atsign.dev`).
NB the `--recursive` flag is used to ensure that the theme submodules are also downloaded.
If you've already made a clone without that flag then run `git submodule update --init --recursive`
to achieve the same outcome.
3. Set your remotes as follows:

   ```sh
   cd atsign.dev
   git remote add upstream git@github.com:atsign-foundation/atsign.dev.git
   git remote set-url upstream --push DISABLED
   ```

   Running `git remote -v` should give something similar to:

   ```text
   origin  git@github.com:yourname/atsign.dev.git (fetch)
   origin  git@github.com:yourname/atsign.dev.git (push)
   upstream        git@github.com:atsign-foundation/atsign.dev.git (fetch)
   upstream        DISABLED (push)
   ```

   The use of `upstream --push DISABLED` is to prevent those
   with `write` access to the main repository from accidentally pushing changes
   directly.

### Development Process

1. Fetch latest changes from main repository:

   ```sh
   git fetch upstream
   ```

1. Check that submodules are up to date:

   ```sh
   git submodule update --remote --merge
   ```

1. Reset your fork's `trunk` branch to exactly match upstream `trunk`:

   ```sh
   git checkout trunk
   git reset --hard upstream/trunk
   git push --force
   ```

   **IMPORTANT**: Do this only once, when you start working on new feature as
   the commands above will completely overwrite any local changes in `trunk` content.
   
1. Edit, edit, edit, and commit your changes to Git:

   ```sh
   # edit, edit, edit
   git add *
   git commit -m 'A useful commit message'
   git push
   ```

1. Open a new Pull Request to the main repository using your `trunk` branch
