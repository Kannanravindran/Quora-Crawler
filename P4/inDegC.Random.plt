#
# Undirected graph - degree Distribution. G(33685, 51292). 11542 (0.3426) nodes with in-deg > avg deg (3.0), 993 (0.0295) with >2*avg.deg (Wed Oct 14 23:02:22 2015)
#

set title "Undirected graph - degree Distribution. G(33685, 51292). 11542 (0.3426) nodes with in-deg > avg deg (3.0), 993 (0.0295) with >2*avg.deg"
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
set yrange[2.000000:]
set terminal png size 1000,800
set output 'inDegC.Random.png'
plot 	"inDegC.Random.tab" using 1:2 title "" with linespoints pt 6,\
	f1(x)=595461.923231*x**-4.076507, f1(x) title "6e+05 * x^{-4.077}  R^2:0.77" with lines linewidth 3
