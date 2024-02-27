---
layout: post
title: Nerdlight - Making Light Out Of Leftovers
permalink: nerdlight.html
thumbnail: /images/thumbnails/nerdlight.jpg
---

I made a thing! A blinky thing.<!-- more -->I found a little baggie containing four
[Adafruit through-hole NeoPixels](https://www.adafruit.com/product/1734) in my tool
bag. They're big, fat, addressable RGB LEDs. I need some more blinky lights in my life - I think
I've been watching too many
[YouTube videos from Big Clive](https://www.youtube.com/watch?v=VDFNA97mS58) - so I made up a
little lightbox thing to put them in. I don't have my full shop here in the new apartment, just
a bag of tools I brought and various household materials, so the hack factor is high. I think it
looks nice, though.

The four LEDs are mounted into a bit of plastic cut from an old hotel room key. I should have taken
a photo of the back - the 5V and ground lines are tied together by bending the legs together and
soldering, and the data ins and outs are chained together. Here's the front, though.

![Mounting for NeoPixels](/images/nerdlight1.jpg)

There's also a little 1N4001 diode visible there - I'm using that to drop the input voltage to the
Neopixels down to three-ish volts, so I can talk to them without a level shifter. I'm powering
them from the +5V rail on the Pi - there's only four pixels, so it should be okay, current-wise.

I'm using a rectangular section cut out of a [Moo](https://www.moo.com/) card box as the enclosure! Why
not. I also made an insert from a business card to act as a divider between the four lights. That
way you get four distinct colors, without mixing.

![Enclosure and light divider](/images/nerdlight2.jpg)

As a diffuser, I'm using a bit of milky plastic cut from&hellip; a milk carton. Recycling!
To hide the cut edges, I snipped some segments from black zip-ties and glued them to the front to
make a bezel and dividers. It looks pretty okay, considering. Another section cut from the box acts
as a kickstand, tilting the lights up to the viewer.

![Diffuser and bezel](/images/nerdlight3.jpg)

I followed Adafruit's
[NeoPixels on Raspberry Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi/)
tutorial to set up the required software goodies. All pretty easy peasy.

And here's how it looks running! The colors are super nice and saturated, more so than they
come through in the video.
<blockquote class="instagram-media" data-instgrm-version="6" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50.0% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAAGFBMVEUiIiI9PT0eHh4gIB4hIBkcHBwcHBwcHBydr+JQAAAACHRSTlMABA4YHyQsM5jtaMwAAADfSURBVDjL7ZVBEgMhCAQBAf//42xcNbpAqakcM0ftUmFAAIBE81IqBJdS3lS6zs3bIpB9WED3YYXFPmHRfT8sgyrCP1x8uEUxLMzNWElFOYCV6mHWWwMzdPEKHlhLw7NWJqkHc4uIZphavDzA2JPzUDsBZziNae2S6owH8xPmX8G7zzgKEOPUoYHvGz1TBCxMkd3kwNVbU0gKHkx+iZILf77IofhrY1nYFnB/lQPb79drWOyJVa/DAvg9B/rLB4cC+Nqgdz/TvBbBnr6GBReqn/nRmDgaQEej7WhonozjF+Y2I/fZou/qAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/BFMx85DLIWL/" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A video posted by John Riney (@rin3y)</a> on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2016-05-09T20:20:35+00:00">May 9, 2016 at 1:20pm PDT</time></p></div></blockquote>
<script async defer src="//platform.instagram.com/en_US/embeds.js"></script>
<br>
So, yeah, not bad for a few minutes work, using minimal tools. _Ooh, pretty lights._
