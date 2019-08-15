





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-wOA18h3okAQWgNcdM+ifzeK5+sEAYkPVcS3CPFIdC9vvD4RGqtHlYG/K6x2baoGTWcyAj3WeE3ok4MpZk3Mtiw==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-edbb2ca6a8a45d0c4f75a2f2e78a2d86.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-vozupRTrzo7k2NwiAgC37o0fUpxqBtSeDrVyaxH6I+ed18h/6awTfjJ5uRMyNRb/2rOxZtsTi8FKLv7DVZMZwg==" rel="stylesheet" href="https://github.githubassets.com/assets/site-c24aa206cdd4fb0b962ca6e303f5faca.css" />
    <link crossorigin="anonymous" media="all" integrity="sha512-TtA9plNgcRtWEQtrabLyi5AfjZoT6h2cH0fHNbaLGq0hVhLeAbke8639lygQahMpdj4FHZ/P7HRjUrhM7SKY2Q==" rel="stylesheet" href="https://github.githubassets.com/assets/github-bd06d35642be41f7a7b291a8c9923889.css" />
    
    
    
    

  <meta name="viewport" content="width=device-width">
  
  <title>gallery-dl/configuration.rst at master · mikf/gallery-dl · GitHub</title>
    <meta name="description" content="Command-line program to download image-galleries and -collections from several image hosting sites - mikf/gallery-dl">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    <meta name="twitter:image:src" content="https://avatars3.githubusercontent.com/u/5375314?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="mikf/gallery-dl" /><meta name="twitter:description" content="Command-line program to download image-galleries and -collections from several image hosting sites - mikf/gallery-dl" />
    <meta property="og:image" content="https://avatars3.githubusercontent.com/u/5375314?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="mikf/gallery-dl" /><meta property="og:url" content="https://github.com/mikf/gallery-dl" /><meta property="og:description" content="Command-line program to download image-galleries and -collections from several image hosting sites - mikf/gallery-dl" />

  <link rel="assets" href="https://github.githubassets.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="C3F2:14E00:E6F641:1637A02:5D44A223" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="C3F2:14E00:E6F641:1637A02:5D44A223" /><meta name="octolytics-dimension-region_edge" content="ams" /><meta name="octolytics-dimension-region_render" content="iad" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">


<meta class="js-ga-set" name="dimension1" content="Logged Out">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="YWVlZTE2NDA2OTEzNWE0ZTY4ZDEyYTQ2ZTEwY2QyZWQzZGQwNTlmN2M2Y2MzM2NmMWI0M2IwYzMzMzcwZTFlM3x7InJlbW90ZV9hZGRyZXNzIjoiODIuNzUuMTYzLjk2IiwicmVxdWVzdF9pZCI6IkMzRjI6MTRFMDA6RTZGNjQxOjE2MzdBMDI6NUQ0NEEyMjMiLCJ0aW1lc3RhbXAiOjE1NjQ3NzkwNDMsImhvc3QiOiJnaXRodWIuY29tIn0=">

    <meta name="enabled-features" content="MARKETPLACE_FEATURED_BLOG_POSTS,MARKETPLACE_INVOICED_BILLING,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_RECOMMENDATIONS,MARKETPLACE_PENDING_INSTALLATIONS">

  <meta name="html-safe-nonce" content="34dc469c7a6e249a7e305dd4d89b1286edc88c44">

  <meta http-equiv="x-pjax-version" content="2cce593b0e01a05fd6f7a4a3f4f687e6">
  

      <link href="https://github.com/mikf/gallery-dl/commits/master.atom" rel="alternate" title="Recent Commits to gallery-dl:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/mikf/gallery-dl git https://github.com/mikf/gallery-dl.git">

  <meta name="octolytics-dimension-user_id" content="5375314" /><meta name="octolytics-dimension-user_login" content="mikf" /><meta name="octolytics-dimension-repository_id" content="25129800" /><meta name="octolytics-dimension-repository_nwo" content="mikf/gallery-dl" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="25129800" /><meta name="octolytics-dimension-repository_network_root_nwo" content="mikf/gallery-dl" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">





  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-responsive page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    


        <header class="Header-old header-logged-out js-details-container Details position-relative f4 py-2" role="banner">
  <div class="container-lg d-lg-flex flex-items-center p-responsive">
    <div class="d-flex flex-justify-between flex-items-center">
        <a class="mr-4" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
          <svg height="32" class="octicon octicon-mark-github text-white" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
        </a>

          <div class="d-lg-none css-truncate css-truncate-target width-fit p-2">
            
              <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
    <a class="Header-link" href="/mikf">mikf</a>
    /
    <a class="Header-link" href="/mikf/gallery-dl">gallery-dl</a>


          </div>

        <div class="d-flex flex-items-center">
            <a href="/join?source=header-repo"
              class="d-inline-block d-lg-none f5 text-white no-underline border border-gray-dark rounded-2 px-2 py-1 mr-3 mr-sm-5"
              data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;C3F2:14E00:E6F641:1637A02:5D44A223&quot;,&quot;originating_url&quot;:&quot;https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="2e9028920c33dcd81a9f20f17a95391643b63056c6a7254b507830683eee43b2"
              data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">
              Sign&nbsp;up
            </a>

          <button class="btn-link d-lg-none mt-1 js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
            <svg height="24" class="octicon octicon-three-bars text-white" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
          </button>
        </div>
    </div>

    <div class="HeaderMenu HeaderMenu--logged-out position-fixed top-0 right-0 bottom-0 height-fit position-lg-relative d-lg-flex flex-justify-between flex-items-center flex-auto">
      <div class="d-flex d-lg-none flex-justify-end border-bottom bg-gray-light p-3">
        <button class="btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
          <svg height="24" class="octicon octicon-x text-gray" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        </button>
      </div>

        <nav class="mt-0 px-3 px-lg-0 mb-5 mb-lg-0" aria-label="Global">
          <ul class="d-lg-flex list-style-none">
              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Why GitHub?
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>
                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <a href="/features" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Features <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                    <ul class="list-style-none f5 pb-3">
                      <li class="edge-item-fix"><a href="/features/code-review/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code review">Code review</a></li>
                      <li class="edge-item-fix"><a href="/features/project-management/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Project management">Project management</a></li>
                      <li class="edge-item-fix"><a href="/features/integrations" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Integrations">Integrations</a></li>
                      <li class="edge-item-fix"><a href="/features/actions" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Actions">Actions</a>
                          <li class="edge-item-fix"><a href="/features/package-registry" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Package Registry">Package registry</a>
                      <li class="edge-item-fix"><a href="/features#team-management" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team management">Team management</a></li>
                      <li class="edge-item-fix"><a href="/features#social-coding" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Social coding">Social coding</a></li>
                      <li class="edge-item-fix"><a href="/features#documentation" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Documentation">Documentation</a></li>
                      <li class="edge-item-fix"><a href="/features#code-hosting" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code hosting">Code hosting</a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="/customer-stories" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Customer stories">Customer stories <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="/security" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Security">Security <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="/enterprise" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Enterprise">Enterprise</a>
              </li>

              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Explore
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/explore" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Explore">Explore GitHub <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Learn &amp; contribute</h4>
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/topics" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Topics">Topics</a></li>
                        <li class="edge-item-fix"><a href="/collections" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Collections">Collections</a></li>
                      <li class="edge-item-fix"><a href="/trending" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Trending">Trending</a></li>
                      <li class="edge-item-fix"><a href="https://lab.github.com/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Learning lab">Learning Lab</a></li>
                      <li class="edge-item-fix"><a href="https://opensource.guide" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Open source guides">Open source guides</a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Connect with others</h4>
                    <ul class="list-style-none mb-0">
                      <li class="edge-item-fix"><a href="https://github.com/events" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Events">Events</a></li>
                      <li class="edge-item-fix"><a href="https://github.community" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Community forum">Community forum</a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com" class="py-2 pb-0 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Education">GitHub Education</a></li>
                    </ul>
                  </div>
                </details>
              </li>

              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="/marketplace" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace">Marketplace</a>
              </li>

              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Pricing
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                       <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-4 mt-0 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <a href="/pricing" class="pb-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing">Plans <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>

                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/pricing#feature-comparison" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare plans">Compare plans</a></li>
                      <li class="edge-item-fix"><a href="https://enterprise.github.com/contact" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Contact Sales">Contact Sales</a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="/nonprofit" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Nonprofits">Nonprofit <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com" class="py-2 pb-0 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover"  data-ga-click="(Logged out) Header, go to Education">Education <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
          </ul>
        </nav>

      <div class="d-lg-flex flex-items-center px-3 px-lg-0 text-center text-lg-left">
          <div class="d-lg-flex mb-3 mb-lg-0">
            <div class="header-search flex-self-stretch flex-lg-self-auto mr-0 mr-lg-3 mb-3 mb-lg-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="25129800" data-scoped-search-url="/mikf/gallery-dl/search" data-unscoped-search-url="/search" action="/mikf/gallery-dl/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=bf88x+uCV2zJHl6XrCsd5e9uN9EISIoKEOhGal5onN6nRotw1QvH0sfgdIbuMiXHwSgp8+Hdwq3WvIlYTkzwqA=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


</ul>

            </div>
      </label>
</form>  </div>
</div>

          </div>

        <a href="/login?return_to=%2Fmikf%2Fgallery-dl%2Fblob%2Fmaster%2Fdocs%2Fconfiguration.rst"
          class="HeaderMenu-link no-underline mr-3"
          data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;C3F2:14E00:E6F641:1637A02:5D44A223&quot;,&quot;originating_url&quot;:&quot;https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="5b5b5cb006a3892b75ec407395cd69802e5cf101385a67987b34dab5e6a2b3c2"
          data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">
          Sign&nbsp;in
        </a>
          <a href="/join?source=header-repo"
            class="HeaderMenu-link d-inline-block no-underline border border-gray-dark rounded-1 px-2 py-1"
            data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;C3F2:14E00:E6F641:1637A02:5D44A223&quot;,&quot;originating_url&quot;:&quot;https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="5b5b5cb006a3892b75ec407395cd69802e5cf101385a67987b34dab5e6a2b3c2"
            data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">
            Sign&nbsp;up
          </a>
      </div>
    </div>
  </div>
</header>

  </div>

  <div id="start-of-content" class="show-on-focus"></div>


    <div id="js-flash-container">

</div>



  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      


  








  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav pt-0 pt-lg-4 ">
    <div class="repohead-details-container clearfix container-lg p-responsive d-none d-lg-block">

      <ul class="pagehead-actions">




  <li>
    
  <a class="tooltipped tooltipped-s btn btn-sm btn-with-count" aria-label="You must be signed in to watch a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;C3F2:14E00:E6F641:1637A02:5D44A223&quot;,&quot;originating_url&quot;:&quot;https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="52432d2a2a91c5ffd0683e9398e196fa113221be9e089449b4e2161bb3c8287c" href="/login?return_to=%2Fmikf%2Fgallery-dl">
    <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
</a>    <a class="social-count" href="/mikf/gallery-dl/watchers"
       aria-label="50 users are watching this repository">
      50
    </a>

  </li>

  <li>
        <a class="btn btn-sm btn-with-count tooltipped tooltipped-s" aria-label="You must be signed in to star a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:25129800,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;C3F2:14E00:E6F641:1637A02:5D44A223&quot;,&quot;originating_url&quot;:&quot;https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="e522758bd08ffd54cecdc34a79cdf32b9cd9803244026a6d56106c87f173e4a7" href="/login?return_to=%2Fmikf%2Fgallery-dl">
      <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
      Star
</a>
    <a class="social-count js-social-count" href="/mikf/gallery-dl/stargazers"
      aria-label="630 users starred this repository">
      630
    </a>

  </li>

  <li>
      <a class="btn btn-sm btn-with-count tooltipped tooltipped-s" aria-label="You must be signed in to fork a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:25129800,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;C3F2:14E00:E6F641:1637A02:5D44A223&quot;,&quot;originating_url&quot;:&quot;https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="cde35827a641e02be2bc4cde11e278c136fef52f581863c2f2b961c845458f9f" href="/login?return_to=%2Fmikf%2Fgallery-dl">
        <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
</a>
    <a href="/mikf/gallery-dl/network/members" class="social-count"
       aria-label="78 users forked this repository">
      78
    </a>
  </li>
</ul>

      <h1 class="public ">
    <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=5375314" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/mikf">mikf</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/mikf/gallery-dl">gallery-dl</a></strong>
  

</h1>

    </div>
    
<nav class="hx_reponav reponav js-repo-nav js-sidenav-container-pjax container-lg p-responsive d-none d-lg-block"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /mikf/gallery-dl" href="/mikf/gallery-dl">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /mikf/gallery-dl/issues" href="/mikf/gallery-dl/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">49</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /mikf/gallery-dl/pulls" href="/mikf/gallery-dl/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /mikf/gallery-dl/projects" href="/mikf/gallery-dl/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


    <a data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy /mikf/gallery-dl/security/advisories" href="/mikf/gallery-dl/security/advisories">
      <svg class="octicon octicon-shield" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z"/></svg>
      Security
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse people /mikf/gallery-dl/pulse" href="/mikf/gallery-dl/pulse">
      <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
      Insights
</a>

</nav>

  <div class="reponav-wrapper reponav-small d-lg-none">
  <nav class="reponav js-reponav text-center no-wrap"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /mikf/gallery-dl" href="/mikf/gallery-dl">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /mikf/gallery-dl/issues" href="/mikf/gallery-dl/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">49</span>
          <meta itemprop="position" content="2">
</a>      </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /mikf/gallery-dl/pulls" href="/mikf/gallery-dl/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="3">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /mikf/gallery-dl/projects" href="/mikf/gallery-dl/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="4">
</a>      </span>


      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy /mikf/gallery-dl/security/advisories" href="/mikf/gallery-dl/security/advisories">
        <span itemprop="name">Security</span>
        <meta itemprop="position" content="6">
</a>
      <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /mikf/gallery-dl/pulse" href="/mikf/gallery-dl/pulse">
        Pulse
</a>

  </nav>
</div>


  </div>
<div class="container-lg clearfix new-discussion-timeline experiment-repo-nav  p-responsive">
  <div class="repository-content ">

    
    


  
    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/mikf/gallery-dl/blob/2f33bac030f1e85f659dce95fb4508c99510b2d7/docs/configuration.rst">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:ca6788da53d8535c1dac31f2ae455312 -->
          <div class="signup-prompt-bg rounded-1">
      <div class="signup-prompt p-4 text-center mb-4 rounded-1">
        <div class="position-relative">
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/prompt_dismissals/signup" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="xFU8hNLy9Ql1ORkDx0U5HeyA3cimGbhRhIgSZl9RMqIAxNRk+5P4VMJEHx9RMO8tq7TW9FkbfDCCUsu2g8Ljgw==" />
            <button type="submit" class="position-absolute top-0 right-0 btn-link link-gray" data-ga-click="(Logged out) Sign up prompt, clicked Dismiss, text:dismiss">
              Dismiss
            </button>
</form>          <h3 class="pt-2">Join GitHub today</h3>
          <p class="col-6 mx-auto">GitHub is home to over 36 million developers working together to host and review code, manage projects, and build software together.</p>
          <a class="btn btn-primary" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;files signup prompt&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;C3F2:14E00:E6F641:1637A02:5D44A223&quot;,&quot;originating_url&quot;:&quot;https://github.com/mikf/gallery-dl/blob/master/docs/configuration.rst&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="4c1dd10709a26d3e46a41fb742601bfb426e00a6376816c969e89689b467be76" data-ga-click="(Logged out) Sign up prompt, clicked Sign up, text:sign-up" href="/join?source=prompt-blob-show">Sign up</a>
        </div>
      </div>
    </div>


    <div class="d-flex flex-items-start flex-shrink-0 mb-2 flex-column flex-md-row">
      <span class="d-flex flex-justify-between width-full width-md-auto">
        
<details class="details-reset details-overlay select-menu branch-select-menu  hx_rsm" id="branch-select-menu">
  <summary class="btn btn-sm select-menu-button css-truncate"
           data-hotkey="w"
           
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target">master</span>
  </summary>

  <details-menu class="select-menu-modal hx_rsm-modal position-absolute" style="z-index: 99;" src="/mikf/gallery-dl/ref-list/master/docs/configuration.rst?source_action=show&amp;source_controller=blob" preload>
    <include-fragment class="select-menu-loading-overlay anim-pulse">
      <svg height="32" class="octicon octicon-octoface" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
    </include-fragment>
  </details-menu>
</details>

        <div class="BtnGroup flex-shrink-0 d-md-none">
          <a href="/mikf/gallery-dl/find/master"
                class="js-pjax-capture-input btn btn-sm BtnGroup-item"
                data-pjax
                data-hotkey="t">
            Find file
          </a>
          <clipboard-copy value="docs/configuration.rst" class="btn btn-sm BtnGroup-item">
            Copy path
          </clipboard-copy>
        </div>
      </span>
      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal flex-md-self-center ml-md-2 mr-md-3 my-2 my-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment"><a data-pjax="true" href="/mikf/gallery-dl"><span>gallery-dl</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/mikf/gallery-dl/tree/master/docs"><span>docs</span></a></span><span class="separator">/</span><strong class="final-path">configuration.rst</strong>
      </h2>

      <div class="BtnGroup flex-shrink-0 d-none d-md-inline-block">
        <a href="/mikf/gallery-dl/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy value="docs/configuration.rst" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
    </div>



    
  <div class="Box Box--condensed d-flex flex-column flex-shrink-0">
      <div class="Box-body d-flex flex-justify-between bg-blue-light flex-column flex-md-row flex-items-start flex-md-items-center">
        <span class="pr-md-4 f6">
          <a rel="author" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=5375314" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/mikf"><img class="avatar" src="https://avatars2.githubusercontent.com/u/5375314?s=40&amp;v=4" width="20" height="20" alt="@mikf" /></a>
          <a class="text-bold link-gray-dark lh-default v-align-middle" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=5375314" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/mikf">mikf</a>
            <span class="lh-default v-align-middle">
              <a data-pjax="true" title="update default cache directory ... again

Use a &#39;gallery-dl&#39; subdirectory in ~/.cache to adhere to how other
programs store their cached data, and call os.makedirs() so it also
works without an existing ~/.cache directory." class="link-gray" href="/mikf/gallery-dl/commit/0609afd1e470dbf48cc46e24d1f8bf69c2b6731e">update default cache directory ... again</a>
            </span>
        </span>
        <span class="d-inline-block flex-shrink-0 v-align-bottom f6 mt-2 mt-md-0">
          <a class="pr-2 text-mono link-gray" href="/mikf/gallery-dl/commit/0609afd1e470dbf48cc46e24d1f8bf69c2b6731e" data-pjax>0609afd</a>
          <relative-time datetime="2019-08-01T20:11:00Z">Aug 1, 2019</relative-time>
        </span>
      </div>

    <div class="Box-body d-flex flex-items-center flex-auto f6 border-bottom-0 flex-wrap" >
      <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
        <summary class="btn-link" aria-haspopup="dialog">
          <span><strong>3</strong> contributors</span>
        </summary>
        <details-dialog
          class="Box Box--overlay d-flex flex-column anim-fade-in fast"
          aria-label="Users who have contributed to this file"
          src="/mikf/gallery-dl/contributors/master/docs/configuration.rst/list" preload>
          <div class="Box-header">
            <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
              <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
            </button>
            <h3 class="Box-title">
              Users who have contributed to this file
            </h3>
          </div>
          <include-fragment class="octocat-spinner my-3" aria-label="Loading..."></include-fragment>
        </details-dialog>
      </details>
        <span class="">
    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=5375314" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/mikf/gallery-dl/commits/master/docs/configuration.rst?author=mikf">
      <img class="avatar mr-1" src="https://avatars2.githubusercontent.com/u/5375314?s=40&amp;v=4" width="20" height="20" alt="@mikf" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=12064918" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/mikf/gallery-dl/commits/master/docs/configuration.rst?author=Hrxn">
      <img class="avatar mr-1" src="https://avatars0.githubusercontent.com/u/12064918?s=40&amp;v=4" width="20" height="20" alt="@Hrxn" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=2178745" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/mikf/gallery-dl/commits/master/docs/configuration.rst?author=markhenrick">
      <img class="avatar mr-1" src="https://avatars3.githubusercontent.com/u/2178745?s=40&amp;v=4" width="20" height="20" alt="@markhenrick" /> 
</a>
</span>

    </div>
  </div>





    <div class="Box mt-3 position-relative">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">

  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">
      1785 lines (1396 sloc)
      <span class="file-info-divider"></span>
    52.6 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/mikf/gallery-dl/raw/master/docs/configuration.rst">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/mikf/gallery-dl/blame/master/docs/configuration.rst">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/mikf/gallery-dl/commits/master/docs/configuration.rst">History</a>
    </div>


    <div>

          <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
            aria-label="You must be signed in to make or propose changes">
            <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
          </button>
          <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
            aria-label="You must be signed in to make or propose changes">
            <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
    </div>
  </div>
</div>




      
  <div id="readme" class="Box-body readme blob instapaper_body js-code-block-container">
    <article class="markdown-body entry-content p-3 p-md-6" itemprop="text"><h1><a id="user-content-configuration" class="anchor" aria-hidden="true" href="#configuration"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Configuration</h1>
<a name="user-content-contents"></a>
<h2><a id="user-content-contents" class="anchor" aria-hidden="true" href="#contents"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Contents</h2>
<ol>
<li><a href="#extractor-options">Extractor Options</a></li>
<li><a href="#extractor-specific-options">Extractor-specific Options</a></li>
<li><a href="#downloader-options">Downloader Options</a></li>
<li><a href="#output-options">Output Options</a></li>
<li><a href="#postprocessor-options">Postprocessor Options</a></li>
<li><a href="#miscellaneous-options">Miscellaneous Options</a></li>
<li><a href="#api-tokens-ids">API Tokens &amp; IDs</a></li>
</ol>
<a name="user-content-extractor-options"></a>
<h2><a id="user-content-extractor-options" class="anchor" aria-hidden="true" href="#extractor-options"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Extractor Options</h2>
<p>Each extractor is identified by its <code>category</code> and <code>subcategory</code>.
The <code>category</code> is the lowercase site name without any spaces or special
characters, which is usually just the module name
(<code>pixiv</code>, <code>danbooru</code>, ...).
The <code>subcategory</code> is a lowercase word describing the general functionality
of that extractor (<code>user</code>, <code>favorite</code>, <code>manga</code>, ...).</p>
<p>Each one of the following options can be specified on multiple levels of the
configuration tree:</p>
<table>




<tbody valign="top">
<tr><td>Base level:</td>
<td><code>extractor.&lt;option-name&gt;</code></td>
</tr>
<tr><td>Category level:</td>
<td><code>extractor.&lt;category&gt;.&lt;option-name&gt;</code></td>
</tr>
<tr><td>Subcategory level:</td>
<td><code>extractor.&lt;category&gt;.&lt;subcategory&gt;.&lt;option-name&gt;</code></td>
</tr>
</tbody>
</table>
<p>A value in a "deeper" level hereby overrides a value of the same name on a
lower level. Setting the <code>extractor.pixiv.filename</code> value, for example, lets
you specify a general filename pattern for all the different pixiv extractors.
Using the <code>extractor.pixiv.user.filename</code> value lets you override this
general pattern specifically for <code>PixivUserExtractor</code> instances.</p>
<p>The <code>category</code> and <code>subcategory</code> of all extractors are included in the
output of <code>gallery-dl --list-extractors</code>. For a specific URL these values
can also be determined by using the <code>-K</code>/<code>--list-keywords</code> command-line
option (see the example below).</p>
<a name="user-content-extractor-filename"></a>
<h3><a id="user-content-extractorfilename" class="anchor" aria-hidden="true" href="#extractorfilename"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.filename</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Example</td>
<td><code>"{manga}_c{chapter}_{page:&gt;03}.{extension}"</code></td>
</tr>
<tr><td>Description</td>
<td><p>A <a href="https://docs.python.org/3/library/string.html#formatstrings" rel="nofollow">format string</a> to build the resulting filename
for a downloaded file.</p>
<p>The available replacement keys depend on the extractor used. A list
of keys for a specific one can be acquired by calling <em>gallery-dl</em>
with the <code>-K</code>/<code>--list-keywords</code> command-line option.
For example:</p>
<pre>$ gallery-dl -K http://seiga.nicovideo.jp/seiga/im5977527
Keywords for directory names:
-----------------------------
category
  seiga
subcategory
  image

Keywords for filenames:
-----------------------
category
  seiga
extension
  None
image-id
  5977527
subcategory
  image
</pre>
<p>Note: Even if the value of the <code>extension</code> key is missing or
<code>None</code>, it will filled in later when the file download is
starting. This key is therefore always available to provide
a valid filename extension.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-directory"></a>
<h3><a id="user-content-extractordirectory" class="anchor" aria-hidden="true" href="#extractordirectory"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.directory</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>list</code> of <code>strings</code></td>
</tr>
<tr><td>Example</td>
<td><code>["{category}", "{manga}", "c{chapter} - {title}"]</code></td>
</tr>
<tr><td>Description</td>
<td><p>A list of <a href="https://docs.python.org/3/library/string.html#formatstrings" rel="nofollow">format strings</a> for the resulting target directory.</p>
<p>Each individual string in such a list represents a single path
segment, which will be joined together and appended to the
<a href="#extractor-base-directory">base-directory</a> to form the complete target directory path.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-base-directory"></a>
<h3><a id="user-content-extractorbase-directory" class="anchor" aria-hidden="true" href="#extractorbase-directory"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.base-directory</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><a href="#path"><code>Path</code></a></td>
</tr>
<tr><td>Default</td>
<td><code>"./gallery-dl/"</code></td>
</tr>
<tr><td>Description</td>
<td>Directory path used as the base for all download destinations.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-restrict-filenames"></a>
<h3><a id="user-content-extractorrestrict-filenames" class="anchor" aria-hidden="true" href="#extractorrestrict-filenames"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.restrict-filenames</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"auto"</code></td>
</tr>
<tr><td>Example</td>
<td><code>"/!? ()[]{}"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Characters to replace with underscores (<code>_</code>) when generating
directory and file names.</p>
<p>Special values:</p>
<ul>
<li><code>"auto"</code>: Use characters from <code>"unix"</code> or <code>"windows"</code>
depending on the local operating system</li>
<li><code>"unix"</code>: <code>"/"</code></li>
<li><code>"windows"</code>: <code>"&lt;&gt;:\"\\|/?*"</code></li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-skip"></a>
<h3><a id="user-content-extractorskip" class="anchor" aria-hidden="true" href="#extractorskip"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.skip</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code> or <code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls the behavior when downloading files whose filename
already exists.</p>
<ul>
<li><code>true</code>: Skip downloads</li>
<li><code>false</code>: Overwrite already existing files</li>
<li><code>"abort"</code>: Abort the current extractor run</li>
<li><code>"abort:N"</code>: Skip downloads and abort extractor run
after <code>N</code> consecutive skips</li>
<li><code>"exit"</code>: Exit the program altogether</li>
<li><code>"exit:N"</code>: Skip downloads and exit the program
after <code>N</code> consecutive skips</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-sleep"></a>
<h3><a id="user-content-extractorsleep" class="anchor" aria-hidden="true" href="#extractorsleep"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.sleep</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>float</code></td>
</tr>
<tr><td>Default</td>
<td><code>0</code></td>
</tr>
<tr><td>Description</td>
<td>Number of seconds to sleep before each download.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-username-password"></a>
<h3><a id="user-content-extractorusername--password" class="anchor" aria-hidden="true" href="#extractorusername--password"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.username &amp; .password</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td><p>The username and password to use when attempting to log in to
another site.</p>
<p>Specifying username and password is required for the
<code>pixiv</code>, <code>nijie</code>, and <code>seiga</code>
modules and optional (but strongly recommended) for
<code>danbooru</code>, <code>exhentai</code>, <code>idolcomplex</code>, <code>instagram</code>,
<code>luscious</code>, <code>sankaku</code>, <code>tsumino</code>, and <code>twitter</code>.</p>
<p>These values can also be set via the <code>-u/--username</code> and
<code>-p/--password</code> command-line options or by using a <a href="https://stackoverflow.com/tags/.netrc/info" rel="nofollow"><code>.netrc</code></a> file.
(see <a href="https://github.com/mikf/gallery-dl#5authentication">Authentication</a>)</p>
<p>Note: The password for <code>danbooru</code> is the API key found in your
user profile, not the password for your account.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-netrc"></a>
<h3><a id="user-content-extractornetrc" class="anchor" aria-hidden="true" href="#extractornetrc"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.netrc</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Enable the use of <a href="https://stackoverflow.com/tags/.netrc/info" rel="nofollow"><code>.netrc</code></a> authentication data.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-cookies"></a>
<h3><a id="user-content-extractorcookies" class="anchor" aria-hidden="true" href="#extractorcookies"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.cookies</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><a href="#path"><code>Path</code></a> or <code>object</code></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td><p>Source to read additional cookies from.</p>
<ul>
<li>If this is a <a href="#path"><code>Path</code></a>, it specifies a
Mozilla/Netscape format cookies.txt file.</li>
<li>If this is an <code>object</code>, its key-value pairs, which should both
be <code>strings</code>, will be used as cookie-names and -values.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-proxy"></a>
<h3><a id="user-content-extractorproxy" class="anchor" aria-hidden="true" href="#extractorproxy"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.proxy</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code> or <code>object</code></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td><p>Proxy (or proxies) to be used for remote connections.</p>
<ul>
<li><p>If this is a <code>string</code>, it is the proxy URL for all
outgoing requests.</p>
</li>
<li><p>If this is an <code>object</code>, it is a scheme-to-proxy mapping to
specify different proxy URLs for each scheme.
It is also possible to set a proxy for a specific host by using
<code>scheme://host</code> as key.
See <a href="http://docs.python-requests.org/en/master/user/advanced/#proxies" rel="nofollow">Requests' proxy documentation</a> for more details.</p>
<p>Example:</p>
<pre>{
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
    "http://10.20.1.128": "http://10.10.1.10:5323"
}
</pre>
</li>
</ul>
<p>Note: All proxy URLs should include a scheme,
otherwise <code>http://</code> is assumed.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-user-agent"></a>
<h3><a id="user-content-extractoruser-agent" class="anchor" aria-hidden="true" href="#extractoruser-agent"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.user-agent</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"</code></td>
</tr>
<tr><td>Description</td>
<td><p>User-Agent header value to be used for HTTP requests.</p>
<p>Note: This option has no effect on pixiv and
readcomiconline extractors, as these need specific values to
function correctly.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-keywords"></a>
<h3><a id="user-content-extractorkeywords" class="anchor" aria-hidden="true" href="#extractorkeywords"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.keywords</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>object</code></td>
</tr>
<tr><td>Example</td>
<td><code>{"type": "Pixel Art", "type_id": 123}</code></td>
</tr>
<tr><td>Description</td>
<td>Additional key-value pairs to be added to each metadata dictionary.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-keywords-default"></a>
<h3><a id="user-content-extractorkeywords-default" class="anchor" aria-hidden="true" href="#extractorkeywords-default"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.keywords-default</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td>any</td>
</tr>
<tr><td>Default</td>
<td><code>"None"</code></td>
</tr>
<tr><td>Description</td>
<td>Default value used for missing or undefined keyword names in
format strings.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-category-transfer"></a>
<h3><a id="user-content-extractorcategory-transfer" class="anchor" aria-hidden="true" href="#extractorcategory-transfer"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.category-transfer</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td>Extractor-specific</td>
</tr>
<tr><td>Description</td>
<td>Transfer an extractor's (sub)category values to all child
extractors spawned by it, to let them inherit their parent's
config options.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-archive"></a>
<h3><a id="user-content-extractorarchive" class="anchor" aria-hidden="true" href="#extractorarchive"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.archive</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><a href="#path"><code>Path</code></a></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td><p>File to store IDs of downloaded files in. Downloads of files
already recorded in this archive file will be <a href="#extractor-skip">skipped</a>.</p>
<p>The resulting archive file is not a plain text file but an SQLite3
database, as either lookup operations are significantly faster or
memory requirements are significantly lower when the
amount of stored IDs gets reasonably large.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-archive-format"></a>
<h3><a id="user-content-extractorarchive-format" class="anchor" aria-hidden="true" href="#extractorarchive-format"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.archive-format</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Example</td>
<td><code>"{id}_{offset}"</code></td>
</tr>
<tr><td>Description</td>
<td>An alternative <a href="https://docs.python.org/3/library/string.html#formatstrings" rel="nofollow">format string</a> to build archive IDs with.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-postprocessors"></a>
<h3><a id="user-content-extractorpostprocessors" class="anchor" aria-hidden="true" href="#extractorpostprocessors"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.postprocessors</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>list</code> of <a href="#postprocessor-configuration"><code>Postprocessor Configuration</code></a> objects</td>
</tr>
<tr><td>Example</td>
<td><pre lang="first">[
    {"name": "zip", "compression": "zip"},
    {"name": "exec",  "command": ["/home/foobar/script", "{category}", "{image_id}"]}
]
</pre>
</td>
</tr>
<tr><td>Description</td>
<td>A list of post-processors to be applied to each downloaded file
in the same order as they are specified.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-retries"></a>
<h3><a id="user-content-extractorretries" class="anchor" aria-hidden="true" href="#extractorretries"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.retries</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>integer</code></td>
</tr>
<tr><td>Default</td>
<td><code>4</code></td>
</tr>
<tr><td>Description</td>
<td>Maximum number of times a failed HTTP request is retried before
giving up or <code>-1</code> for infinite retries.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-timeout"></a>
<h3><a id="user-content-extractortimeout" class="anchor" aria-hidden="true" href="#extractortimeout"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.timeout</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>float</code> or <code>null</code></td>
</tr>
<tr><td>Default</td>
<td><code>30</code></td>
</tr>
<tr><td>Description</td>
<td><p>Amount of time (in seconds) to wait for a successful connection
and response from a remote server.</p>
<p>This value gets internally used as the <a href="https://docs.python-requests.org/en/latest/user/advanced/#timeouts" rel="nofollow"><code>timeout</code></a> parameter for the
<a href="https://docs.python-requests.org/en/master/api/#requests.request" rel="nofollow"><code>requests.request()</code></a> method.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-verify"></a>
<h3><a id="user-content-extractorverify" class="anchor" aria-hidden="true" href="#extractorverify"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.verify</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code> or <code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls whether to verify SSL/TLS certificates for HTTPS requests.</p>
<p>If this is a <code>string</code>, it must be the path to a CA bundle to use
instead of the default certificates.</p>
<p>This value gets internally used as the <a href="https://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification" rel="nofollow"><code>verify</code></a> parameter for the
<a href="https://docs.python-requests.org/en/master/api/#requests.request" rel="nofollow"><code>requests.request()</code></a> method.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-download"></a>
<h3><a id="user-content-extractordownload" class="anchor" aria-hidden="true" href="#extractordownload"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.download</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls whether to download media files.</p>
<p>Setting this to <code>false</code> won't download any files, but all other
functions (<a href="#extractor-postprocessors">postprocessors</a>, <a href="#extractor-archive">download archive</a>, etc.)
will be executed as normal.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-image-range"></a>
<h3><a id="user-content-extractorimage-range" class="anchor" aria-hidden="true" href="#extractorimage-range"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.image-range</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Example</td>
<td><div>
<div><code>"10-20"</code>,</div>
<div><code>"-5, 10, 30-50, 100-"</code></div>
</div>
</td>
</tr>
<tr><td>Description</td>
<td><p>Index-range(s) specifying which images to download.</p>
<p>Note: The index of the first image is <code>1</code>.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-chapter-range"></a>
<h3><a id="user-content-extractorchapter-range" class="anchor" aria-hidden="true" href="#extractorchapter-range"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.chapter-range</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Description</td>
<td>Like <a href="#extractor-image-range">image-range</a>, but applies to delegated URLs
like manga-chapters, etc.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-image-filter"></a>
<h3><a id="user-content-extractorimage-filter" class="anchor" aria-hidden="true" href="#extractorimage-filter"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.image-filter</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Example</td>
<td><div>
<div><code>"width &gt;= 1200 and width/height &gt; 1.2"</code>,</div>
<div><code>"re.search(r'foo(bar)+', description)"</code></div>
</div>
</td>
</tr>
<tr><td>Description</td>
<td><div>
<div>Python expression controlling which images to download.</div>
<div>Files for which the expression evaluates to <code>False</code>
are ignored.</div>
<div>Available keys are the filename-specific ones listed
by <code>-K</code> or <code>-j</code>.</div>
</div>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-chapter-filter"></a>
<h3><a id="user-content-extractorchapter-filter" class="anchor" aria-hidden="true" href="#extractorchapter-filter"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.chapter-filter</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Description</td>
<td>Like <a href="#extractor-image-filter">image-filter</a>, but applies to delegated URLs
like manga-chapters, etc.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-image-unique"></a>
<h3><a id="user-content-extractorimage-unique" class="anchor" aria-hidden="true" href="#extractorimage-unique"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.image-unique</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Ignore image URLs that have been encountered before during the
current extractor run.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-chapter-unique"></a>
<h3><a id="user-content-extractorchapter-unique" class="anchor" aria-hidden="true" href="#extractorchapter-unique"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.chapter-unique</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Like <a href="#extractor-image-unique">image-unique</a>, but applies to delegated URLs
like manga-chapters, etc.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-date-format"></a>
<h3><a id="user-content-extractordate-format" class="anchor" aria-hidden="true" href="#extractordate-format"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.*.date-format</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"%Y-%m-%dT%H:%M:%S"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Format string used to parse <code>string</code> values of
date-min and date-max.</p>
<p>See <a href="https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior" rel="nofollow">strftime() and strptime() Behavior</a> for a list of formatting directives.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-specific-options"></a>
<h2><a id="user-content-extractor-specific-options" class="anchor" aria-hidden="true" href="#extractor-specific-options"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Extractor-specific Options</h2>
<a name="user-content-extractor-artstation-external"></a>
<h3><a id="user-content-extractorartstationexternal" class="anchor" aria-hidden="true" href="#extractorartstationexternal"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.artstation.external</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Try to follow external URLs of embedded players.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-deviantart-extra"></a>
<h3><a id="user-content-extractordeviantartextra" class="anchor" aria-hidden="true" href="#extractordeviantartextra"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.deviantart.extra</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td><p>Download extra Sta.sh resources from description texts.</p>
<p>Note: Enabling this option also enables <a href="#extractor-deviantart-metadata">deviantart.metadata</a>.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-deviantart-flat"></a>
<h3><a id="user-content-extractordeviantartflat" class="anchor" aria-hidden="true" href="#extractordeviantartflat"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.deviantart.flat</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Select the directory structure created by the Gallery- and
Favorite-Extractors.</p>
<ul>
<li><code>true</code>: Use a flat directory structure.</li>
<li><code>false</code>: Collect a list of all gallery-folders or
favorites-collections and transfer any further work to other
extractors (<code>folder</code> or <code>collection</code>), which will then
create individual subdirectories for each of them.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-deviantart-folders"></a>
<h3><a id="user-content-extractordeviantartfolders" class="anchor" aria-hidden="true" href="#extractordeviantartfolders"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.deviantart.folders</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td><p>Provide a <code>folders</code> metadata field that contains the names of all
folders a deviation is present in.</p>
<p>Note: Gathering this information requires a lot of API calls.
Use with caution.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-deviantart-journals"></a>
<h3><a id="user-content-extractordeviantartjournals" class="anchor" aria-hidden="true" href="#extractordeviantartjournals"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.deviantart.journals</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"html"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Selects the output format of journal entries.</p>
<ul>
<li><code>"html"</code>: HTML with (roughly) the same layout as on DeviantArt.</li>
<li><code>"text"</code>: Plain text with image references and HTML tags removed.</li>
<li><code>"none"</code>: Don't download journals.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-deviantart-mature"></a>
<h3><a id="user-content-extractordeviantartmature" class="anchor" aria-hidden="true" href="#extractordeviantartmature"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.deviantart.mature</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Enable mature content.</p>
<p>This option simply sets the <a href="https://www.deviantart.com/developers/http/v1/20160316/object/deviation" rel="nofollow"><code>mature_content</code></a> parameter for API
calls to either <code>"true"</code> or <code>"false"</code> and does not do any other
form of content filtering.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-deviantart-metadata"></a>
<h3><a id="user-content-extractordeviantartmetadata" class="anchor" aria-hidden="true" href="#extractordeviantartmetadata"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.deviantart.metadata</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Request extended metadata for deviation objects to additionally
provide <code>description</code>, <code>tags</code>, <code>license</code> and <code>is_watching</code>
fields.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-deviantart-original"></a>
<h3><a id="user-content-extractordeviantartoriginal" class="anchor" aria-hidden="true" href="#extractordeviantartoriginal"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.deviantart.original</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code> or <code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Download original files if available.</p>
<p>Setting this option to <code>"images"</code> only downloads original
files if they are images and falls back to preview versions for
everything else (archives, etc.).</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-deviantart-refresh-token"></a>
<h3><a id="user-content-extractordeviantartrefresh-token" class="anchor" aria-hidden="true" href="#extractordeviantartrefresh-token"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.deviantart.refresh-token</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td><p>The <code>refresh_token</code> value you get from linking your
DeviantArt account to <em>gallery-dl</em>.</p>
<p>Using a <code>refresh_token</code> allows you to access private or otherwise
not publicly available deviations.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-deviantart-wait-min"></a>
<h3><a id="user-content-extractordeviantartwait-min" class="anchor" aria-hidden="true" href="#extractordeviantartwait-min"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.deviantart.wait-min</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>integer</code></td>
</tr>
<tr><td>Default</td>
<td><code>0</code></td>
</tr>
<tr><td>Description</td>
<td><p>Minimum wait time in seconds before API requests.</p>
<p>Note: This value will internally be rounded up
to the next power of 2.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-exhentai-limits"></a>
<h3><a id="user-content-extractorexhentailimits" class="anchor" aria-hidden="true" href="#extractorexhentailimits"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.exhentai.limits</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Check image download limits
and stop extraction when they are exceeded.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-exhentai-original"></a>
<h3><a id="user-content-extractorexhentaioriginal" class="anchor" aria-hidden="true" href="#extractorexhentaioriginal"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.exhentai.original</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Download full-sized original images if available.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-exhentai-wait-min-wait-max"></a>
<h3><a id="user-content-extractorexhentaiwait-min--wait-max" class="anchor" aria-hidden="true" href="#extractorexhentaiwait-min--wait-max"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.exhentai.wait-min &amp; .wait-max</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>float</code></td>
</tr>
<tr><td>Default</td>
<td><code>3.0</code> and <code>6.0</code></td>
</tr>
<tr><td>Description</td>
<td><p>Minimum and maximum wait time in seconds between each image</p>
<p>ExHentai detects and blocks automated downloaders.
<em>gallery-dl</em> waits a randomly selected number of
seconds between <code>wait-min</code> and <code>wait-max</code> after
each image to prevent getting blocked.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-flickr-access-token-access-token-secret"></a>
<h3><a id="user-content-extractorflickraccess-token--access-token-secret" class="anchor" aria-hidden="true" href="#extractorflickraccess-token--access-token-secret"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.flickr.access-token &amp; .access-token-secret</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td>The <code>access_token</code> and <code>access_token_secret</code> values you get
from linking your Flickr account to <em>gallery-dl</em>.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-flickr-videos"></a>
<h3><a id="user-content-extractorflickrvideos" class="anchor" aria-hidden="true" href="#extractorflickrvideos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.flickr.videos</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Extract and download videos.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-flickr-size-max"></a>
<h3><a id="user-content-extractorflickrsize-max" class="anchor" aria-hidden="true" href="#extractorflickrsize-max"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.flickr.size-max</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>integer</code> or <code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td><p>Sets the maximum allowed size for downloaded images.</p>
<ul>
<li>If this is an <code>integer</code>, it specifies the maximum image dimension
(width and height) in pixels.</li>
<li>If this is a <code>string</code>, it should be one of Flickr's format specifiers
(<code>"Original"</code>, <code>"Large"</code>, ... or <code>"o"</code>, <code>"k"</code>, <code>"h"</code>,
<code>"l"</code>, ...) to use as an upper limit.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-gelbooru-api"></a>
<h3><a id="user-content-extractorgelbooruapi" class="anchor" aria-hidden="true" href="#extractorgelbooruapi"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.gelbooru.api</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Enable use of Gelbooru's API.</p>
<p>Set this value to false if the API has been disabled to switch
to manual information extraction.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-gfycat-format"></a>
<h3><a id="user-content-extractorgfycatformat" class="anchor" aria-hidden="true" href="#extractorgfycatformat"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.gfycat.format</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"mp4"</code></td>
</tr>
<tr><td>Description</td>
<td><p>The name of the preferred animation format, which can be one of
<code>"mp4"</code>, <code>"webm"</code>, <code>"gif"</code>, <code>"webp"</code> or <code>"mjpg"</code>.</p>
<p>If the selected format is not available, <code>"mp4"</code>, <code>"webm"</code>
and <code>"gif"</code> (in that order) will be tried instead, until an
available format is found.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-imgur-mp4"></a>
<h3><a id="user-content-extractorimgurmp4" class="anchor" aria-hidden="true" href="#extractorimgurmp4"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.imgur.mp4</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code> or <code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls whether to choose the GIF or MP4 version of an animation.</p>
<ul>
<li><code>true</code>: Follow Imgur's advice and choose MP4 if the
<code>prefer_video</code> flag in an image's metadata is set.</li>
<li><code>false</code>: Always choose GIF.</li>
<li><code>"always"</code>: Always choose MP4.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-kissmanga-captcha"></a>
<h3><a id="user-content-extractorkissmangacaptcha" class="anchor" aria-hidden="true" href="#extractorkissmangacaptcha"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.kissmanga.captcha</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"stop"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls how to handle redirects to CAPTCHA pages.</p>
<ul>
<li><code>"stop</code>: Stop the current extractor run.</li>
<li><code>"wait</code>: Ask the user to solve the CAPTCHA and wait.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-oauth-browser"></a>
<h3><a id="user-content-extractoroauthbrowser" class="anchor" aria-hidden="true" href="#extractoroauthbrowser"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.oauth.browser</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls how a user is directed to an OAuth authorization site.</p>
<ul>
<li><code>true</code>: Use Python's <a href="https://docs.python.org/3/library/webbrowser.html" rel="nofollow"><code>webbrowser.open()</code></a> method to automatically
open the URL in the user's browser.</li>
<li><code>false</code>: Ask the user to copy &amp; paste an URL from the terminal.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-photobucket-subalbums"></a>
<h3><a id="user-content-extractorphotobucketsubalbums" class="anchor" aria-hidden="true" href="#extractorphotobucketsubalbums"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.photobucket.subalbums</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Download subalbums.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-pixiv-ugoira"></a>
<h3><a id="user-content-extractorpixivugoira" class="anchor" aria-hidden="true" href="#extractorpixivugoira"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.pixiv.ugoira</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Download Pixiv's Ugoira animations or ignore them.</p>
<p>These animations come as a <code>.zip</code> file containing all the single
animation frames in JPEG format.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-plurk-comments"></a>
<h3><a id="user-content-extractorplurkcomments" class="anchor" aria-hidden="true" href="#extractorplurkcomments"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.plurk.comments</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Also search Plurk comments for URLs.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-reactor-wait-min-wait-max"></a>
<h3><a id="user-content-extractorreactorwait-min--wait-max" class="anchor" aria-hidden="true" href="#extractorreactorwait-min--wait-max"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.reactor.wait-min &amp; .wait-max</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>float</code></td>
</tr>
<tr><td>Default</td>
<td><code>3.0</code> and <code>6.0</code></td>
</tr>
<tr><td>Description</td>
<td>Minimum and maximum wait time in seconds between HTTP requests
during the extraction process.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-readcomiconline-captcha"></a>
<h3><a id="user-content-extractorreadcomiconlinecaptcha" class="anchor" aria-hidden="true" href="#extractorreadcomiconlinecaptcha"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.readcomiconline.captcha</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"stop"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls how to handle redirects to CAPTCHA pages.</p>
<ul>
<li><code>"stop</code>: Stop the current extractor run.</li>
<li><code>"wait</code>: Ask the user to solve the CAPTCHA and wait.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-recursive-blacklist"></a>
<h3><a id="user-content-extractorrecursiveblacklist" class="anchor" aria-hidden="true" href="#extractorrecursiveblacklist"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.recursive.blacklist</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>list</code> of <code>strings</code></td>
</tr>
<tr><td>Default</td>
<td><code>["directlink", "oauth", "recursive", "test"]</code></td>
</tr>
<tr><td>Description</td>
<td>A list of extractor categories which should be ignored when using
the <code>recursive</code> extractor.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-reddit-comments"></a>
<h3><a id="user-content-extractorredditcomments" class="anchor" aria-hidden="true" href="#extractorredditcomments"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.reddit.comments</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>integer</code> or <code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>500</code></td>
</tr>
<tr><td>Description</td>
<td><p>The value of the <code>limit</code> parameter when loading
a submission and its comments.
This number (roughly) specifies the total amount of comments
being retrieved with the first API call.</p>
<p>Reddit's internal default and maximum values for this parameter
appear to be 200 and 500 respectively.</p>
<p>The value 0 ignores all comments and significantly reduces the
time required when scanning a subreddit.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-reddit-morecomments"></a>
<h3><a id="user-content-extractorredditmorecomments" class="anchor" aria-hidden="true" href="#extractorredditmorecomments"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.reddit.morecomments</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td><p>Retrieve additional comments by resolving the <code>more</code> comment
stubs in the base comment tree.</p>
<p>This requires 1 additional API call for every 100 extra comments.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-reddit-date-min-date-max"></a>
<h3><a id="user-content-extractorredditdate-min--date-max" class="anchor" aria-hidden="true" href="#extractorredditdate-min--date-max"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.reddit.date-min &amp; .date-max</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><a href="#date"><code>Date</code></a></td>
</tr>
<tr><td>Default</td>
<td><code>0</code> and <code>253402210800</code> (timestamp of <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime.max" rel="nofollow"><code>datetime.max</code></a>)</td>
</tr>
<tr><td>Description</td>
<td>Ignore all submissions posted before/after this date.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-reddit-id-min-id-max"></a>
<h3><a id="user-content-extractorredditid-min--id-max" class="anchor" aria-hidden="true" href="#extractorredditid-min--id-max"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.reddit.id-min &amp; .id-max</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Example</td>
<td><code>"6kmzv2"</code></td>
</tr>
<tr><td>Description</td>
<td>Ignore all submissions posted before/after the submission with
this ID.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-reddit-recursion"></a>
<h3><a id="user-content-extractorredditrecursion" class="anchor" aria-hidden="true" href="#extractorredditrecursion"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.reddit.recursion</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>integer</code></td>
</tr>
<tr><td>Default</td>
<td><code>0</code></td>
</tr>
<tr><td>Description</td>
<td><p>Reddit extractors can recursively visit other submissions
linked to in the initial set of submissions.
This value sets the maximum recursion depth.</p>
<p>Special values:</p>
<ul>
<li><code>0</code>: Recursion is disabled</li>
<li><code>-1</code>: Infinite recursion (don't do this)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-reddit-refresh-token"></a>
<h3><a id="user-content-extractorredditrefresh-token" class="anchor" aria-hidden="true" href="#extractorredditrefresh-token"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.reddit.refresh-token</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td><p>The <code>refresh_token</code> value you get from linking your
Reddit account to <em>gallery-dl</em>.</p>
<p>Using a <code>refresh_token</code> allows you to access private or otherwise
not publicly available subreddits, given that your account is
authorized to do so,
but requests to the reddit API are going to be rate limited
at 600 requests every 10 minutes/600 seconds.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-sankaku-wait-min-wait-max"></a>
<h3><a id="user-content-extractorsankakuwait-min--wait-max" class="anchor" aria-hidden="true" href="#extractorsankakuwait-min--wait-max"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.sankaku.wait-min &amp; .wait-max</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>float</code></td>
</tr>
<tr><td>Default</td>
<td><code>3.0</code> and <code>6.0</code></td>
</tr>
<tr><td>Description</td>
<td><p>Minimum and maximum wait time in seconds between each image</p>
<p>Sankaku Channel responds with <code>429 Too Many Requests</code> if it
receives too many HTTP requests in a certain amount of time.
Waiting a few seconds between each request tries to prevent that.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-smugmug-videos"></a>
<h3><a id="user-content-extractorsmugmugvideos" class="anchor" aria-hidden="true" href="#extractorsmugmugvideos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.smugmug.videos</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Download video files.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-tumblr-avatar"></a>
<h3><a id="user-content-extractortumblravatar" class="anchor" aria-hidden="true" href="#extractortumblravatar"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.tumblr.avatar</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Download blog avatars.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-tumblr-date-min-date-max"></a>
<h3><a id="user-content-extractortumblrdate-min--date-max" class="anchor" aria-hidden="true" href="#extractortumblrdate-min--date-max"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.tumblr.date-min &amp; .date-max</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><a href="#date"><code>Date</code></a></td>
</tr>
<tr><td>Default</td>
<td><code>0</code> and <code>null</code></td>
</tr>
<tr><td>Description</td>
<td>Ignore all posts published before/after this date.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-tumblr-external"></a>
<h3><a id="user-content-extractortumblrexternal" class="anchor" aria-hidden="true" href="#extractortumblrexternal"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.tumblr.external</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Follow external URLs (e.g. from "Link" posts) and try to extract
images from them.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-tumblr-inline"></a>
<h3><a id="user-content-extractortumblrinline" class="anchor" aria-hidden="true" href="#extractortumblrinline"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.tumblr.inline</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Search posts for inline images and videos.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-tumblr-reblogs"></a>
<h3><a id="user-content-extractortumblrreblogs" class="anchor" aria-hidden="true" href="#extractortumblrreblogs"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.tumblr.reblogs</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code> or <code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><ul>
<li><code>true</code>: Extract media from reblogged posts</li>
<li><code>false</code>: Skip reblogged posts</li>
<li><code>"same-blog"</code>: Skip reblogged posts unless the original post
is from the same blog</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-tumblr-posts"></a>
<h3><a id="user-content-extractortumblrposts" class="anchor" aria-hidden="true" href="#extractortumblrposts"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.tumblr.posts</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code> or <code>list</code> of <code>strings</code></td>
</tr>
<tr><td>Default</td>
<td><code>"all"</code></td>
</tr>
<tr><td>Example</td>
<td><code>"video,audio,link"</code> or <code>["video", "audio", "link"]</code></td>
</tr>
<tr><td>Description</td>
<td><p>A (comma-separated) list of post types to extract images, etc. from.</p>
<p>Possible types are <code>text</code>, <code>quote</code>, <code>link</code>, <code>answer</code>,
<code>video</code>, <code>audio</code>, <code>photo</code>, <code>chat</code>.</p>
<p>You can use <code>"all"</code> instead of listing all types separately.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-twitter-content"></a>
<h3><a id="user-content-extractortwittercontent" class="anchor" aria-hidden="true" href="#extractortwittercontent"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.twitter.content</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Extract tweet text as <code>content</code> metadata.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-twitter-retweets"></a>
<h3><a id="user-content-extractortwitterretweets" class="anchor" aria-hidden="true" href="#extractortwitterretweets"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.twitter.retweets</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Extract images from retweets.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-twitter-videos"></a>
<h3><a id="user-content-extractortwittervideos" class="anchor" aria-hidden="true" href="#extractortwittervideos"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.twitter.videos</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Use <a href="https://github.com/ytdl-org/youtube-dl">youtube-dl</a> to download from video tweets.</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-wallhaven-api-key"></a>
<h3><a id="user-content-extractorwallhavenapi-key" class="anchor" aria-hidden="true" href="#extractorwallhavenapi-key"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.wallhaven.api-key</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td><p>Your  <a href="https://wallhaven.cc/settings/account" rel="nofollow">API Key</a> to use
your account's browsing settings and default filters when searching.</p>
<p>See <a href="https://wallhaven.cc/help/api" rel="nofollow">https://wallhaven.cc/help/api</a> for more information.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-booru-tags"></a>
<h3><a id="user-content-extractorboorutags" class="anchor" aria-hidden="true" href="#extractorboorutags"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.[booru].tags</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td><p>Categorize tags by their respective types
and provide them as <code>tags_&lt;type&gt;</code> metadata fields.</p>
<p>Note: This requires 1 additional HTTP request for each post.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-manga-extractor-chapter-reverse"></a>
<h3><a id="user-content-extractormanga-extractorchapter-reverse" class="anchor" aria-hidden="true" href="#extractormanga-extractorchapter-reverse"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.[manga-extractor].chapter-reverse</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td><p>Reverse the order of chapter URLs extracted from manga pages.</p>
<ul>
<li><code>true</code>: Start with the latest chapter</li>
<li><code>false</code>: Start with the first chapter</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-options"></a>
<h2><a id="user-content-downloader-options" class="anchor" aria-hidden="true" href="#downloader-options"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Downloader Options</h2>
<a name="user-content-downloader-enabled"></a>
<h3><a id="user-content-downloaderenabled" class="anchor" aria-hidden="true" href="#downloaderenabled"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.*.enabled</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Enable/Disable this downloader module.</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-mtime"></a>
<h3><a id="user-content-downloadermtime" class="anchor" aria-hidden="true" href="#downloadermtime"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.*.mtime</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Use <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.29" rel="nofollow"><code>Last-Modified</code></a> HTTP response headers
to set file modification times.</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-part"></a>
<h3><a id="user-content-downloaderpart" class="anchor" aria-hidden="true" href="#downloaderpart"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.*.part</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls the use of <code>.part</code> files during file downloads.</p>
<ul>
<li><code>true</code>: Write downloaded data into <code>.part</code> files and rename
them upon download completion. This mode additionally supports
resuming incomplete downloads.</li>
<li><code>false</code>: Do not use <code>.part</code> files and write data directly
into the actual output files.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-part-directory"></a>
<h3><a id="user-content-downloaderpart-directory" class="anchor" aria-hidden="true" href="#downloaderpart-directory"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.*.part-directory</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><a href="#path"><code>Path</code></a></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td><p>Alternate location for <code>.part</code> files.</p>
<p>Missing directories will be created as needed.
If this value is <code>null</code>, <code>.part</code> files are going to be stored
alongside the actual output files.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-rate"></a>
<h3><a id="user-content-downloaderrate" class="anchor" aria-hidden="true" href="#downloaderrate"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.*.rate</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Examples</td>
<td><code>"32000"</code>, <code>"500k"</code>, <code>"2.5M"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Maximum download rate in bytes per second.</p>
<p>Possible values are valid integer or floating-point numbers
optionally followed by one of <code>k</code>, <code>m</code>. <code>g</code>, <code>t</code> or <code>p</code>.
These suffixes are case-insensitive.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-retries"></a>
<h3><a id="user-content-downloaderretries" class="anchor" aria-hidden="true" href="#downloaderretries"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.*.retries</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>integer</code></td>
</tr>
<tr><td>Default</td>
<td><a href="#extractor-retries">extractor.*.retries</a></td>
</tr>
<tr><td>Description</td>
<td>Maximum number of retries during file downloads
or <code>-1</code> for infinite retries.</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-timeout"></a>
<h3><a id="user-content-downloadertimeout" class="anchor" aria-hidden="true" href="#downloadertimeout"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.*.timeout</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>float</code> or <code>null</code></td>
</tr>
<tr><td>Default</td>
<td><a href="#extractor-timeout">extractor.*.timeout</a></td>
</tr>
<tr><td>Description</td>
<td>Connection timeout during file downloads.</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-verify"></a>
<h3><a id="user-content-downloaderverify" class="anchor" aria-hidden="true" href="#downloaderverify"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.*.verify</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code> or <code>string</code></td>
</tr>
<tr><td>Default</td>
<td><a href="#extractor-verify">extractor.*.verify</a></td>
</tr>
<tr><td>Description</td>
<td>Certificate validation during file downloads.</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-ytdl-format"></a>
<h3><a id="user-content-downloaderytdlformat" class="anchor" aria-hidden="true" href="#downloaderytdlformat"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.ytdl.format</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td>youtube-dl's default, currently <code>"bestvideo+bestaudio/best"</code></td>
</tr>
<tr><td>Description</td>
<td>Video <a href="https://github.com/ytdl-org/youtube-dl#format-selection">format selection</a>
directly passed to youtube-dl.</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-ytdl-forward-cookies"></a>
<h3><a id="user-content-downloaderytdlforward-cookies" class="anchor" aria-hidden="true" href="#downloaderytdlforward-cookies"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.ytdl.forward-cookies</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Forward cookies to youtube-dl.</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-ytdl-logging"></a>
<h3><a id="user-content-downloaderytdllogging" class="anchor" aria-hidden="true" href="#downloaderytdllogging"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.ytdl.logging</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><div>
<div>Route youtube-dl's output through gallery-dl's logging system.</div>
<div>Otherwise youtube-dl will write its output directly to stdout/stderr.</div>
</div>
<p>Note: Set <code>quiet</code> and <code>no_warnings</code> in
<a href="#downloader-ytdl-raw-options">downloader.ytdl.raw-options</a> to <code>true</code> to suppress all output.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-downloader-ytdl-raw-options"></a>
<h3><a id="user-content-downloaderytdlraw-options" class="anchor" aria-hidden="true" href="#downloaderytdlraw-options"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>downloader.ytdl.raw-options</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>object</code></td>
</tr>
<tr><td>Example</td>
<td><pre lang="first">{
    "quiet": true,
    "writesubtitles": true,
    "merge_output_format": "mkv"
}
</pre>
</td>
</tr>
<tr><td>Description</td>
<td><div>
<div>Additional options passed directly to the <code>YoutubeDL</code> constructor.</div>
<div>All available options can be found in <a href="https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L138-L318">youtube-dl's docstrings</a>.</div>
</div>
</td>
</tr>
</tbody>
</table>
<a name="user-content-output-options"></a>
<h2><a id="user-content-output-options" class="anchor" aria-hidden="true" href="#output-options"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Output Options</h2>
<a name="user-content-output-mode"></a>
<h3><a id="user-content-outputmode" class="anchor" aria-hidden="true" href="#outputmode"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>output.mode</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"auto"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls the output string format and status indicators.</p>
<ul>
<li><code>"null"</code>: No output</li>
<li><code>"pipe"</code>: Suitable for piping to other processes or files</li>
<li><code>"terminal"</code>: Suitable for the standard Windows console</li>
<li><code>"color"</code>: Suitable for terminals that understand ANSI escape codes and colors</li>
<li><code>"auto"</code>: Automatically choose the best suitable output mode</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-output-shorten"></a>
<h3><a id="user-content-outputshorten" class="anchor" aria-hidden="true" href="#outputshorten"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>output.shorten</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Controls whether the output strings should be shortened to fit
on one console line.</td>
</tr>
</tbody>
</table>
<a name="user-content-output-progress"></a>
<h3><a id="user-content-outputprogress" class="anchor" aria-hidden="true" href="#outputprogress"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>output.progress</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code> or <code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls the progress indicator when <em>gallery-dl</em> is run with
multiple URLs as arguments.</p>
<ul>
<li><code>true</code>: Show the default progress indicator
(<code>"[{current}/{total}] {url}"</code>)</li>
<li><code>false</code>: Do not show any progress indicator</li>
<li>Any <code>string</code>: Show the progress indicator using this
as a custom <a href="https://docs.python.org/3/library/string.html#formatstrings" rel="nofollow">format string</a>. Possible replacement keys are
<code>current</code>, <code>total</code>  and <code>url</code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-output-log"></a>
<h3><a id="user-content-outputlog" class="anchor" aria-hidden="true" href="#outputlog"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>output.log</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code> or <a href="#logging-configuration"><code>Logging Configuration</code></a></td>
</tr>
<tr><td>Default</td>
<td><code>"[{name}][{levelname}] {message}"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Configuration for standard logging output to stderr.</p>
<p>If this is a simple <code>string</code>, it specifies
the format string for logging messages.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-output-logfile"></a>
<h3><a id="user-content-outputlogfile" class="anchor" aria-hidden="true" href="#outputlogfile"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>output.logfile</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><a href="#path"><code>Path</code></a> or <a href="#logging-configuration"><code>Logging Configuration</code></a></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td>File to write logging output to.</td>
</tr>
</tbody>
</table>
<a name="user-content-output-unsupportedfile"></a>
<h3><a id="user-content-outputunsupportedfile" class="anchor" aria-hidden="true" href="#outputunsupportedfile"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>output.unsupportedfile</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><a href="#path"><code>Path</code></a> or <a href="#logging-configuration"><code>Logging Configuration</code></a></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Description</td>
<td><p>File to write external URLs unsupported by <em>gallery-dl</em> to.</p>
<p>The default format string here is <code>"{message}"</code>.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-output-num-to-str"></a>
<h3><a id="user-content-outputnum-to-str" class="anchor" aria-hidden="true" href="#outputnum-to-str"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>output.num-to-str</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Convert numeric values (<code>integer</code> or <code>float</code>) to <code>string</code>
before outputting them as JSON.</td>
</tr>
</tbody>
</table>
<a name="user-content-postprocessor-options"></a>
<h2><a id="user-content-postprocessor-options" class="anchor" aria-hidden="true" href="#postprocessor-options"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Postprocessor Options</h2>
<a name="user-content-classify"></a>
<h3><a id="user-content-classify" class="anchor" aria-hidden="true" href="#classify"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>classify</h3>
<p>Categorize files by filename extension</p>
<a name="user-content-classify-mapping"></a>
<h3><a id="user-content-classifymapping" class="anchor" aria-hidden="true" href="#classifymapping"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>classify.mapping</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>object</code></td>
</tr>
<tr><td>Default</td>
<td><pre lang="first">{
    "Pictures" : ["jpg", "jpeg", "png", "gif", "bmp", "svg", "webp"],
    "Video"    : ["flv", "ogv", "avi", "mp4", "mpg", "mpeg", "3gp", "mkv", "webm", "vob", "wmv"],
    "Music"    : ["mp3", "aac", "flac", "ogg", "wma", "m4a", "wav"],
    "Archives" : ["zip", "rar", "7z", "tar", "gz", "bz2"]
}
</pre>
</td>
</tr>
<tr><td>Description</td>
<td><p>A mapping from directory names to filename extensions that should
be stored in them.</p>
<p>Files with an extension not listed will be ignored and stored
in their default location.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-exec"></a>
<h3><a id="user-content-exec" class="anchor" aria-hidden="true" href="#exec"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>exec</h3>
<p>Execute external commands.</p>
<a name="user-content-exec-async"></a>
<h3><a id="user-content-execasync" class="anchor" aria-hidden="true" href="#execasync"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>exec.async</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Controls whether to wait for a subprocess to finish
or to let it run asynchronously.</td>
</tr>
</tbody>
</table>
<a name="user-content-exec-command"></a>
<h3><a id="user-content-execcommand" class="anchor" aria-hidden="true" href="#execcommand"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>exec.command</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>list</code> of <code>strings</code></td>
</tr>
<tr><td>Example</td>
<td><code>["echo", "{user[account]}", "{id}"]</code></td>
</tr>
<tr><td>Description</td>
<td><p>The command to run.</p>
<p>Each element of this list is treated as a <a href="https://docs.python.org/3/library/string.html#formatstrings" rel="nofollow">format string</a> using
the files' metadata.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-metadata"></a>
<h3><a id="user-content-metadata" class="anchor" aria-hidden="true" href="#metadata"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>metadata</h3>
<p>Write image metadata to separate files</p>
<a name="user-content-metadata-mode"></a>
<h3><a id="user-content-metadatamode" class="anchor" aria-hidden="true" href="#metadatamode"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>metadata.mode</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"json"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Select how to write metadata.</p>
<ul>
<li><code>"json"</code>: all metadata using <a href="https://docs.python.org/3/library/json.html#json.dump" rel="nofollow">json.dump()</a></li>
<li><code>"tags"</code>: <code>tags</code> separated by newlines</li>
<li><code>"custom"</code>: result of applying <a href="#metadata-format">metadata.format</a> to a file's
metadata dictionary</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-metadata-extension"></a>
<h3><a id="user-content-metadataextension" class="anchor" aria-hidden="true" href="#metadataextension"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>metadata.extension</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"json"</code> or <code>"txt"</code></td>
</tr>
<tr><td>Description</td>
<td>Filename extension for metadata files.</td>
</tr>
</tbody>
</table>
<a name="user-content-metadata-format"></a>
<h3><a id="user-content-metadataformat" class="anchor" aria-hidden="true" href="#metadataformat"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>metadata.format</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Example</td>
<td><code>"tags:\n\n{tags:J\n}\n"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Custom format string to build content of metadata files.</p>
<p>Note: Only applies for <code>"mode": "custom"</code>.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-mtime"></a>
<h3><a id="user-content-mtime" class="anchor" aria-hidden="true" href="#mtime"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>mtime</h3>
<p>Set file modification time according to its metadata</p>
<a name="user-content-mtime-key"></a>
<h3><a id="user-content-mtimekey" class="anchor" aria-hidden="true" href="#mtimekey"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>mtime.key</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"date"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Name of the metadata field whose value should be used.</p>
<p>This value must either be a UNIX timestamp or a
<a href="https://docs.python.org/3/library/datetime.html#datetime-objects" rel="nofollow"><code>datetime</code></a> object.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-ugoira"></a>
<h3><a id="user-content-ugoira" class="anchor" aria-hidden="true" href="#ugoira"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ugoira</h3>
<p>Convert Pixiv Ugoira to WebM using <a href="https://www.ffmpeg.org/" rel="nofollow">FFmpeg</a>.</p>
<a name="user-content-ugoira-extension"></a>
<h3><a id="user-content-ugoiraextension" class="anchor" aria-hidden="true" href="#ugoiraextension"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ugoira.extension</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"webm"</code></td>
</tr>
<tr><td>Description</td>
<td>Filename extension for the resulting video files.</td>
</tr>
</tbody>
</table>
<a name="user-content-ugoira-ffmpeg-args"></a>
<h3><a id="user-content-ugoiraffmpeg-args" class="anchor" aria-hidden="true" href="#ugoiraffmpeg-args"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ugoira.ffmpeg-args</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>list</code> of <code>strings</code></td>
</tr>
<tr><td>Default</td>
<td><code>null</code></td>
</tr>
<tr><td>Example</td>
<td><code>["-c:v", "libvpx-vp9", "-an", "-b:v", "2M"]</code></td>
</tr>
<tr><td>Description</td>
<td>Additional FFmpeg command-line arguments.</td>
</tr>
</tbody>
</table>
<a name="user-content-ugoira-ffmpeg-location"></a>
<h3><a id="user-content-ugoiraffmpeg-location" class="anchor" aria-hidden="true" href="#ugoiraffmpeg-location"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ugoira.ffmpeg-location</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><a href="#path"><code>Path</code></a></td>
</tr>
<tr><td>Default</td>
<td><code>"ffmpeg"</code></td>
</tr>
<tr><td>Description</td>
<td>Location of the <code>ffmpeg</code> (or <code>avconv</code>) executable to use.</td>
</tr>
</tbody>
</table>
<a name="user-content-ugoira-ffmpeg-output"></a>
<h3><a id="user-content-ugoiraffmpeg-output" class="anchor" aria-hidden="true" href="#ugoiraffmpeg-output"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ugoira.ffmpeg-output</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td>Show FFmpeg output.</td>
</tr>
</tbody>
</table>
<a name="user-content-ugoira-ffmpeg-twopass"></a>
<h3><a id="user-content-ugoiraffmpeg-twopass" class="anchor" aria-hidden="true" href="#ugoiraffmpeg-twopass"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ugoira.ffmpeg-twopass</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Enable Two-Pass encoding.</td>
</tr>
</tbody>
</table>
<a name="user-content-ugoira-framerate"></a>
<h3><a id="user-content-ugoiraframerate" class="anchor" aria-hidden="true" href="#ugoiraframerate"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ugoira.framerate</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"auto"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Controls the frame rate argument (<code>-r</code>) for FFmpeg</p>
<ul>
<li><code>"auto"</code>: Automatically assign a fitting frame rate
based on delays between frames.</li>
<li>any other <code>string</code>:  Use this value as argument for <code>-r</code>.</li>
<li><code>null</code> or an empty <code>string</code>: Don't set an explicit frame rate.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-ugoira-keep-files"></a>
<h3><a id="user-content-ugoirakeep-files" class="anchor" aria-hidden="true" href="#ugoirakeep-files"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ugoira.keep-files</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Keep ZIP archives after conversion.</td>
</tr>
</tbody>
</table>
<a name="user-content-ugoira-libx264-prevent-odd"></a>
<h3><a id="user-content-ugoiralibx264-prevent-odd" class="anchor" aria-hidden="true" href="#ugoiralibx264-prevent-odd"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ugoira.libx264-prevent-odd</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><p>Prevent <code>"width/height not divisible by 2"</code> errors
when using <code>libx264</code> or <code>libx265</code> encoders
by applying a simple cropping filter. See this <a href="https://stackoverflow.com/questions/20847674" rel="nofollow">Stack Overflow
thread</a>
for more information.</p>
<p>This option, when <code>libx264/5</code> is used, automatically
adds <code>["-vf", "crop=iw-mod(iw\\,2):ih-mod(ih\\,2)"]</code>
to the list of FFmpeg command-line arguments
to reduce an odd width/height by 1 pixel and make them even.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-zip"></a>
<h3><a id="user-content-zip" class="anchor" aria-hidden="true" href="#zip"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>zip</h3>
<p>Store files in a ZIP archive.</p>
<a name="user-content-zip-compression"></a>
<h3><a id="user-content-zipcompression" class="anchor" aria-hidden="true" href="#zipcompression"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>zip.compression</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"store"</code></td>
</tr>
<tr><td>Description</td>
<td><p>Compression method to use when writing the archive.</p>
<p>Possible values are <code>"store"</code>, <code>"zip"</code>, <code>"bzip2"</code>, <code>"lzma"</code>.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-zip-extension"></a>
<h3><a id="user-content-zipextension" class="anchor" aria-hidden="true" href="#zipextension"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>zip.extension</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"zip"</code></td>
</tr>
<tr><td>Description</td>
<td>Filename extension for the created ZIP archive.</td>
</tr>
</tbody>
</table>
<a name="user-content-zip-keep-files"></a>
<h3><a id="user-content-zipkeep-files" class="anchor" aria-hidden="true" href="#zipkeep-files"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>zip.keep-files</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code></td>
</tr>
<tr><td>Default</td>
<td><code>false</code></td>
</tr>
<tr><td>Description</td>
<td>Keep the actual files after writing them to a ZIP archive.</td>
</tr>
</tbody>
</table>
<a name="user-content-zip-mode"></a>
<h3><a id="user-content-zipmode" class="anchor" aria-hidden="true" href="#zipmode"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>zip.mode</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>"default"</code></td>
</tr>
<tr><td>Description</td>
<td><ul>
<li><p><code>"default"</code>: Write the central directory file header
once after everything is done or an exception is raised.</p>
</li>
<li><p><code>"safe"</code>: Update the central directory file header
each time a file is stored in a ZIP archive.</p>
<p>This greatly reduces the chance a ZIP archive gets corrupted in
case the Python interpreter gets shut down unexpectedly
(power outage, SIGKILL) but is also a lot slower.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-miscellaneous-options"></a>
<h2><a id="user-content-miscellaneous-options" class="anchor" aria-hidden="true" href="#miscellaneous-options"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Miscellaneous Options</h2>
<a name="user-content-cache-file"></a>
<h3><a id="user-content-cachefile" class="anchor" aria-hidden="true" href="#cachefile"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>cache.file</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><a href="#path"><code>Path</code></a></td>
</tr>
<tr><td>Default</td>
<td><ul>
<li><a href="https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir" rel="nofollow"><code>tempfile.gettempdir()</code></a> + <code>".gallery-dl.cache"</code> on Windows</li>
<li>(<code>$XDG_CACHE_HOME</code> or <code>"~/.cache"</code>) + <code>"/gallery-dl/cache.sqlite3"</code> on all other platforms</li>
</ul>
</td>
</tr>
<tr><td>Description</td>
<td><p>Path of the SQLite3 database used to cache login sessions,
cookies and API tokens across gallery-dl invocations.</p>
<p>Set this option to <code>null</code> or an invalid path to disable
this cache.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-ciphers"></a>
<h3><a id="user-content-ciphers" class="anchor" aria-hidden="true" href="#ciphers"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>ciphers</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>bool</code> or <code>string</code></td>
</tr>
<tr><td>Default</td>
<td><code>true</code></td>
</tr>
<tr><td>Description</td>
<td><ul>
<li><code>true</code>: Update urllib3's default cipher list</li>
<li><code>false</code>: Leave the default cipher list as is</li>
<li>Any <code>string</code>: Replace urllib3's default ciphers with these
(See <a href="https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ciphers" rel="nofollow">SSLContext.set_ciphers()</a>
for details)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-api-tokens-ids"></a>
<h2><a id="user-content-api-tokens--ids" class="anchor" aria-hidden="true" href="#api-tokens--ids"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>API Tokens &amp; IDs</h2>
<p>All configuration keys listed in this section have fully functional default
values embedded into <em>gallery-dl</em> itself, but if things unexpectedly break
or you want to use your own personal client credentials, you can follow these
instructions to get an alternative set of API tokens and IDs.</p>
<a name="user-content-extractor-deviantart-client-id-client-secret"></a>
<h3><a id="user-content-extractordeviantartclient-id--client-secret" class="anchor" aria-hidden="true" href="#extractordeviantartclient-id--client-secret"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.deviantart.client-id &amp; .client-secret</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>How To</td>
<td><ul>
<li>login and visit DeviantArt's
<a href="https://www.deviantart.com/developers/apps" rel="nofollow">Applications &amp; Keys</a>
section</li>
<li>click "Register your Application"</li>
<li>scroll to "OAuth2 Redirect URI Whitelist (Required)"
and enter "<a href="https://mikf.github.io/gallery-dl/oauth-redirect.html" rel="nofollow">https://mikf.github.io/gallery-dl/oauth-redirect.html</a>"</li>
<li>click "Save" (top right)</li>
<li>copy <code>client_id</code> and <code>client_secret</code> of your new
application and put them in your configuration file</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-flickr-api-key-api-secret"></a>
<h3><a id="user-content-extractorflickrapi-key--api-secret" class="anchor" aria-hidden="true" href="#extractorflickrapi-key--api-secret"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.flickr.api-key &amp; .api-secret</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>How To</td>
<td><ul>
<li>login and <a href="https://www.flickr.com/services/apps/create/apply/" rel="nofollow">Create an App</a>
in Flickr's <a href="https://www.flickr.com/services/" rel="nofollow">App Garden</a></li>
<li>click "APPLY FOR A NON-COMMERCIAL KEY"</li>
<li>fill out the form with a random name and description
and click "SUBMIT"</li>
<li>copy <code>Key</code> and <code>Secret</code> and put them in your configuration
file</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-pawoo-access-token"></a>
<h3><a id="user-content-extractorpawooaccess-token" class="anchor" aria-hidden="true" href="#extractorpawooaccess-token"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.pawoo.access-token</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>How To</td>
<td> </td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-reddit-client-id-user-agent"></a>
<h3><a id="user-content-extractorredditclient-id--user-agent" class="anchor" aria-hidden="true" href="#extractorredditclient-id--user-agent"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.reddit.client-id &amp; .user-agent</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>How To</td>
<td><ul>
<li>login and visit the <a href="https://www.reddit.com/prefs/apps/" rel="nofollow">apps</a>
section of your account's preferences</li>
<li>click the "are you a developer? create an app..." button</li>
<li>fill out the form, choose "installed app", preferably set
"<a href="http://localhost:6414/" rel="nofollow">http://localhost:6414/</a>" as "redirect uri" and finally click
"create app"</li>
<li>copy the client id (third line, under your application's name and
"installed app") and put it in your configuration file</li>
<li>use "<code>Python:&lt;application name&gt;:v1.0 (by /u/&lt;username&gt;)</code>" as
user-agent and replace <code>&lt;application name&gt;</code> and <code>&lt;username&gt;</code>
accordingly (see Reddit's
<a href="https://github.com/reddit/reddit/wiki/API">API access rules</a>)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-smugmug-api-key-api-secret"></a>
<h3><a id="user-content-extractorsmugmugapi-key--api-secret" class="anchor" aria-hidden="true" href="#extractorsmugmugapi-key--api-secret"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.smugmug.api-key &amp; .api-secret</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>How To</td>
<td><ul>
<li>login and <a href="https://api.smugmug.com/api/developer/apply" rel="nofollow">Apply for an API Key</a></li>
<li>use a random name and description,
set "Type" to "Application", "Platform" to "All",
and "Use" to "Non-Commercial"</li>
<li>fill out the two checkboxes at the bottom and click "Apply"</li>
<li>copy <code>API Key</code> and <code>API Secret</code>
and put them in your configuration file</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-extractor-tumblr-api-key-api-secret"></a>
<h3><a id="user-content-extractortumblrapi-key--api-secret" class="anchor" aria-hidden="true" href="#extractortumblrapi-key--api-secret"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>extractor.tumblr.api-key &amp; .api-secret</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code></td>
</tr>
<tr><td>How To</td>
<td><ul>
<li>login and visit Tumblr's
<a href="https://www.tumblr.com/oauth/apps" rel="nofollow">Applications</a> section</li>
<li>click "Register application"</li>
<li>fill out the form: use a random name and description, set
<a href="https://example.org/" rel="nofollow">https://example.org/</a> as "Application Website" and "Default
callback URL"</li>
<li>solve Google's "I'm not a robot" challenge and click "Register"</li>
<li>click "Show secret key" (below "OAuth Consumer Key")</li>
<li>copy your <code>OAuth Consumer Key</code> and <code>Secret Key</code>
and put them in your configuration file</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-custom-types"></a>
<h2><a id="user-content-custom-types" class="anchor" aria-hidden="true" href="#custom-types"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Custom Types</h2>
<a name="user-content-date"></a>
<h3><a id="user-content-date" class="anchor" aria-hidden="true" href="#date"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Date</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code> or <code>integer</code></td>
</tr>
<tr><td>Examples</td>
<td><ul>
<li><code>"2019-01-01T00:00:00"</code></li>
<li><code>"2019"</code> with <code>"%Y"</code> as <a href="#extractor-date-format">date-format</a></li>
<li><code>1546297200</code></li>
</ul>
</td>
</tr>
<tr><td>Description</td>
<td><p>A <a href="#date"><code>Date</code></a> value represents a specific point in time.</p>
<ul>
<li>If given as <code>string</code>, it is parsed according to <a href="#extractor-date-format">date-format</a>.</li>
<li>If given as <code>integer</code>, it is interpreted as UTC timestamp.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<a name="user-content-path"></a>
<h3><a id="user-content-path" class="anchor" aria-hidden="true" href="#path"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Path</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>string</code> or <code>list</code> of <code>strings</code></td>
</tr>
<tr><td>Examples</td>
<td><ul>
<li><code>"file.ext"</code></li>
<li><code>"~/path/to/file.ext"</code></li>
<li><code>"$HOME/path/to/file.ext"</code></li>
<li><code>["$HOME", "path", "to", "file.ext"]</code></li>
</ul>
</td>
</tr>
<tr><td>Description</td>
<td><p>A <a href="#path"><code>Path</code></a> is a <code>string</code> representing the location of a file
or directory.</p>
<p>Simple <a href="https://docs.python.org/3/library/os.path.html#os.path.expanduser" rel="nofollow">tilde expansion</a>
and <a href="https://docs.python.org/3/library/os.path.html#os.path.expandvars" rel="nofollow">environment variable expansion</a>
is supported.</p>
<p>In Windows environments, backslashes (<code>"\"</code>) can, in addition to
forward slashes (<code>"/"</code>), be used as path separators.
Because backslashes are JSON's escape character,
they themselves have to be escaped.
The path <code>C:\path\to\file.ext</code> has therefore to be written as
<code>"C:\\path\\to\\file.ext"</code> if you want to use backslashes.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-logging-configuration"></a>
<h3><a id="user-content-logging-configuration" class="anchor" aria-hidden="true" href="#logging-configuration"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Logging Configuration</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>object</code></td>
</tr>
<tr><td>Examples</td>
<td><pre lang="first">{
    "format": "{asctime} {name}: {message}",
    "format-date": "%H:%M:%S",
    "path": "~/log.txt",
    "encoding": "ascii"
}

{
    "level": "debug",
    "format": {
        "debug"  : "debug: {message}",
        "info"   : "[{name}] {message}",
        "warning": "Warning: {message}",
        "error"  : "ERROR: {message}"
    }
}
</pre>
</td>
</tr>
<tr><td>Description</td>
<td><p>Extended logging output configuration.</p>
<ul>
<li><dl>
<dt>format</dt>
<dd><ul>
<li><p>General format string for logging messages
or a dictionary with format strings for each loglevel.</p>
<p>In addition to the default
<a href="https://docs.python.org/3/library/logging.html#logrecord-attributes" rel="nofollow">LogRecord attributes</a>,
it is also possible to access the current
<a href="https://github.com/mikf/gallery-dl/blob/2e516a1e3e09cb8a9e36a8f6f7e41ce8d4402f5a/gallery_dl/extractor/common.py#L24">extractor</a>
and <a href="https://github.com/mikf/gallery-dl/blob/2e516a1e3e09cb8a9e36a8f6f7e41ce8d4402f5a/gallery_dl/job.py#L19">job</a>
objects as well as their attributes
(e.g. <code>"{extractor.url}"</code>)</p>
</li>
<li><p>Default: <code>"[{name}][{levelname}] {message}"</code></p>
</li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>format-date</dt>
<dd><ul>
<li>Format string for <code>{asctime}</code> fields in logging messages
(see <a href="https://docs.python.org/3/library/time.html#time.strftime" rel="nofollow">strftime() directives</a>)</li>
<li>Default: <code>"%Y-%m-%d %H:%M:%S"</code></li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>level</dt>
<dd><ul>
<li>Minimum logging message level
(one of <code>"debug"</code>, <code>"info"</code>, <code>"warning"</code>, <code>"error"</code>, <code>"exception"</code>)</li>
<li>Default: <code>"info"</code></li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>path</dt>
<dd><ul>
<li><a href="#path"><code>Path</code></a> to the output file</li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>mode</dt>
<dd><ul>
<li>Mode in which the file is opened;
use <code>"w"</code> to truncate or <code>"a"</code> to append
(see <a href="https://docs.python.org/3/library/functions.html#open" rel="nofollow">open()</a>)</li>
<li>Default: <code>"w"</code></li>
</ul>
</dd>
</dl>
</li>
<li><dl>
<dt>encoding</dt>
<dd><ul>
<li>File encoding</li>
<li>Default: <code>"utf-8"</code></li>
</ul>
</dd>
</dl>
</li>
</ul>
<p>Note: path, mode and encoding are only applied when configuring
logging output to a file.</p>
</td>
</tr>
</tbody>
</table>
<a name="user-content-postprocessor-configuration"></a>
<h3><a id="user-content-postprocessor-configuration" class="anchor" aria-hidden="true" href="#postprocessor-configuration"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Postprocessor Configuration</h3>
<table>




<tbody valign="top">
<tr><td>Type</td>
<td><code>object</code></td>
</tr>
<tr><td>Example</td>
<td><pre lang="first">{
    "name": "zip",
    "compression": "store",
    "extension": "cbz",
    "whitelist": ["mangadex", "exhentai", "nhentai"]
}
</pre>
</td>
</tr>
<tr><td>Description</td>
<td><p>An object with the <code>name</code> of a post-processor and its options.</p>
<p>See <a href="#postprocessor-options">Postprocessor Options</a> for a list of all available
post-processors and their respective options.</p>
<p>You can also set a <code>whitelist</code> or <code>blacklist</code> to
only enable or disable a post-processor for the specified
extractor categories.</p>
</td>
</tr>
</tbody>
</table>

</article>
  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>



  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">&copy; 2019 <span title="0.27130s from unicorn-55554bfd8b-95lvh">GitHub</span>, Inc.</li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-BlCvumXWTvpASEdhCGiahDUDf7Bwb8QXA2XnnSnqJ9QafxcNcrNYUNYS2wXmd3nEpO//+zlZa9DSV9zmu5MqRg==" type="application/javascript" src="https://github.githubassets.com/assets/compat-bootstrap-90c0ace0.js"></script>
    <script crossorigin="anonymous" integrity="sha512-wnzuXnJOv44OjFcu212AzXLSnG/ZC2w+604e2QGofkYgeMWZYQfHPb6NeH6194cJ8HvT0UEsmHzlCSXPVHcg6w==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-069938ed.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-/Y1wpl1aY/vedgylTJDuNAeobNLd980HlatSO7pdREx2e+kh4ijbkH0T8qp/+sJPD4FOBcodJ2AyDATrXVdVKA==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-d62e19fe.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

