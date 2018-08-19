# Cowin E7 Wired NC off

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.7; 26 5.5; 28 4.8; 30 3.9; 32 2.9; 35 1.7; 37 1.0; 40 0.0; 42 -0.5; 45 -1.3; 49 -2.1; 52 -2.5; 56 -2.7; 59 -2.8; 64 -2.9; 68 -3.3; 73 -4.1; 78 -5.1; 83 -6.1; 89 -7.2; 95 -8.2; 102 -9.1; 109 -9.7; 117 -9.9; 125 -10.5; 134 -11.3; 143 -12.0; 153 -12.2; 164 -11.5; 175 -12.4; 188 -12.8; 201 -12.5; 215 -12.2; 230 -11.5; 246 -10.8; 263 -10.0; 282 -8.9; 301 -8.0; 323 -7.1; 345 -6.2; 369 -5.7; 395 -5.3; 423 -4.2; 452 -3.3; 484 -2.7; 518 -2.1; 554 -1.4; 593 -0.7; 635 -0.5; 679 -0.4; 726 -0.3; 777 0.0; 832 -0.3; 890 -0.2; 952 -0.0; 1019 -0.0; 1090 -0.7; 1167 -0.4; 1248 -0.2; 1336 -0.0; 1429 0.3; 1529 0.9; 1636 1.2; 1751 1.0; 1873 1.9; 2004 2.4; 2145 3.1; 2295 3.9; 2455 5.1; 2627 5.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.3; 4219 1.7; 4514 -2.1; 4830 -4.3; 5168 -4.4; 5530 -3.8; 5917 -4.0; 6331 -4.8; 6775 -5.4; 7249 -4.3; 7756 -2.6; 8299 -1.7; 8880 -1.7; 9502 -2.0; 10167 -2.1; 10879 -1.8; 11640 -1.4; 12455 -1.4; 13327 -1.9; 14260 -1.9; 15258 -0.8; 16326 -0.5; 17469 -2.4; 18692 -4.4; 20000 -4.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 Wired NC off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 1.53 | 6.9 dB   |
| Peaking | 127 Hz  | 0.81 | -7.9 dB  |
| Peaking | 223 Hz  | 1.03 | -7.9 dB  |
| Peaking | 3607 Hz | 1.07 | 16.8 dB  |
| Peaking | 4862 Hz | 0.85 | -14.0 dB |
| Peaking | 15 Hz   | 1.17 | 1.1 dB   |
| Peaking | 697 Hz  | 1.34 | 2.3 dB   |
| Peaking | 985 Hz  | 0.47 | -1.7 dB  |
| Peaking | 2678 Hz | 1.87 | 2.3 dB   |
| Peaking | 3258 Hz | 5.99 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cowin%20E7%20Wired%20NC%20off/Cowin%20E7%20Wired%20NC%20off.png)