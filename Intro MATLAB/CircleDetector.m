picture = imread('bluecirc.jpg');
imshow(picture)
%%
d = drawline
%%
pos = d.Position;
diffPos = diff(pos);
diameter = hypot(diffPos(1), diffPos(2))
%%
grayImage = rgb2gray(picture);
imshow(grayImage)
%%
[centres, radii] = imfindcircles(picture,[10, 30], 'ObjectPolarity', 'bright')
%%
viscircles(centres, radii,'Color','b');
%imshow(picture)
