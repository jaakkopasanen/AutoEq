# Oppo PM3 Sample C

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.7; 22 2.5; 23 2.5; 25 2.4; 26 2.4; 28 2.3; 30 2.2; 32 2.2; 35 2.2; 37 2.2; 40 2.2; 42 2.2; 45 2.2; 49 2.3; 52 2.4; 56 2.3; 59 2.2; 64 2.3; 68 2.3; 73 2.4; 78 2.4; 83 2.4; 89 2.3; 95 1.9; 102 1.0; 109 0.4; 117 -0.2; 125 -0.9; 134 -1.3; 143 -1.5; 153 -1.4; 164 -0.6; 175 -0.7; 188 -1.2; 201 -0.9; 215 -0.4; 230 0.2; 246 0.7; 263 1.2; 282 2.0; 301 2.6; 323 3.1; 345 3.4; 369 3.6; 395 3.4; 423 3.1; 452 2.7; 484 2.1; 518 1.4; 554 1.1; 593 1.0; 635 0.6; 679 0.2; 726 0.0; 777 0.1; 832 0.1; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.6; 1336 -0.9; 1429 -1.3; 1529 -1.6; 1636 -1.5; 1751 -2.0; 1873 -2.6; 2004 -2.6; 2145 -2.7; 2295 -3.0; 2455 -1.9; 2627 -1.1; 2811 -1.2; 3008 -0.6; 3219 -0.0; 3444 0.4; 3685 -0.3; 3943 -0.6; 4219 -0.4; 4514 1.1; 4830 3.0; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 Sample C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.91 | 2.6 dB  |
| Peaking | 74 Hz    | 2.88 | 2.2 dB  |
| Peaking | 380 Hz   | 2.27 | 3.9 dB  |
| Peaking | 2071 Hz  | 1.58 | -2.9 dB |
| Peaking | 5741 Hz  | 3.27 | 7.0 dB  |
| Peaking | 96 Hz    | 3.24 | 1.6 dB  |
| Peaking | 146 Hz   | 1.39 | -1.9 dB |
| Peaking | 293 Hz   | 4.51 | 1.2 dB  |
| Peaking | 4126 Hz  | 8.83 | -1.4 dB |
| Peaking | 24000 Hz | 1.82 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3%20Sample%20C/Oppo%20PM3%20Sample%20C.png)