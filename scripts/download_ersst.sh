yr=1880
while [ $yr -le 2016 ]; do
nm=1
while [ $nm -le 12 ]; do
if [ $nm -lt 10 ]; then
nm=0$nm
fi
wget ftp://ftp.ncdc.noaa.gov/pub/data/cmb/ersst/v5/netcdf/ersst.v5.$yr$nm.nc
nm=`expr $nm + 1`
done
yr=`expr $yr + 1`
done
