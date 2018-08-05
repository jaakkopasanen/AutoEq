# T-Peos Popular

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 -8.4; 22 -8.3; 23 -8.3; 25 -8.2; 26 -8.2; 28 -8.1; 30 -7.9; 32 -7.8; 35 -7.6; 37 -7.4; 40 -7.2; 42 -7.1; 45 -6.9; 49 -6.6; 52 -6.4; 56 -6.1; 59 -5.9; 64 -5.6; 68 -5.4; 73 -5.1; 78 -5.0; 83 -4.9; 89 -4.9; 95 -5.0; 102 -5.2; 109 -5.3; 117 -5.4; 125 -5.6; 134 -5.8; 143 -5.7; 153 -5.5; 164 -5.3; 175 -4.9; 188 -4.6; 201 -4.3; 215 -3.8; 230 -3.4; 246 -3.1; 263 -2.7; 282 -2.2; 301 -1.9; 323 -1.5; 345 -1.1; 369 -0.8; 395 -0.4; 423 -0.0; 452 0.3; 484 0.5; 518 0.7; 554 1.0; 593 1.4; 635 1.5; 679 1.4; 726 1.5; 777 1.6; 832 1.3; 890 0.9; 952 0.5; 1019 -0.3; 1090 -0.6; 1167 -0.1; 1248 -1.2; 1336 -2.2; 1429 -3.0; 1529 -4.2; 1636 -5.2; 1751 -6.0; 1873 -6.6; 2004 -7.0; 2145 -7.2; 2295 -6.4; 2455 -4.4; 2627 -2.0; 2811 0.3; 3008 2.8; 3219 4.3; 3444 5.4; 3685 5.3; 3943 4.2; 4219 1.6; 4514 -0.9; 4830 -3.5; 5168 -5.9; 5530 -6.0; 5917 -2.2; 6331 0.5; 6775 2.3; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -1.9; 9502 -2.9; 10167 -2.5; 10879 -0.7; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Popular ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.53 | -7.3 dB |
| Peaking | 41 Hz    | 0.5  | -5.0 dB |
| Peaking | 153 Hz   | 1.22 | -4.4 dB |
| Peaking | 2030 Hz  | 2.1  | -8.1 dB |
| Peaking | 3406 Hz  | 4.21 | 7.7 dB  |
| Peaking | 750 Hz   | 1.35 | 2.6 dB  |
| Peaking | 1623 Hz  | 0.73 | -1.5 dB |
| Peaking | 5264 Hz  | 3.57 | -6.9 dB |
| Peaking | 4953 Hz  | 0.53 | 2.2 dB  |
| Peaking | 39246 Hz | 2.54 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Popular/T-Peos%20Popular.png)