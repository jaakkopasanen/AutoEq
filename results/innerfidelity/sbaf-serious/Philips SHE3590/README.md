# Philips SHE3590

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 10 -84; 20 -11.2; 22 -11.1; 23 -11.0; 25 -10.8; 26 -10.7; 28 -10.5; 30 -10.3; 32 -10.1; 35 -9.8; 37 -9.6; 40 -9.3; 42 -9.1; 45 -8.8; 49 -8.3; 52 -8.1; 56 -7.7; 59 -7.5; 64 -7.1; 68 -6.8; 73 -6.6; 78 -6.3; 83 -6.2; 89 -6.2; 95 -6.2; 102 -6.3; 109 -6.4; 117 -6.5; 125 -6.7; 134 -6.7; 143 -6.7; 153 -6.5; 164 -6.2; 175 -5.9; 188 -5.6; 201 -5.2; 215 -4.8; 230 -4.3; 246 -4.0; 263 -3.6; 282 -3.1; 301 -2.8; 323 -2.4; 345 -2.0; 369 -1.7; 395 -1.4; 423 -1.0; 452 -0.7; 484 -0.5; 518 -0.3; 554 0.1; 593 0.5; 635 0.6; 679 0.5; 726 0.5; 777 0.7; 832 0.8; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.5; 1336 -2.3; 1429 -3.1; 1529 -3.9; 1636 -4.6; 1751 -5.2; 1873 -5.7; 2004 -6.3; 2145 -7.0; 2295 -8.0; 2455 -8.4; 2627 -8.2; 2811 -6.6; 3008 -3.8; 3219 -1.1; 3444 0.8; 3685 1.3; 3943 0.8; 4219 -1.0; 4514 -2.8; 4830 -4.4; 5168 -5.3; 5530 -5.0; 5917 -3.2; 6331 -1.9; 6775 -0.7; 7249 0.5; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.8dB` and instead set Global volume in the UI for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE3590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 0.57 | -10.5 dB |
| Peaking | 35 Hz   | 0.42 | -7.2 dB  |
| Peaking | 159 Hz  | 0.98 | -4.8 dB  |
| Peaking | 2267 Hz | 2.12 | -8.7 dB  |
| Peaking | 5313 Hz | 5.32 | -5.5 dB  |
| Peaking | 805 Hz  | 1.49 | 1.7 dB   |
| Peaking | 1568 Hz | 2.98 | -1.3 dB  |
| Peaking | 2204 Hz | 3.74 | 4.2 dB   |
| Peaking | 2716 Hz | 1.37 | -4.7 dB  |
| Peaking | 3484 Hz | 3.26 | 6.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SHE3590/Philips%20SHE3590.png)