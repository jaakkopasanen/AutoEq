# Audeze SINE DX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.9; 42 5.9; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.8; 64 5.8; 68 5.7; 73 5.6; 78 5.6; 83 5.4; 89 5.2; 95 5.0; 102 4.6; 109 4.3; 117 4.0; 125 3.6; 134 3.3; 143 3.1; 153 2.9; 164 2.8; 175 2.8; 188 2.9; 201 2.8; 215 2.9; 230 2.9; 246 2.8; 263 2.7; 282 2.7; 301 2.7; 323 2.6; 345 2.7; 369 2.6; 395 2.5; 423 2.5; 452 2.4; 484 2.2; 518 2.1; 554 2.3; 593 2.5; 635 2.6; 679 2.3; 726 2.0; 777 1.7; 832 1.3; 890 0.8; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.2; 1248 -1.8; 1336 -1.8; 1429 -2.6; 1529 -3.7; 1636 -3.4; 1751 -2.6; 1873 -1.1; 2004 0.5; 2145 2.3; 2295 3.5; 2455 4.6; 2627 4.9; 2811 5.4; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.5; 20000 -2.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze SINE DX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.33 | 5.7 dB  |
| Peaking | 78 Hz   | 0.87 | 2.6 dB  |
| Peaking | 405 Hz  | 0.48 | 2.3 dB  |
| Peaking | 1557 Hz | 1.85 | -6.5 dB |
| Peaking | 3597 Hz | 0.79 | 7.2 dB  |
| Peaking | 1844 Hz | 5.7  | -0.7 dB |
| Peaking | 2362 Hz | 3.07 | 1.1 dB  |
| Peaking | 3694 Hz | 3.24 | -0.9 dB |
| Peaking | 6235 Hz | 2.32 | 5.6 dB  |
| Peaking | 7354 Hz | 1.42 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20SINE%20DX/Audeze%20SINE%20DX.png)