## Gatsby Notes

  - Instead of googling au hasard, if you need to get the current path
    of the component, file, etc., simply import `import { globalHistory  } from
    "@reach/router"` at the top of the page, and then use
    `globalHistory.location.pathname` to get the name. Christ is that harder
    than I wanted.
