# FLC Technology FLC8 C C Gn Strin

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.8; 68 5.7; 73 5.6; 78 5.3; 83 5.0; 89 4.5; 95 4.0; 102 3.3; 109 2.8; 117 2.2; 125 1.6; 134 1.0; 143 0.6; 153 0.5; 164 0.3; 175 0.2; 188 0.1; 201 0.0; 215 0.1; 230 0.2; 246 0.1; 263 0.3; 282 0.4; 301 0.4; 323 0.5; 345 0.7; 369 0.8; 395 0.9; 423 1.2; 452 1.3; 484 1.2; 518 1.3; 554 1.6; 593 1.9; 635 1.9; 679 1.8; 726 1.6; 777 1.7; 832 1.7; 890 1.2; 952 0.6; 1019 -0.2; 1090 -0.9; 1167 -1.3; 1248 -1.5; 1336 -1.6; 1429 -1.4; 1529 -0.7; 1636 0.0; 1751 0.9; 1873 1.8; 2004 2.2; 2145 2.4; 2295 2.3; 2455 2.0; 2627 1.5; 2811 1.4; 3008 4.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.7; 4514 3.2; 4830 4.7; 5168 6.0; 5530 6.0; 5917 5.0; 6331 1.2; 6775 -4.4; 7249 -7.3; 7756 -6.7; 8299 -4.9; 8880 -4.1; 9502 -5.0; 10167 -6.1; 10879 -5.2; 11640 -2.4; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technology FLC8 C C Gn Strin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.5  | 6.8 dB   |
| Peaking | 3522 Hz  | 2.21 | 6.0 dB   |
| Peaking | 5750 Hz  | 2.69 | 8.7 dB   |
| Peaking | 10304 Hz | 4.1  | -5.7 dB  |
| Peaking | 7237 Hz  | 2.84 | -10.5 dB |
| Peaking | 85 Hz    | 1.21 | 3.9 dB   |
| Peaking | 103 Hz   | 0.58 | -2.9 dB  |
| Peaking | 857 Hz   | 0.77 | 4.4 dB   |
| Peaking | 1252 Hz  | 0.97 | -5.3 dB  |
| Peaking | 1943 Hz  | 2.87 | 3.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technology%20FLC8%20C%20C%20Gn%20Strin/FLC%20Technology%20FLC8%20C%20C%20Gn%20Strin.png)