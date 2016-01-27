#
# Directed graph - out-degree Distribution. G(35115, 101921). 992 (0.0283) nodes with out-deg > avg deg (5.8), 976 (0.0278) with >2*avg.deg (Mon Oct 12 20:30:42 2015)
#

set title "Directed graph - out-degree Distribution. G(35115, 101921). 992 (0.0283) nodes with out-deg > avg deg (5.8), 976 (0.0278) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Out-degree"
set ylabel "Count (CCDF)"
set tics scale 2
set yrange[1.000000:]
set terminal png size 1000,800
set output 'outDegC.outDegreeDistribution.png'
plot 	"outDegC.outDegreeDistribution.tab" using 1:2 title "" with linespoints pt 6,\
	f1(x)=28323.423039*x**-1.063658, f1(x) title "3e+04 * x^{-1.064}  R^2:0.64" with lines linewidth 3
