# These are some of the classes of a complex video conversion
# framework. We don't control that code, therefore
# can't simplify it.


class VideoFile:
    def operation(self, filename):
        pass


class OggCompressionCodec:
    def operation(self):
        pass


class MPEG4CompressionCodec:
    def operation(self):
        pass


class CodecFactory:
    def operation(self):
        pass


class BitrateReader:
    def operation(self):
        pass


class AudioMixer:
    def operation(self):
        pass


# We create a facade class to hide the framework's complexity
# behind a simple interface.
class VideoConverter:
    def convert(self, filename, format):
        VideoFile().operation(filename)
        CodecFactory().operation()
        if format == "mp4":
            MPEG4CompressionCodec().operation()
        else:
            OggCompressionCodec().operation()
        BitrateReader().operation()
        AudioMixer().operation()


# Application classes don't depend on a billion classes
# provided by the complex framework. Also, if you decide to
# switch frameworks, you only need to rewrite the facade class.

VideoConverter().convert("youtubevideo.ogg", "mp4")
