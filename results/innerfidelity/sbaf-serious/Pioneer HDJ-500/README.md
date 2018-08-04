# Pioneer HDJ-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.7; 49 4.9; 52 4.4; 56 3.8; 59 3.5; 64 3.2; 68 3.2; 73 3.2; 78 3.0; 83 2.6; 89 2.6; 95 2.5; 102 2.2; 109 1.9; 117 1.6; 125 1.2; 134 0.8; 143 0.6; 153 0.3; 164 0.3; 175 0.2; 188 0.1; 201 0.0; 215 -0.1; 230 0.1; 246 0.4; 263 0.2; 282 0.3; 301 0.1; 323 0.0; 345 -0.1; 369 -0.6; 395 -0.4; 423 -0.0; 452 -0.1; 484 -0.4; 518 -0.7; 554 -0.8; 593 -0.7; 635 -0.7; 679 -0.7; 726 -0.7; 777 -0.6; 832 -0.4; 890 -0.3; 952 -0.2; 1019 0.0; 1090 0.4; 1167 0.9; 1248 1.4; 1336 1.5; 1429 1.9; 1529 2.4; 1636 2.8; 1751 3.5; 1873 4.6; 2004 5.6; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.7; 4830 0.4; 5168 -2.1; 5530 -2.0; 5917 0.1; 6331 -0.1; 6775 -1.6; 7249 0.9; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.5; 16326 -1.6; 17469 -1.2; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.49 | 6.3 dB  |
| Peaking | 917 Hz   | 0.68 | -2.2 dB |
| Peaking | 3323 Hz  | 0.54 | 8.1 dB  |
| Peaking | 5274 Hz  | 5.37 | -6.3 dB |
| Peaking | 41470 Hz | 0.84 | -3.5 dB |
| Peaking | 100 Hz   | 3.67 | 0.6 dB  |
| Peaking | 163 Hz   | 2.25 | -0.6 dB |
| Peaking | 2076 Hz  | 7.41 | 1.3 dB  |
| Peaking | 4395 Hz  | 9.21 | 2.7 dB  |
| Peaking | 16668 Hz | 2.97 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-500/Pioneer%20HDJ-500.png)