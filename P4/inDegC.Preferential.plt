#
# Undirected graph - degree Distribution. G(35668, 178315). 9795 (0.2746) nodes with in-deg > avg deg (10.0), 2590 (0.0726) with >2*avg.deg (Wed Oct 14 23:02:22 2015)
#

set title "Undirected graph - degree Distribution. G(35668, 178315). 9795 (0.2746) nodes with in-deg > avg deg (10.0), 2590 (0.0726) with >2*avg.deg"
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
set yrange[1.000000:]
set terminal png size 1000,800
set output 'inDegC.Preferential.png'
plot 	"inDegC.Preferential.tab" using 1:2 title "" with linespoints pt 6,\
	f1(x)=819009.268875*x**-1.921862, f1(x) title "8e+05 * x^{-1.922}  R^2:0.99" with lines linewidth 3
