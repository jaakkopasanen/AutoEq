# Phiaton PS 300 NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.4; 22 2.5; 23 1.6; 25 0.1; 26 -0.6; 28 -1.8; 30 -2.7; 32 -3.5; 35 -4.4; 37 -5.0; 40 -5.6; 42 -5.9; 45 -6.3; 49 -6.8; 52 -7.2; 56 -7.4; 59 -7.4; 64 -7.5; 68 -7.5; 73 -8.4; 78 -9.5; 83 -9.7; 89 -9.9; 95 -10.0; 102 -10.1; 109 -10.1; 117 -10.2; 125 -10.4; 134 -10.5; 143 -10.5; 153 -10.6; 164 -10.5; 175 -10.4; 188 -10.1; 201 -9.6; 215 -9.6; 230 -9.6; 246 -9.4; 263 -9.4; 282 -9.5; 301 -9.5; 323 -9.5; 345 -9.3; 369 -8.9; 395 -8.2; 423 -7.0; 452 -5.4; 484 -2.8; 518 0.6; 554 3.4; 593 4.9; 635 4.5; 679 3.9; 726 3.3; 777 2.4; 832 1.5; 890 0.9; 952 0.4; 1019 -0.1; 1090 -0.8; 1167 -2.0; 1248 -2.4; 1336 -3.9; 1429 -6.0; 1529 -8.1; 1636 -9.7; 1751 -10.7; 1873 -9.7; 2004 -7.8; 2145 -6.0; 2295 -4.5; 2455 -3.0; 2627 -1.3; 2811 -1.3; 3008 -0.8; 3219 1.8; 3444 5.3; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.6; 7249 1.3; 7756 0.1; 8299 -1.6; 8880 -1.5; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09999993821055dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 300 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 85 Hz   | 0.69 | -8.9 dB  |
| Peaking | 190 Hz  | 1.36 | -6.6 dB  |
| Peaking | 337 Hz  | 3.04 | -7.4 dB  |
| Peaking | 1796 Hz | 2.68 | -12.0 dB |
| Peaking | 4591 Hz | 1.52 | 7.5 dB   |
| Peaking | 20 Hz   | 3.51 | 4.9 dB   |
| Peaking | 439 Hz  | 3.31 | -5.1 dB  |
| Peaking | 605 Hz  | 2.22 | 7.7 dB   |
| Peaking | 6266 Hz | 5.99 | 2.9 dB   |
| Peaking | 8420 Hz | 3.66 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20300%20NC/Phiaton%20PS%20300%20NC.png)