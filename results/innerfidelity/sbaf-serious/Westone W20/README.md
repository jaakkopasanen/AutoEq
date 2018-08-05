# Westone W20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.3; 22 2.2; 23 2.1; 25 2.0; 26 1.9; 28 1.9; 30 1.8; 32 1.7; 35 1.6; 37 1.6; 40 1.5; 42 1.5; 45 1.4; 49 1.3; 52 1.3; 56 1.2; 59 1.2; 64 1.1; 68 1.0; 73 0.8; 78 0.6; 83 0.4; 89 -0.0; 95 -0.5; 102 -1.1; 109 -1.5; 117 -2.1; 125 -2.7; 134 -3.3; 143 -3.5; 153 -3.6; 164 -3.9; 175 -3.9; 188 -3.9; 201 -3.9; 215 -3.9; 230 -3.7; 246 -3.7; 263 -3.5; 282 -3.4; 301 -3.2; 323 -3.1; 345 -2.8; 369 -2.7; 395 -2.5; 423 -2.1; 452 -1.9; 484 -1.7; 518 -1.5; 554 -1.1; 593 -0.6; 635 -0.4; 679 -0.3; 726 -0.0; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -1.1; 1529 -1.4; 1636 -1.7; 1751 -1.8; 1873 -1.8; 2004 -1.6; 2145 -1.5; 2295 -1.0; 2455 0.4; 2627 1.9; 2811 3.9; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.2; 5168 4.2; 5530 5.2; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.28 | 2.5 dB  |
| Peaking | 185 Hz  | 0.66 | -5.5 dB |
| Peaking | 2075 Hz | 1.77 | -4.4 dB |
| Peaking | 6035 Hz | 4.62 | 4.3 dB  |
| Peaking | 3486 Hz | 1.26 | 7.5 dB  |
| Peaking | 9 Hz    | 1.33 | 0.8 dB  |
| Peaking | 822 Hz  | 3.04 | 0.9 dB  |
| Peaking | 1536 Hz | 6.11 | -0.6 dB |
| Peaking | 6757 Hz | 3.6  | 1.8 dB  |
| Peaking | 7693 Hz | 2.42 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W20/Westone%20W20.png)