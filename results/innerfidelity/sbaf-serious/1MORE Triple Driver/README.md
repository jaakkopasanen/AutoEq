# 1MORE Triple Driver

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.3; 23 -1.5; 25 -1.9; 26 -2.1; 28 -2.4; 30 -2.7; 32 -2.9; 35 -3.2; 37 -3.3; 40 -3.5; 42 -3.6; 45 -3.8; 49 -3.9; 52 -4.0; 56 -4.0; 59 -4.1; 64 -4.1; 68 -4.2; 73 -4.3; 78 -4.4; 83 -4.6; 89 -4.9; 95 -5.3; 102 -5.7; 109 -6.0; 117 -6.4; 125 -6.9; 134 -7.1; 143 -7.3; 153 -7.2; 164 -7.2; 175 -7.0; 188 -6.7; 201 -6.5; 215 -6.2; 230 -5.8; 246 -5.5; 263 -5.2; 282 -4.7; 301 -4.4; 323 -4.0; 345 -3.5; 369 -3.1; 395 -2.8; 423 -2.3; 452 -1.8; 484 -1.6; 518 -1.2; 554 -0.7; 593 -0.2; 635 0.1; 679 0.2; 726 0.4; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.4; 1336 -1.0; 1429 -1.6; 1529 -2.2; 1636 -2.9; 1751 -3.3; 1873 -3.6; 2004 -3.9; 2145 -4.3; 2295 -4.7; 2455 -4.5; 2627 -4.3; 2811 -3.6; 3008 -2.2; 3219 -1.0; 3444 -0.3; 3685 -1.0; 3943 -2.9; 4219 -5.1; 4514 -5.2; 4830 -2.2; 5168 2.8; 5530 5.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.3; 9502 -3.7; 10167 -3.8; 10879 -1.7; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 -0.9; 15258 -3.8; 16326 -4.8; 17469 -3.5; 18692 -1.6; 20000 -0.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 55 Hz    | 0.43 | -3.0 dB |
| Peaking | 175 Hz   | 0.81 | -6.1 dB |
| Peaking | 2253 Hz  | 1.94 | -4.9 dB |
| Peaking | 4443 Hz  | 5.47 | -6.9 dB |
| Peaking | 5812 Hz  | 3.77 | 7.9 dB  |
| Peaking | 799 Hz   | 2.12 | 1.5 dB  |
| Peaking | 1632 Hz  | 5.52 | -1.1 dB |
| Peaking | 12497 Hz | 0.77 | 3.1 dB  |
| Peaking | 9852 Hz  | 3.24 | -6.1 dB |
| Peaking | 31583 Hz | 1.57 | -6.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Triple%20Driver/1MORE%20Triple%20Driver.png)