# mc-prod

MC production pipeline


First of all you should configure the path where you tuples are going to be
located. 


the general rule is...
```bash
produzione /scratch47/marcos.romero/mc-private-prod/{EventType}/{Year}/{Magnet}/{CustomFlag}_G{GaussVersion}_B{BooleVersion}/{Bunch}.digi -j
```

# Run Gauss

```bash
produzione /scratch47/marcos.romero/mc-private-prod/11144061/2015/MagUp/20211103_Gv49r11/5.sim -j
```

# Run Boole
```bash
produzione /scratch47/marcos.romero/mc-private-prod/11144061/2015/MagUp/20211103_Gv49r11_Bv30r4/5.digi -j
```


# Run Moore
```bash
produzione /scratch47/marcos.romero/mc-private-prod/11144061/2015/MagUp/20211103_Gv49r11_Bv30r4_M0v25r4/5.digi -j
produzione /scratch47/marcos.romero/mc-private-prod/11144061/2015/MagUp/20211103_Gv49r11_Bv30r4_M1v25r4/5.digi -j
produzione /scratch47/marcos.romero/mc-private-prod/11144061/2015/MagUp/20211103_Gv49r11_Bv30r4_M2v25r4/5.digi -j
```
``` brunel /scratch47/marcos.romero/mc-private-prod/11144061/2015/MagUp/20211103_Gv49r11_Bv30r4_M2v25r4_Bv50r7/5.dst ```
## FAQ
to force to rerun some file use `-F`





## TODO:
 - handle TCK
