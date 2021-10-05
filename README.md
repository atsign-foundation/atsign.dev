<img src="https://atsign.dev/assets/img/@dev.png?sanitize=true">

### Now for a little internet optimism

# atsign.dev

The atsign.dev repo is home to the code behind our developer site. As everything we have to offer is open-source, why not make our website open-source too, to prove that we aren't using cookies or anything that tracks your presence.  

## Why is there an atsign.dev?

We hope that this site has the A -> Z of everything you will need to develop with the @platform.

If you are a developer, this is your site -  come join us and help us improve the content and the experience. We are always learning from you.

## What can you find in atsign.dev?

If you are new to the @platform, learn about how the platform works and how this can make such a big difference for you by cutting down on time to develop and market applications.

The site gives you all the tools, samples, examples and documentation needed to get started on the @platform and SDK. The site also provides access to the various communities where you can collaborate and talk to other developers working on the platform.

##  Pages we recommend visiting:

If this is your first time here, we strongly recommend navigating through our ‘[getting started](https://atsign.dev/docs/get-started/)’ page. There, you will find all of the steps you will need to take in order to start developing your very own @platform application. 

If you’d like to see what an @platform application looks like, feel free to visit our ‘[sample apps](https://atsign.dev/docs/sample-apps/)’ page! Here, you will find a list of demonstrative applications showing off the many verbs/methods that exist on the @platform. The most basic of this list is ‘[at_hello_world](https://github.com/atsign-foundation/at_demos/tree/trunk/at_hello_world)’ and the most advanced are ‘[at_cookbook](https://github.com/atsign-foundation/at_demos/tree/trunk/at_cookbook)’ and ‘[@mosphere](https://github.com/atsign-foundation/atmosphere)’

## How can you contribute?

If you think there should be a change made, or think there could be anything
done better, feel free to raise a pull request to the trunk branch.

Take a look at [CONTRIBUTING.md](CONTRIBUTING.md) for further instructions.

## How does stuff get from here to the production site?

When changes are merged to trunk they get published to the staging site [devstaging.atsign.wtf](https://devstaging.atsign.wtf/) by running the [HugoBuild](https://github.com/atsign-foundation/atsign.dev/blob/trunk/.github/workflows/HugoBuild.yml) GitHub Action, which publishes to the gh-pages branch in this repo.

When a [release](https://github.com/atsign-foundation/atsign.dev/releases) is tagged with a semanic version number (e.g. 1.0.8) the [DeployProd](https://github.com/atsign-foundation/atsign.dev/blob/trunk/.github/workflows/DeployProd.yml) Action runs, which publishes to the gh-pages branch in the [atsign.dev-prod](https://github.com/atsign-foundation/atsign.dev-prod) repo.

### Automated scraping from pub.dev

Some of the content here is taken from [pub.dev](https://pub.dev/publishers/atsign.org/packages), which is the authorative source for API docs. The [UpdateLibraries](https://github.com/atsign-foundation/atsign.dev/blob/trunk/.github/workflows/UpdateLibraries.yml) Action is set to run at 1415 daily to check for any updates to API docs for our packages.