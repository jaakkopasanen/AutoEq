# Skullcandy Crusher Wireless Wired Sub Off

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 10 -84; 20 -4.7; 22 -5.2; 23 -5.4; 25 -5.7; 26 -5.9; 28 -6.2; 30 -6.5; 32 -6.7; 35 -7.1; 37 -7.3; 40 -7.5; 42 -7.5; 45 -7.5; 49 -7.5; 52 -7.9; 56 -8.3; 59 -8.2; 64 -7.2; 68 -6.2; 73 -5.2; 78 -5.7; 83 -7.2; 89 -8.8; 95 -9.4; 102 -9.0; 109 -9.0; 117 -9.4; 125 -10.4; 134 -10.9; 143 -10.9; 153 -10.3; 164 -9.0; 175 -9.8; 188 -9.2; 201 -8.4; 215 -7.7; 230 -6.6; 246 -5.7; 263 -4.8; 282 -3.8; 301 -2.9; 323 -2.4; 345 -1.6; 369 -0.8; 395 -0.3; 423 0.3; 452 0.8; 484 1.0; 518 1.3; 554 1.9; 593 2.3; 635 1.6; 679 0.9; 726 0.0; 777 -0.3; 832 -0.3; 890 -0.1; 952 0.0; 1019 0.0; 1090 -0.0; 1167 0.1; 1248 0.4; 1336 0.2; 1429 -0.3; 1529 -0.8; 1636 -1.2; 1751 -1.6; 1873 -1.8; 2004 -2.0; 2145 -2.6; 2295 -3.0; 2455 -3.1; 2627 -3.6; 2811 -4.3; 3008 -4.7; 3219 -4.8; 3444 -4.2; 3685 -4.0; 3943 -3.6; 4219 -4.3; 4514 -4.0; 4830 -2.6; 5168 -0.9; 5530 -1.9; 5917 -4.2; 6331 -3.7; 6775 -3.7; 7249 -4.5; 7756 -5.7; 8299 -7.2; 8880 -8.3; 9502 -8.9; 10167 -8.6; 10879 -7.6; 11640 -6.3; 12455 -4.7; 13327 -2.7; 14260 -0.7; 15258 -0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.3956025456387064dB` and instead set Global volume in the UI for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher Wireless Wired Sub Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of --0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.48 | -6.8 dB |
| Peaking | 151 Hz   | 1.19 | -9.1 dB |
| Peaking | 3143 Hz  | 1.5  | -4.4 dB |
| Peaking | 9660 Hz  | 1.55 | -9.2 dB |
| Peaking | 75 Hz    | 6.59 | 2.4 dB  |
| Peaking | 92 Hz    | 5.6  | -1.8 dB |
| Peaking | 228 Hz   | 3.6  | -1.7 dB |
| Peaking | 536 Hz   | 1.88 | 2.8 dB  |
| Peaking | 15261 Hz | 3.55 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Crusher%20Wireless%20Wired%20Sub%20Off/Skullcandy%20Crusher%20Wireless%20Wired%20Sub%20Off.png)