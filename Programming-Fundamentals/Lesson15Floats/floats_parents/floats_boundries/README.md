##Formatting Contexts

###Description:

Notes for strategy how to make boundaries respect floats.
###Strategy 1: Block Formatting Contexts
This strategy forces normal flow siblings to respect the boundaries of floats. Elements with a block formatting context (remember those from last lesson!) may not overlap floats.

This rule originally protected elements like ```<table>```, which create their own block formatting context, from being invaded by floats. The reasoning behind this is that you wouldn't want a random image to push aside all the text inside a carefully built table.

You can take advantage of this rule - if you force elements to establish a block formatting context, they'll respect the boundaries of the float.

In this example, I'm using the overflow property to set a block formatting context (any value other than visible, including auto, forces an element to take on a block formatting context).
**- Udacity**

###Credit

Example from Udacity course.
