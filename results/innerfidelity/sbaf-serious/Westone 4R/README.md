# Westone 4R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.3; 22 2.8; 23 2.5; 25 2.1; 26 1.9; 28 1.5; 30 1.2; 32 0.9; 35 0.5; 37 0.3; 40 0.1; 42 -0.1; 45 -0.3; 49 -0.5; 52 -0.7; 56 -0.8; 59 -1.0; 64 -1.2; 68 -1.4; 73 -1.6; 78 -1.8; 83 -2.1; 89 -2.7; 95 -3.1; 102 -3.7; 109 -4.2; 117 -4.9; 125 -5.5; 134 -6.0; 143 -6.3; 153 -6.5; 164 -6.6; 175 -6.7; 188 -6.7; 201 -6.6; 215 -6.6; 230 -6.4; 246 -6.3; 263 -6.2; 282 -6.0; 301 -5.8; 323 -5.6; 345 -5.3; 369 -5.1; 395 -4.8; 423 -4.4; 452 -4.1; 484 -3.8; 518 -3.4; 554 -2.9; 593 -2.2; 635 -1.8; 679 -1.4; 726 -0.9; 777 -0.4; 832 -0.1; 890 0.0; 952 0.1; 1019 -0.0; 1090 -0.3; 1167 -0.4; 1248 -0.6; 1336 -0.9; 1429 -1.0; 1529 -1.1; 1636 -0.9; 1751 -0.5; 1873 0.2; 2004 0.9; 2145 1.6; 2295 2.3; 2455 3.2; 2627 3.9; 2811 4.5; 3008 5.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -4.0; 9502 -6.8; 10167 -7.6; 10879 -5.0; 11640 -0.7; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 4R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 8 Hz     | 0.23 | 3.5 dB   |
| Peaking | 222 Hz   | 0.47 | -7.2 dB  |
| Peaking | 1716 Hz  | 1.07 | -6.8 dB  |
| Peaking | 3380 Hz  | 0.32 | 8.3 dB   |
| Peaking | 9701 Hz  | 2.38 | -12.0 dB |
| Peaking | 39 Hz    | 0.88 | -2.4 dB  |
| Peaking | 39 Hz    | 0.34 | 1.8 dB   |
| Peaking | 135 Hz   | 2.23 | -1.3 dB  |
| Peaking | 12066 Hz | 8.41 | 1.5 dB   |
| Peaking | 15870 Hz | 1.03 | -0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%204R/Westone%204R.png)