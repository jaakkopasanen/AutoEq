# Sennheiser Momentum In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 -8.7; 22 -9.0; 23 -9.1; 25 -9.3; 26 -9.4; 28 -9.5; 30 -9.6; 32 -9.6; 35 -9.6; 37 -9.5; 40 -9.5; 42 -9.5; 45 -9.5; 49 -9.5; 52 -9.5; 56 -9.6; 59 -9.7; 64 -9.9; 68 -10.0; 73 -10.2; 78 -10.4; 83 -10.6; 89 -10.8; 95 -10.9; 102 -11.1; 109 -11.2; 117 -11.3; 125 -11.4; 134 -11.4; 143 -11.4; 153 -11.4; 164 -11.2; 175 -11.1; 188 -10.9; 201 -10.6; 215 -10.3; 230 -9.9; 246 -9.4; 263 -9.8; 282 -9.7; 301 -9.1; 323 -8.5; 345 -7.9; 369 -7.4; 395 -6.9; 423 -6.4; 452 -5.9; 484 -5.3; 518 -4.7; 554 -4.1; 593 -3.6; 635 -3.0; 679 -2.4; 726 -1.8; 777 -1.2; 832 -0.7; 890 -0.3; 952 -0.1; 1019 0.1; 1090 0.2; 1167 0.3; 1248 0.5; 1336 0.8; 1429 1.0; 1529 1.3; 1636 1.5; 1751 1.7; 1873 1.9; 2004 2.2; 2145 2.5; 2295 2.9; 2455 3.4; 2627 3.8; 2811 4.2; 3008 4.6; 3219 4.9; 3444 5.1; 3685 4.9; 3943 4.8; 4219 4.4; 4514 3.9; 4830 3.1; 5168 2.0; 5530 0.5; 5917 -1.8; 6331 -4.9; 6775 -7.3; 7249 -7.5; 7756 -6.5; 8299 -5.0; 8880 -5.0; 9502 -6.5; 10167 -7.8; 10879 -7.4; 11640 -7.0; 12455 -8.9; 13327 -12.8; 14260 -16.8; 15258 -19.6; 16326 -20.5; 17469 -18.5; 18692 -13.3; 20000 -4.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.183656183813757dB` and instead set Global volume in the UI for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.16 | -9.1 dB  |
| Peaking | 222 Hz   | 0.57 | -5.7 dB  |
| Peaking | 3346 Hz  | 1.08 | 6.7 dB   |
| Peaking | 16225 Hz | 0.76 | -21.0 dB |
| Peaking | 24000 Hz | 1.19 | -6.2 dB  |
| Peaking | 1013 Hz  | 2.02 | 1.1 dB   |
| Peaking | 4980 Hz  | 3.41 | 2.3 dB   |
| Peaking | 6862 Hz  | 4.2  | -5.6 dB  |
| Peaking | 11985 Hz | 3.78 | 3.6 dB   |
| Peaking | 14357 Hz | 4.52 | -1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)