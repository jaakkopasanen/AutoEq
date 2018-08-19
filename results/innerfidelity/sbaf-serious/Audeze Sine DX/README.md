# Audeze SINE DX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.8; 40 5.8; 42 5.8; 45 5.8; 49 5.8; 52 5.7; 56 5.5; 59 5.4; 64 5.2; 68 5.1; 73 4.9; 78 4.8; 83 4.6; 89 4.4; 95 4.2; 102 4.0; 109 3.9; 117 3.8; 125 3.6; 134 3.4; 143 3.3; 153 3.2; 164 3.0; 175 3.0; 188 3.1; 201 3.0; 215 3.0; 230 3.0; 246 2.9; 263 2.7; 282 2.8; 301 2.7; 323 2.7; 345 2.7; 369 2.6; 395 2.5; 423 2.6; 452 2.4; 484 2.2; 518 2.1; 554 2.3; 593 2.5; 635 2.6; 679 2.3; 726 2.0; 777 1.7; 832 1.3; 890 0.8; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.2; 1248 -1.8; 1336 -1.8; 1429 -2.6; 1529 -3.7; 1636 -3.4; 1751 -2.6; 1873 -1.1; 2004 0.5; 2145 2.3; 2295 3.5; 2455 4.6; 2627 4.9; 2811 5.4; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.5; 20000 -2.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze SINE DX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.37 | 4.9 dB  |
| Peaking | 67 Hz   | 0.48 | 3.0 dB  |
| Peaking | 408 Hz  | 0.46 | 2.2 dB  |
| Peaking | 1556 Hz | 1.84 | -6.5 dB |
| Peaking | 3595 Hz | 0.79 | 7.2 dB  |
| Peaking | 1846 Hz | 5.7  | -0.7 dB |
| Peaking | 2366 Hz | 3.14 | 1.1 dB  |
| Peaking | 3692 Hz | 3.25 | -0.9 dB |
| Peaking | 6230 Hz | 2.32 | 5.5 dB  |
| Peaking | 7364 Hz | 1.42 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20SINE%20DX/Audeze%20SINE%20DX.png)