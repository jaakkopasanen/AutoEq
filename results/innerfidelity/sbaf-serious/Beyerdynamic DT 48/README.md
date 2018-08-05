# Beyerdynamic DT 48

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 4.5; 73 -1.5; 78 -6.1; 83 -6.5; 89 -4.6; 95 -3.1; 102 -2.8; 109 -3.2; 117 -3.1; 125 -2.8; 134 -2.5; 143 -2.2; 153 -1.7; 164 -1.5; 175 -2.6; 188 -2.0; 201 -1.6; 215 -1.2; 230 -0.7; 246 -0.3; 263 0.1; 282 0.6; 301 1.1; 323 1.5; 345 1.8; 369 2.1; 395 2.5; 423 3.3; 452 4.0; 484 4.6; 518 5.4; 554 6.0; 593 6.0; 635 6.0; 679 5.2; 726 3.7; 777 3.4; 832 3.2; 890 2.2; 952 0.9; 1019 -0.3; 1090 -1.6; 1167 -2.8; 1248 -3.6; 1336 -4.0; 1429 -4.7; 1529 -5.4; 1636 -6.2; 1751 -6.7; 1873 -7.0; 2004 -6.8; 2145 -6.1; 2295 -5.2; 2455 -2.8; 2627 -0.7; 2811 1.0; 3008 1.9; 3219 2.1; 3444 3.3; 3685 4.7; 3943 5.4; 4219 5.6; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 0.2; 7756 -5.1; 8299 -9.0; 8880 -9.0; 9502 -5.0; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.9; 15258 -5.1; 16326 -8.7; 17469 -10.5; 18692 -9.1; 20000 -3.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.5  | 7.4 dB   |
| Peaking | 1843 Hz  | 1.04 | -18.4 dB |
| Peaking | 4007 Hz  | 0.15 | 11.4 dB  |
| Peaking | 8600 Hz  | 3.16 | -18.1 dB |
| Peaking | 17369 Hz | 0.96 | -15.3 dB |
| Peaking | 65 Hz    | 2.03 | 9.5 dB   |
| Peaking | 80 Hz    | 3.93 | -10.7 dB |
| Peaking | 125 Hz   | 0.64 | -3.8 dB  |
| Peaking | 574 Hz   | 1.84 | 4.0 dB   |
| Peaking | 1170 Hz  | 3.57 | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048/Beyerdynamic%20DT%2048.png)