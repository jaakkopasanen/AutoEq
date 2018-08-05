# NarMoo W1M

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.3; 22 -5.4; 23 -5.4; 25 -5.4; 26 -5.4; 28 -5.4; 30 -5.3; 32 -5.2; 35 -5.1; 37 -5.0; 40 -4.9; 42 -4.8; 45 -4.7; 49 -4.5; 52 -4.3; 56 -4.1; 59 -4.0; 64 -3.8; 68 -3.6; 73 -3.5; 78 -3.4; 83 -3.5; 89 -3.5; 95 -3.8; 102 -4.0; 109 -4.3; 117 -4.5; 125 -4.8; 134 -5.1; 143 -5.2; 153 -5.1; 164 -5.1; 175 -4.8; 188 -4.7; 201 -4.5; 215 -4.2; 230 -4.0; 246 -3.8; 263 -3.6; 282 -3.3; 301 -3.1; 323 -2.9; 345 -2.7; 369 -2.5; 395 -2.4; 423 -2.1; 452 -1.9; 484 -1.8; 518 -1.7; 554 -1.4; 593 -1.0; 635 -0.8; 679 -0.8; 726 -0.6; 777 -0.3; 832 -0.3; 890 -0.2; 952 -0.1; 1019 0.2; 1090 0.4; 1167 0.6; 1248 0.9; 1336 1.2; 1429 1.4; 1529 1.6; 1636 1.7; 1751 2.1; 1873 2.5; 2004 2.8; 2145 2.8; 2295 2.9; 2455 3.0; 2627 3.4; 2811 4.1; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.0; 4830 3.3; 5168 4.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo W1M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.59 | -5.3 dB |
| Peaking | 173 Hz   | 0.58 | -4.5 dB |
| Peaking | 3452 Hz  | 1.13 | 6.0 dB  |
| Peaking | 5969 Hz  | 4.57 | 4.4 dB  |
| Peaking | 26196 Hz | 0.86 | -0.7 dB |
| Peaking | 84 Hz    | 4.35 | 0.5 dB  |
| Peaking | 2382 Hz  | 1.22 | 1.7 dB  |
| Peaking | 2556 Hz  | 2.8  | -2.5 dB |
| Peaking | 6653 Hz  | 8.14 | 2.0 dB  |
| Peaking | 7826 Hz  | 1.86 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20W1M/NarMoo%20W1M.png)