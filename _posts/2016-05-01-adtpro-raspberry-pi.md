---
layout: post
title: Raspberry Pi File Server For Apple II
date: 2016-05-01
permalink: pi-apple-ii.html
thumbnail: /images/thumbnails/disk.png
---

I've been spending a little time with my Apple IIc - possibly the cutest computer Apple has ever
released.<!-- more --> Look at that little monitor!

<blockquote class="instagram-media" data-instgrm-version="6" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50.0% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAAGFBMVEUiIiI9PT0eHh4gIB4hIBkcHBwcHBwcHBydr+JQAAAACHRSTlMABA4YHyQsM5jtaMwAAADfSURBVDjL7ZVBEgMhCAQBAf//42xcNbpAqakcM0ftUmFAAIBE81IqBJdS3lS6zs3bIpB9WED3YYXFPmHRfT8sgyrCP1x8uEUxLMzNWElFOYCV6mHWWwMzdPEKHlhLw7NWJqkHc4uIZphavDzA2JPzUDsBZziNae2S6owH8xPmX8G7zzgKEOPUoYHvGz1TBCxMkd3kwNVbU0gKHkx+iZILf77IofhrY1nYFnB/lQPb79drWOyJVa/DAvg9B/rLB4cC+Nqgdz/TvBbBnr6GBReqn/nRmDgaQEej7WhonozjF+Y2I/fZou/qAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/BBvIQEYrIYW/" style="color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;">A video posted by John Riney (@rin3y)</a> on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2016-02-13T18:24:03+00:00">Feb 13, 2016 at 10:24am PST</time></p></div></blockquote>
<script async defer src="//platform.instagram.com/en_US/embeds.js"></script>
<br>
<p>It works, as far as I can tell, perfectly. The question becomes, then, how do you get software into
a machine that only accepts these:</p>

![floppy disk](/images/floppy.jpg)

Turns out this is a cleanly solved problem. [ADTPro](http://adtpro.sourceforge.net/) is a super-slick
utility to transfer files to the Apple family. It can use the cassette ports or Ethernet connections
on Apples that have them, but in my case, I'm making use of the IIc's built in serial ports. So the
setup looks like

> #### [Computer] -> [USB serial adapter] -> [9-pin serial to 5-pin DIN adapter] -> [Apple]

Finding a USB serial adapter that works worth a crap is a bit tricky; after trying a few from
Fry's, I found one with a Moschip 7840 chipset that is dodgy under OSX but pretty stable under
Linux. Adapting from a regular 9-pin serial plug to the Apple's serial port is just a bit of
soldering _(and, on a side tangent, wow, did computer manufacturers in the 80s have a love affair
with DIN plugs. Frequently weird, hard-to-find ones &mdash - although fortunately, the Apple serial
port is just a regular 5-pin.)_

So this works all well and good, except that I've got to drag my laptop over to the Apple whenever
I want to copy disks around. That's not lazy enough by far. Wait, don't I have a Raspberry Pi
laying around not doing anything? Ah! Perfect! So we still use ADTPro and the USB serial adapter,
but we run them on the Pi, which we can just leave running all the time behind the Apple. I've got a
16 gig SD card plugged in, so there's a ton of storage. Also, I've got a little USB hub on there,
both to add more ports if I need a keyboard and mouse for debugging, and also because my Pi tends
to spaz out if you unplug something&hellip; The whole rig looks like this:

![Raspberry Pi file server for my IIc](https://instagram.fsnc1-1.fna.fbcdn.net/t51.2885-15/e35/13092223_820917534709904_333915038_n.jpg)

This ended up being a pretty plug-and-play affair;
I used the lite version of [Raspbian](https://www.raspberrypi.org/downloads/raspbian/), although
I ended up needing X11 on it as well, so you might as well use the full version. ADTPro runs on
Java, so you'll need that - I used Oracle's JDK, which is installable from apt-get. The only
slightly twitchy thing in the setup was having to modify ADTPro's startup script to use the Raspberry
Pi version of the RXTX serial drivers for Java - the script looks for them in the wrong place.

From there, it was a matter of making a quick init script to boot ADT when the Pi starts - it has
a convenient headless mode to let it run as a service, although I discovered you need a full X11
setup running for this to work.

The packages I remember having to install were as follows (might not be a comprehensive list):

{% highlight text %}
oracle-java8-jdk
librxtx-java
xinit
xserver-xorg
xvfb
lightdm
samba
samba-common-bin
{% endhighlight %}

Oh yeah, I put a Samba share on there too, so I can drag and drop files from my main PC onto the Pi.
Maximum laziness activated! This isn't a particularly original setup, but it works so cleanly,
I thought it was worth writing up. So with this setup, along with the amazing
[Bmp2DHR](http://www.appleoldies.ca/bmp2dhr/)
and [AppleCommander](http://applecommander.sourceforge.net/) utilities, I can put pictures of my cat
onto floppy disk, and therefore onto the Apple's little monochrome screen - and isn't that what
technology is really all about? *Don't answer that.*

<blockquote class="instagram-media" data-instgrm-version="6" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50.0% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAAGFBMVEUiIiI9PT0eHh4gIB4hIBkcHBwcHBwcHBydr+JQAAAACHRSTlMABA4YHyQsM5jtaMwAAADfSURBVDjL7ZVBEgMhCAQBAf//42xcNbpAqakcM0ftUmFAAIBE81IqBJdS3lS6zs3bIpB9WED3YYXFPmHRfT8sgyrCP1x8uEUxLMzNWElFOYCV6mHWWwMzdPEKHlhLw7NWJqkHc4uIZphavDzA2JPzUDsBZziNae2S6owH8xPmX8G7zzgKEOPUoYHvGz1TBCxMkd3kwNVbU0gKHkx+iZILf77IofhrY1nYFnB/lQPb79drWOyJVa/DAvg9B/rLB4cC+Nqgdz/TvBbBnr6GBReqn/nRmDgaQEej7WhonozjF+Y2I/fZou/qAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/BE5SkUSLITI/" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;">A video posted by John Riney (@rin3y)</a> on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2016-05-02T06:40:47+00:00">May 1, 2016 at 11:40pm PDT</time></p></div></blockquote>
<script async defer src="//platform.instagram.com/en_US/embeds.js"></script>
