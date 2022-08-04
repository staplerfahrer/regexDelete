# regexDelete
Delete files matching a regex. Command line utility. Allows for testing and multiple regexes.

-t is for testing, -d for actually deleting.

Usage:

    regexDelete -t "test1.*\.jpg$"

    regexDelete -d "pattern1.*\.jpg$" "pattern2.*\.bmp$"


On the Windows command line, double-escape your backslashes before the trailing " like so:

	regexDelete -d "(\\temp\\|temporary|temp-)" "\.pma$" "swreporter" "\\wer\\\\" "cache2?\\\\" "service worker" "itunes media" "Downloads" "CrashDumps"