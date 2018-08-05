# 1MORE Multi Unit Earphones

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.3; 22 -0.8; 23 -1.0; 25 -1.4; 26 -1.6; 28 -1.9; 30 -2.1; 32 -2.4; 35 -2.6; 37 -2.8; 40 -3.0; 42 -3.0; 45 -3.1; 49 -3.3; 52 -3.4; 56 -3.5; 59 -3.5; 64 -3.5; 68 -3.5; 73 -3.7; 78 -3.7; 83 -3.9; 89 -4.2; 95 -4.5; 102 -5.0; 109 -5.3; 117 -5.7; 125 -6.1; 134 -6.3; 143 -6.5; 153 -6.5; 164 -6.4; 175 -6.1; 188 -5.9; 201 -5.7; 215 -5.3; 230 -5.0; 246 -4.6; 263 -4.3; 282 -3.9; 301 -3.6; 323 -3.2; 345 -2.8; 369 -2.4; 395 -2.0; 423 -1.6; 452 -1.1; 484 -0.9; 518 -0.6; 554 -0.1; 593 0.3; 635 0.5; 679 0.6; 726 0.8; 777 0.9; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.2; 1336 -1.9; 1429 -2.8; 1529 -3.6; 1636 -4.4; 1751 -5.1; 1873 -5.6; 2004 -5.9; 2145 -5.9; 2295 -5.4; 2455 -3.8; 2627 -2.0; 2811 -0.3; 3008 1.4; 3219 2.1; 3444 2.2; 3685 0.8; 3943 -1.5; 4219 -2.8; 4514 -0.1; 4830 4.3; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -1.7; 10167 -3.6; 10879 -3.3; 11640 -1.6; 12455 -0.1; 13327 0.0; 14260 -0.6; 15258 -2.1; 16326 -3.5; 17469 -4.1; 18692 -3.7; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Multi Unit Earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 52 Hz    | 0.56 | -2.5 dB |
| Peaking | 166 Hz   | 0.88 | -5.9 dB |
| Peaking | 1962 Hz  | 2.5  | -6.7 dB |
| Peaking | 5794 Hz  | 2.75 | 7.7 dB  |
| Peaking | 20069 Hz | 0.2  | -3.1 dB |
| Peaking | 748 Hz   | 2.62 | 1.8 dB  |
| Peaking | 3273 Hz  | 5.26 | 3.3 dB  |
| Peaking | 4171 Hz  | 8.99 | -4.6 dB |
| Peaking | 10520 Hz | 5.69 | -3.1 dB |
| Peaking | 13203 Hz | 3.34 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Multi%20Unit%20Earphones/1MORE%20Multi%20Unit%20Earphones.png)