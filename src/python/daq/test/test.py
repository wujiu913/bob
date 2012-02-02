#!/usr/bin/env python

"""Test data aquisition
"""

import os, sys
import unittest
import bob.io
from bob.daq import *
import tempfile

def test_file(name):
  """Returns the path to the filename for this test."""
  return os.path.join("../../io/test/data", name)

def get_tempfilename(prefix='bobtest_', suffix='.avi'):
  (fd, name) = tempfile.mkstemp(suffix, prefix)
  os.unlink(name)
  return name

INPUT_VIDEO = test_file('test.mov')
OUTPUT_VIDEO = get_tempfilename('bobtest_daq_video', suffix='')

class DaqTest(unittest.TestCase):
  """Performs various data aquisition tests."""
  
  def test_VideoReaderCamera(self):
    video = bob.io.VideoReader(INPUT_VIDEO)

    pf = PixelFormat.RGB24
    fs = FrameSize(video.width, video.height)
    fi = FrameInterval(1, int(video.frameRate))

    camera = VideoReaderCamera(video)

    self.assertTrue(camera.getSupportedPixelFormats()[0] == pf)
    self.assertTrue(camera.getSupportedFrameSizes(pf)[0] == fs)
    self.assertTrue(camera.getSupportedFrameIntervals(pf, fs)[0] == fi)

    fl = VisionerFaceLocalization()
    controller = SimpleController()
    display = ConsoleDisplay()

    outputWriter = BobOutputWriter()
    outputWriter.setOutputDir(os.path.dirname(OUTPUT_VIDEO))
    outputWriter.setOutputName(os.path.basename(OUTPUT_VIDEO))
    outputWriter.open(video.width, video.height, int(video.frameRate))

    controller.addControllerCallback(fl)
    controller.addControllerCallback(display)
    controller.addStoppable(camera)

    controller.setOutputWriter(outputWriter)
    controller.recordingDelay = 1
    controller.length = 3

    fl.addFaceLocalizationCallback(display)
    
    camera.addCameraCallback(controller)

    self.assertTrue(camera.start() == 0)
    self.assertTrue(fl.start() == True)
    display.start()

    del outputWriter

    text_file = OUTPUT_VIDEO + ".txt"
    video_file = OUTPUT_VIDEO + ".avi"

    self.assertTrue(os.path.exists(video_file))
    self.assertTrue(os.path.exists(text_file))

    os.unlink(video_file)
    os.unlink(text_file)

if __name__ == '__main__':
  sys.argv.append('-v')
  if os.environ.has_key('BOB_PROFILE') and \
      os.environ['BOB_PROFILE'] and \
      hasattr(bob.core, 'ProfilerStart'):
    bob.core.ProfilerStart(os.environ['BOB_PROFILE'])
  os.chdir(os.path.realpath(os.path.dirname(sys.argv[0])))
  unittest.main()
  if os.environ.has_key('BOB_PROFILE') and \
      os.environ['BOB_PROFILE'] and \
      hasattr(bob.core, 'ProfilerStop'):
    bob.core.ProfilerStop()
