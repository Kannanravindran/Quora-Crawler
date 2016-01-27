#
# Undirected graph - degree Distribution. G(18, 27). 0 (0.0000) nodes with in-deg > avg deg (3.0), 0 (0.0000) with >2*avg.deg (Wed Oct 14 23:02:22 2015)
#

set title "Undirected graph - degree Distribution. G(18, 27). 0 (0.0000) nodes with in-deg > avg deg (3.0), 0 (0.0000) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count (CCDF)"
set tics scale 2
set yrange[18.000000:]
set terminal png size 1000,800
set output 'inDegC.Small.png'
plot 	"inDegC.Small.tab" using 1:2 title "" with linespoints pt 6,\
	f1(x)=1.000000*x**0.000000, f1(x) title "1 * x^{0}  R^2:-nan" with lines linewidth 3
