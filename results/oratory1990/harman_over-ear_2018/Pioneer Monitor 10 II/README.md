# Pioneer Monitor 10 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.9; 52 5.6; 56 5.3; 59 5.0; 64 4.5; 68 4.2; 73 3.8; 78 3.3; 83 2.9; 89 2.6; 95 2.4; 102 1.9; 109 1.2; 117 0.3; 125 -0.8; 134 -1.6; 143 -2.3; 153 -3.0; 164 -3.9; 175 -4.5; 188 -5.1; 201 -5.7; 215 -6.3; 230 -6.4; 246 -6.5; 263 -6.7; 282 -7.5; 301 -7.7; 323 -7.5; 345 -7.4; 369 -7.2; 395 -6.8; 423 -6.4; 452 -6.0; 484 -5.4; 518 -4.8; 554 -4.1; 593 -3.3; 635 -2.5; 679 -1.8; 726 -1.2; 777 -0.9; 832 -0.4; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.1; 1167 0.1; 1248 0.2; 1336 0.4; 1429 0.2; 1529 0.1; 1636 0.4; 1751 1.7; 1873 3.6; 2004 5.3; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -2.3; 14260 -6.2; 15258 -9.1; 16326 -9.8; 17469 -9.0; 18692 -8.5; 20000 -9.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.36 | 6.7 dB   |
| Peaking | 278 Hz   | 0.69 | -8.7 dB  |
| Peaking | 2285 Hz  | 2.76 | 3.9 dB   |
| Peaking | 4442 Hz  | 0.76 | 6.6 dB   |
| Peaking | 17768 Hz | 0.8  | -10.5 dB |
| Peaking | 850 Hz   | 3.2  | 1.3 dB   |
| Peaking | 1583 Hz  | 6.76 | -1.7 dB  |
| Peaking | 6404 Hz  | 4.23 | 2.8 dB   |
| Peaking | 7493 Hz  | 2.77 | -2.8 dB  |
| Peaking | 12242 Hz | 4.77 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Pioneer%20Monitor%2010%20II/Pioneer%20Monitor%2010%20II.png)