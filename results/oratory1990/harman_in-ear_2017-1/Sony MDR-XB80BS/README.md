# Sony MDR-XB80BS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.0; 23 -2.1; 25 -2.1; 26 -2.1; 28 -2.1; 30 -2.2; 32 -2.3; 35 -2.3; 37 -2.4; 40 -2.5; 42 -2.6; 45 -2.7; 49 -2.9; 52 -3.0; 56 -3.2; 59 -3.3; 64 -3.6; 68 -3.8; 73 -4.0; 78 -4.3; 83 -4.5; 89 -4.9; 95 -5.3; 102 -5.7; 109 -5.7; 117 -5.8; 125 -5.8; 134 -5.7; 143 -5.6; 153 -5.3; 164 -5.0; 175 -4.5; 188 -4.0; 201 -3.4; 215 -2.8; 230 -2.2; 246 -1.7; 263 -1.2; 282 -0.9; 301 -0.5; 323 -0.2; 345 -0.0; 369 0.1; 395 0.1; 423 0.0; 452 0.0; 484 -0.0; 518 -0.0; 554 -0.1; 593 -0.1; 635 -0.1; 679 -0.1; 726 0.0; 777 0.1; 832 0.2; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.0; 1248 0.2; 1336 0.7; 1429 1.3; 1529 1.8; 1636 2.3; 1751 2.7; 1873 2.9; 2004 3.1; 2145 3.1; 2295 3.0; 2455 2.8; 2627 2.8; 2811 3.4; 3008 4.5; 3219 5.7; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.0; 5530 2.4; 5917 0.4; 6331 2.1; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.7; 15258 -6.1; 16326 -9.5; 17469 -10.5; 18692 -10.1; 20000 -8.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999988230117dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB80BS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 0.46 | -2.4 dB  |
| Peaking | 128 Hz   | 1.12 | -5.1 dB  |
| Peaking | 1861 Hz  | 3    | 1.9 dB   |
| Peaking | 3979 Hz  | 1.2  | 6.5 dB   |
| Peaking | 18176 Hz | 1.25 | -12.0 dB |
| Peaking | 190 Hz   | 4.17 | -0.7 dB  |
| Peaking | 349 Hz   | 2.18 | 0.9 dB   |
| Peaking | 13497 Hz | 2.68 | 3.1 dB   |
| Peaking | 15892 Hz | 3.77 | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20MDR-XB80BS/Sony%20MDR-XB80BS.png)