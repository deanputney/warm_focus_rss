# Warm Focus radio show podcast RSS script

This script collects information about the Warm Focus show from its website and transforms it into a podcast RSS feed.

AI Instructions:

1. Write and test code to complete the task described below.
2. When you have a working script, save it to the file "warm_focus_rss.py"

Here is what the script should do:

1. Identify key information needed for a podcast RSS feed from the Warm Focus website.
2. Create a valid podcast feed using this information.

Here is what we know so far about how to get this information:

1. The radio show webpage is: https://bff.fm/shows/warm-focus
2. All information is accessible via the HTML source.
3. Each show is in an li element with class "BroadcastRow"
   1. Each title is inside the show element in an h3 element with class "BroadcastRow-title"
   2. Each air date is inside the show element in a time element with class "BroadcastRow-date"
   3. Each album art URL is inside the show element in an img element with class "BroadcastRow-image"
      1. These URLs have GET parameters which define a cropped version of the file. Removing them should give you the full sized file.
   4. Each MP3 URL is inside the show element in a button element with class "PlaybackInvoker".
      1. The button element has an attribute called "data-src". This is a base64 encoded string of the URL for the MP3.
