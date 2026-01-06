You can use **ChatGPT’s built-in Connectors** (no coding):

- in the ChatGPT app or web interface, go to _Settings → Connectors_, connect your **Google Calendar** (and Gmail if you want additional context)
- Grant permission

Once connected, you can ask questions like “What’s on my calendar today?” or “Do I have any conflicts tomorrow?” directly in chat.

> [!note]
> I had to have a few goes at this and do a re-connection for it work properly.

## But what about secondary calendars?

I wanted to look through a secondary "planning" calendar i have. But that did not work at all ❌😬

- Seems that that on my google workspace the calendar is not being shared via the API somehow (??)
- 🎉 The hacky workaround was to share the secret ics link
- BUT that only worked in Gemini
    - In ChatGPT it still could not access. It claimed (who knows if true) "The environment I’m running in does not allow arbitrary binary/text file downloads from Google endpoints, even when they are public or secret URLs."

### ChatGPT: 😞 Can't filter by calendar

So for my use case it didn't work.

I wanted to pull and review just the events from a specific calendar "Rufus planning".

But ... the current integration exposes events without exposing the underlying calendar IDs, so those events can’t be isolated by calendar name.

> [!warning]
> 
> I actually think the bigger issue was that chatgpt could *not* even access that calendar (see below). The above was chatgpt's analysis which i think turned out to be wrong with further digging.

### Both Gemini and ChatGPT incorrectly claimed that we had found a workaround

Gemini claimted it had found this workaround for accessing the calendar ... BUT it did NOT work 🤦‍♂️

> The Issue
> 
> By default, Gemini's calendar integration often only "sees" your Primary calendar (the one associated with your main email address). Even if you own secondary calendars—like a "Planning" or "Team" calendar—they may not appear in the AI's list of accessible tools, even if they are visible in your browser.
> 
> The Solution: Direct Calendar ID Mapping
> 
> To bypass this "Primary-only" limitation, you can force a connection by providing the unique Calendar ID.
> 
> 1. **Locate the ID**: In Google Calendar desktop, go to the secondary calendar's **Settings and sharing**.
>     
> 2. **Copy the String**: Scroll to **Integrate calendar** and copy the **Calendar ID** (e.g., `longstring@group.calendar.google.com`).
>     
> 3. **Paste into Chat**: Provide this ID directly to Gemini. This allows the API to "ping" the specific calendar directly, bypassing the standard list.

#### ChatGPT claimed the workaround worked but it didn't

What also became clearer was that neither Gemini not ChatGPT could access this **"secondary"** calendar. i actually think that was the main issue.

> Yes — providing the calendar ID _does_ resolve this. The limitation wasn’t access to the events themselves, but lack of visibility of calendar metadata (specifically calendar IDs) in the default integration. With the explicit calendar ID (`artearthtech.com_r63nmilujsalhfgcq2bj2j3vmc@group.calendar.google.com`), events can be queried directly from that calendar and cleanly isolated.

And then after trying it ...

> I tried, but **I still can’t execute a calendar-ID–scoped query** with this connector.
> 
> ...
> 
> there is **no callable operation exposed to me that can fetch events scoped to that calendar**. I can only retrieve events from the merged view of all accessible calendars, without a way to say “only this calendar,” and without calendar IDs attached to returned events.
