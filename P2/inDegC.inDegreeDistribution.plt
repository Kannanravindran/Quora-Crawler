#
# Directed graph - in-degree Distribution. G(35115, 101921). 2604 (0.0742) nodes with in-deg > avg deg (5.8), 1145 (0.0326) with >2*avg.deg (Mon Oct 12 20:30:42 2015)
#

set title "Directed graph - in-degree Distribution. G(35115, 101921). 2604 (0.0742) nodes with in-deg > avg deg (5.8), 1145 (0.0326) with >2*avg.deg"
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
set output 'inDegC.inDegreeDistribution.png'
plot 	"inDegC.inDegreeDistribution.tab" using 1:2 title "" with linespoints pt 6,\
	f1(x)=34543.379335*x**-1.337983, f1(x) title "3e+04 * x^{-1.338}  R^2:0.99" with lines linewidth 3
