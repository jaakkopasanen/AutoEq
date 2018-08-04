# Cowin E7 Wired NC off

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.8; 26 5.5; 28 4.8; 30 3.9; 32 3.0; 35 1.8; 37 1.1; 40 0.2; 42 -0.4; 45 -1.1; 49 -1.9; 52 -2.2; 56 -2.4; 59 -2.4; 64 -2.4; 68 -2.7; 73 -3.4; 78 -4.3; 83 -5.3; 89 -6.4; 95 -7.5; 102 -8.5; 109 -9.3; 117 -9.7; 125 -10.5; 134 -11.5; 143 -12.2; 153 -12.4; 164 -11.8; 175 -12.7; 188 -13.0; 201 -12.7; 215 -12.3; 230 -11.6; 246 -10.9; 263 -10.0; 282 -8.9; 301 -8.0; 323 -7.1; 345 -6.2; 369 -5.7; 395 -5.3; 423 -4.2; 452 -3.3; 484 -2.7; 518 -2.1; 554 -1.4; 593 -0.7; 635 -0.5; 679 -0.5; 726 -0.3; 777 0.0; 832 -0.3; 890 -0.2; 952 -0.0; 1019 -0.0; 1090 -0.7; 1167 -0.4; 1248 -0.2; 1336 -0.0; 1429 0.3; 1529 0.9; 1636 1.2; 1751 1.0; 1873 1.9; 2004 2.4; 2145 3.1; 2295 3.9; 2455 5.1; 2627 5.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.3; 4219 1.7; 4514 -2.1; 4830 -4.3; 5168 -4.4; 5530 -3.8; 5917 -4.0; 6331 -4.8; 6775 -5.4; 7249 -4.3; 7756 -2.6; 8299 -1.7; 8880 -1.7; 9502 -2.0; 10167 -2.1; 10879 -1.8; 11640 -1.4; 12455 -1.4; 13327 -1.9; 14260 -1.9; 15258 -0.8; 16326 -0.5; 17469 -2.4; 18692 -4.4; 20000 -4.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 Wired NC off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.59 | 6.9 dB   |
| Peaking | 133 Hz  | 0.89 | -7.9 dB  |
| Peaking | 224 Hz  | 1.02 | -8.1 dB  |
| Peaking | 3588 Hz | 1.07 | 16.6 dB  |
| Peaking | 4891 Hz | 0.86 | -13.9 dB |
| Peaking | 250 Hz  | 2.31 | 0.6 dB   |
| Peaking | 671 Hz  | 1.4  | 2.3 dB   |
| Peaking | 817 Hz  | 0.42 | -1.5 dB  |
| Peaking | 2522 Hz | 4.3  | 2.0 dB   |
| Peaking | 8442 Hz | 7.13 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cowin%20E7%20Wired%20NC%20off/Cowin%20E7%20Wired%20NC%20off.png)