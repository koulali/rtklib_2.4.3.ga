#../app/rnx2rtkp/gcc/rnx2rtkp -p ppp-static -o pos_spt.out -e -t str20350.17o tidb0350.17o brdc0350.17n igs19346.sp3 igs19346.clk

#Kinematic solution with ambiguity resolution + antenna model 
#You can try remove the antex files from the configuration and 
#see how it impacts the solution !!

../app/rnx2rtkp/gcc/rnx2rtkp -i -v 2 -k opts5.conf -o pos.out str20350.17o tidb0350.17o brdc0350.17n igs19346.sp3 igs19346.clk
