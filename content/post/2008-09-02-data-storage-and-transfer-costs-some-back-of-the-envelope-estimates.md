---
title: >-
  Data Storage and Transfer Costs: Some Back of the Envelope Estimates
slug: data-storage-and-transfer-costs-some-back-of-the-envelope-estimates
date: 2008-09-02T11:29:37
themes: [u'Notebook']
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 341
---

For large data centres a big industry player estimated costs of Â£22 / GB / Month = Â£250k / TB / Year. Majority of this was hardware and energy costs (not costs of human sysadmins). This seems quite a lot. However, Amazon S3 quote for Europe (cheaper for US):

    Storage
    $0.18 per GB-Month of storage used

    Data Transfer
    $0.100 per GB - all data transfer in

    $0.170 per GB - first 10 TB / month data transfer out
    $0.130 per GB - next 40 TB / month data transfer out
    $0.110 per GB - next 100 TB / month data transfer out
    $0.100 per GB - data transfer out / month over 150 TB

    Requests
    $0.012 per 1,000 PUT, POST, or LIST requests
    $0.012 per 10,000 GET and all other requests*
    * No charge for delete requests

Subtracting say Â£2 for costs of storage and transfer leaves Â£20 per GB Month = $40 / GBM. On Amazon's figures this is around 235 GB of transfer (0.235 TB). A ratio of 235 to 1 on the underlying data. Not necessarily an infeasible level (235 users / byte / month). This also demonstrates that b/w costs will dwarf storage costs in most cases.

