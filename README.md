# Hexahue decoder/encoder

Hexahue decoder & encoder

[What is Hexahue code](https://www.boxentriq.com/code-breaking/hexahue)

## Demo

You can encode message to Hexahue code as follow.

```
$ cd hexahue
$ python hexahue.py 
input mode (d: decode, e: encode) > e
input output image filename > demo.png
input message for encript > Hello, world.
```

Then, you'll get the encoded image as below.

[image★demo.png]

You can decode morse code to human message as follow.

```
$ cd hexahue
$ python hexahue.py
input mode (d: decode, e: encode) > d
input source filename > demo.png
HELLO, WORLD.
```

## Description

You can encode message to Hexahue code image, and decode Hexahue code image to message with this script.  
You can choose encoded image width, encode/decode image padding, and color for space (white or black) for encoding.

## Usage

Only execute `hexahue.py` on python3.

```
$ python hexahue.py
```

If you want run tests, execute shell script as follow.

```
$ cd hexahue
$ ./exec_test.sh
```

## Customize

You can specify below by editing `./settings.yml`.

* encoded image maximum width
* encode/decode image padding
* color for space (white or black) for encoding

## Limitation

* The target image have to 1 color by 1 pixel.
* Fuzzy color is not supported. 