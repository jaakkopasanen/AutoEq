# Stax SR-003 SA-1993

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.7; 22 4.5; 23 4.4; 25 4.2; 26 4.1; 28 3.9; 30 3.8; 32 3.8; 35 3.7; 37 3.6; 40 3.6; 42 3.5; 45 3.4; 49 3.3; 52 3.3; 56 3.2; 59 3.2; 64 3.1; 68 3.0; 73 2.7; 78 2.5; 83 2.3; 89 1.9; 95 1.4; 102 0.8; 109 0.3; 117 -0.3; 125 -0.9; 134 -1.4; 143 -1.8; 153 -2.1; 164 -2.3; 175 -2.3; 188 -2.4; 201 -2.6; 215 -2.6; 230 -2.6; 246 -2.7; 263 -2.7; 282 -2.7; 301 -2.9; 323 -2.8; 345 -2.9; 369 -3.0; 395 -3.1; 423 -3.2; 452 -3.3; 484 -3.5; 518 -3.6; 554 -3.4; 593 -3.0; 635 -2.7; 679 -2.2; 726 -1.6; 777 -0.8; 832 0.3; 890 0.9; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.2; 1248 -2.2; 1336 -3.1; 1429 -4.2; 1529 -5.7; 1636 -6.1; 1751 -4.6; 1873 -3.2; 2004 -2.2; 2145 -0.8; 2295 0.2; 2455 1.5; 2627 1.7; 2811 3.4; 3008 5.1; 3219 5.9; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.1; 5917 2.5; 6331 3.0; 6775 1.3; 7249 0.5; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.4; 15258 -2.9; 16326 -4.0; 17469 -2.4; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-003 SA-1993 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.42 | 4.4 dB  |
| Peaking | 74 Hz    | 1.41 | 2.2 dB  |
| Peaking | 278 Hz   | 0.49 | -3.4 dB |
| Peaking | 1641 Hz  | 2.99 | -6.8 dB |
| Peaking | 3943 Hz  | 1.3  | 7.1 dB  |
| Peaking | 559 Hz   | 2.89 | -1.4 dB |
| Peaking | 896 Hz   | 4.45 | 2.5 dB  |
| Peaking | 5330 Hz  | 7.81 | 2.3 dB  |
| Peaking | 7912 Hz  | 2.21 | -1.1 dB |
| Peaking | 16477 Hz | 3.05 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-003%20SA-1993/Stax%20SR-003%20SA-1993.png)