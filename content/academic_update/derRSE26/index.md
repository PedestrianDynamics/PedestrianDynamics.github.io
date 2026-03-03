---
title: "derRSE 2026"
date: 2026-03-03
---

The sixth German Conference on Research Software Engineering ([**derRSE26**](https://events.hifis.net/event/2945/)) will be held at the University of Stuttgart from March 3rd to 5th, 2026.

## Talk

**JuPedSim: From Obscure Executables to a Publicly Documented Library**

**Speaker:** Mr Kai Kratz

JuPedSim is an open-source framework for simulating how pedestrians move through buildings, public spaces, and city environments. For years, it was one of those research tools that "just worked" — if you knew how to use it. The software has been part of the pedestrian dynamics community for over 15 years, supporting research and practice from evacuation planning to urban mobility studies.

By 2020, though, JuPedSim had grown into a collection of hard-to-maintain executables driven by complex XML files: powerful, but opaque, and increasingly inaccessible to new users. At some point, we realized we couldn't keep patching it forever. We needed to rethink what JuPedSim was for and who it was for. That's where the real RSE story begins.

We set out to reshape JuPedSim into a modern, community-oriented library — and learned a lot along the way. The transformation was not primarily a technical one; it was a story about stakeholders, sustainability, and focus.

We rebuilt JuPedSim as a Python module with a modular C++ core, but the key change was philosophical: API over configuration, explicit over implicit. Instead of hiding behavior behind large configuration files, we encourage users to express their ideas directly in code. It's not about convenience; it's about clarity and reproducibility. We want people to understand what their simulation does, not just run it. This shift changed how the community interacts with the tool — making experiments more reproducible, the codebase more maintainable, and the system easier to teach and extend.

This journey wasn't purely technical, it required full stakeholder commitment. None of this would have happened without support from domain scientists, developers, and institutions. Gaining that trust meant learning to communicate in their terms: why change was necessary, what would be gained, and how it would affect their work. Along the way, we faced the classic second-system problem — the temptation to rebuild everything, and learned that doing less was often better. We focused on the essentials, dropped non-core tools like JpsEditor, and spun out independent, focused projects such as PedPy, a Python analysis library that became a success in its own right.

Finally, we'll reflect on governance, documentation, and long-term sustainability: how to keep a research software project alive beyond funding cycles and how to turn a codebase into a community.

This talk isn't about code or performance. It's about what it takes to turn a long-running research codebase into something sustainable — building trust, reducing complexity, and creating space for others to contribute.

In short: how we learned to do less, but better.

**Keywords:** pedestrian dynamics, research software engineering, sustainability, governance, community building, Python/C++ hybrid, documentation.

## Download

[Download the talk (PDF)](derRSE26.pdf)
[JuPedSim Website](https://jupedsim.org)
