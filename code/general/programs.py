app_call_dict = {}
app_src_dict = {}


# Blackscholes [keyword = blackscholes]
app_call_dict["blackscholes"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/pkgs/apps/blackscholes/src/blackscholes $ $ $"
app_src_dict["blackscholes"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/pkgs/apps/blackscholes/src"


# Swaptions [keyword = swaptions]
app_call_dict["swaptions"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/pkgs/apps/swaptions/src/swaptions -ns $ -sm $ -nt $ -sd $"
app_src_dict["swaptions"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/pkgs/apps/swaptions/src"


# Streamcluster [keyword = streamcluster]
app_call_dict["streamcluster"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/pkgs/kernels/streamcluster/src/streamcluster $ $ $ $ $ $ $ $ $"
app_src_dict["streamcluster"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/pkgs/kernels/streamcluster/src"


# LU [keyword = lu]
# -nN : Decompose NxN matrix.
# -pP : P = number of processors.
# -bB : Use a block size of B. BxB elements should fit in cache for
#       good performance. Small block sizes (B=8, B=16) work well.
app_call_dict["lu"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/ext/splash2/kernels/lu_cb/src/lu_cb -n$ -p$ -b$"
app_src_dict["lu"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/ext/splash2/kernels/lu_cb/src"


# FFT [keyword = fft]
# -mM : M = even integer; 2**M total complex data points transformed.
# -pP : P = number of processors; Must be a power of 2.
# -nN : N = number of cache lines.
# -lL : L = Log base 2 of cache line length in bytes.
app_call_dict["fft"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/ext/splash2/kernels/fft/src/fft -m$ -p$ -n$ -l$"
app_src_dict["fft"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/ext/splash2/kernels/fft/src"


# Water_nsquared [keyword = water]
# Usage: water < infile
app_call_dict["water"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/ext/splash2/apps/water_nsquared/src/water_nsquared < $"
app_src_dict["water"] = "/shared/workspace/aditikg2/TESTING_STUFF/parsec-3.0/ext/splash2/apps/water_nsquared/src"
