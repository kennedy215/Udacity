#3rd Technique Clearfix

##Details

As a developer, you should always strive to write your code as clearly as possible. Keep surprises to a minimum. The example above breaks the commandment because the HTML seems to indicate that .sibling will be rendered underneath .parent and all of its children, but that's not what happens.

The third technique to clear floats, clearfix, combines aspects of the first two. The goal of the clearfix is to make a normal flow parent resize its box model to fit all of the floats inside it. There are two general techniques to do so.

Add an element with clear: both to the end of a parent. This ensures that the last element is a normal flow element that has been pushed below all the floats.
Turn the parent into a block formatting context with an overflow property other than visible. The block formatting context respects the boundaries of floats and ensures the parent's box model encompasses float children.
The first technique by itself, adding an HTML element with clear: both, violates the commandment of code clarity; HTML should be restricted to rendered content. However, applying the same technique with a pseudo-element works nicely. Here's how it looks.

From **-Udacity**
