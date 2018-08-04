# Noontec Zoro II HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.0; 23 -1.0; 25 -1.1; 26 -1.2; 28 -1.2; 30 -1.3; 32 -1.3; 35 -1.3; 37 -1.4; 40 -1.4; 42 -1.3; 45 -1.3; 49 -1.2; 52 -1.2; 56 -1.3; 59 -1.3; 64 -1.4; 68 -1.4; 73 -1.3; 78 -1.4; 83 -1.4; 89 -1.5; 95 -2.0; 102 -2.4; 109 -2.6; 117 -2.6; 125 -2.6; 134 -3.0; 143 -3.7; 153 -4.1; 164 -3.9; 175 -3.8; 188 -4.1; 201 -4.0; 215 -3.9; 230 -3.6; 246 -3.3; 263 -2.9; 282 -2.4; 301 -2.0; 323 -2.0; 345 -1.9; 369 -1.7; 395 -1.5; 423 -1.3; 452 -1.3; 484 -1.3; 518 -0.8; 554 -0.4; 593 -0.1; 635 0.1; 679 0.1; 726 0.2; 777 0.4; 832 0.4; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.7; 1636 -1.9; 1751 -1.8; 1873 -1.5; 2004 -0.9; 2145 -0.2; 2295 0.5; 2455 1.4; 2627 1.8; 2811 2.2; 3008 2.9; 3219 3.2; 3444 4.3; 3685 5.6; 3943 6.0; 4219 6.0; 4514 5.1; 4830 3.3; 5168 2.9; 5530 3.8; 5917 3.9; 6331 2.9; 6775 2.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.65 | -1.1 dB |
| Peaking | 184 Hz  | 0.9  | -4.1 dB |
| Peaking | 1696 Hz | 3.03 | -2.5 dB |
| Peaking | 3929 Hz | 1.98 | 6.1 dB  |
| Peaking | 5965 Hz | 4.87 | 2.6 dB  |
| Peaking | 458 Hz  | 3.6  | -0.6 dB |
| Peaking | 736 Hz  | 2.18 | 0.8 dB  |
| Peaking | 9865 Hz | 2.95 | -0.3 dB |
| Peaking | 8166 Hz | 8.35 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20HD/Noontec%20Zoro%20II%20HD.png)