---
title: "Schools"
description: "Browse all schools"
---

# 🏫 Schools Index

Browse all available schools:

<ClientOnly>
  <ContentQuery path="/schools" :exclude="['/schools/index']" v-slot="{ data }">
    <ul class="list-disc pl-5">
      <li v-for="item in data" :key="item._path">
        <NuxtLink :to="item._path" class="text-blue-600 hover:underline">
          {{ item.title || item._path.replace('/schools/', '') }}
        </NuxtLink>
      </li>
    </ul>
  </ContentQuery>
</ClientOnly>

