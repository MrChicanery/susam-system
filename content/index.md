---
title: Home Page
description: Explore degrees, courses, and academic programs across the State University System of America.
---

<div class="flex flex-col min-h-screen">
  <header class="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
    <div class="container flex h-14 max-w-screen-2xl items-center justify-between">
      <div class="flex items-center gap-6">
        <a href="/" class="flex items-center space-x-2">
          <span class="font-bold inline-block">SUSAM</span>
        </a>
        <nav class="hidden md:flex gap-6">
          <a href="/schools" class="text-sm font-medium hover:text-foreground/80">Schools</a>
          <a href="/courses" class="text-sm font-medium hover:text-foreground/80">Courses</a>
          <a href="/admissions" class="text-sm font-medium hover:text-foreground/80">Admissions</a>
        </nav>
      </div>
      <div class="flex items-center gap-4">
        <button class="inline-flex items-center justify-center rounded-md text-sm font-medium hover:bg-accent hover:text-accent-foreground h-9 w-9">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-sun"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>
        </button>
      </div>
    </div>
  </header>

  <div class="container max-w-screen-2xl flex-1">
    <div class="flex flex-col items-center justify-center space-y-8 text-center py-12 md:py-24">
      <div class="space-y-4 max-w-3xl">
        <h1 class="font-heading text-4xl md:text-6xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-gray-900 to-gray-600 dark:from-gray-100 dark:to-gray-400">
          Your Academic Journey 
          <span class="block text-gradient-to-r from-blue-600 to-indigo-600">Starts Here</span>
        </h1>
        <p class="text-xl text-muted-foreground">
          Access comprehensive course information, program details, and academic resources across our university system.
        </p>
      </div>
    </div>

    ::card-group{cols=3}
      ::card{icon="lucide:book" title="Schools & Colleges" to="/schools"}
      Explore our diverse network of academic institutions and find your perfect fit.
      ::

      ::card{icon="lucide:library" title="Course Catalog" to="/courses"}
      Browse our comprehensive collection of courses across all disciplines.
      ::

      ::card{icon="lucide:graduation-cap" title="Admissions" to="/admissions"}
      Learn about getting admitted to the University system.
      ::
    ::