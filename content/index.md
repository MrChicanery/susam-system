---
title: "All Pages"
description: "Browse every page in the content directory"
---

# 🗂️ All Pages

Browse all available content pages:

<ClientOnly>
  <ContentList path="/" :exclude="['/index']" v-slot="{ list }">
    <ul class="list-disc pl-4">
      <li v-for="item in list" :key="item._path">
        <NuxtLink :to="item._path" class="text-blue-600 hover:underline">
          {{ item.title || item._path }}
        </NuxtLink>
      </li>
    </ul>
  </ContentList>
</ClientOnly>
