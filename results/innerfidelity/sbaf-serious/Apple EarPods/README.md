# Apple EarPods

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 5.8; 73 5.0; 78 4.1; 83 3.2; 89 2.4; 95 1.7; 102 1.1; 109 0.9; 117 0.6; 125 0.3; 134 0.3; 143 0.3; 153 0.3; 164 0.4; 175 0.5; 188 0.6; 201 0.7; 215 0.8; 230 1.1; 246 1.1; 263 1.1; 282 1.4; 301 1.4; 323 1.5; 345 1.6; 369 1.7; 395 1.7; 423 2.0; 452 2.0; 484 1.7; 518 1.7; 554 1.8; 593 2.0; 635 1.8; 679 1.6; 726 1.4; 777 1.3; 832 1.1; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -2.0; 1336 -3.2; 1429 -4.7; 1529 -6.2; 1636 -7.7; 1751 -9.0; 1873 -9.9; 2004 -10.4; 2145 -10.7; 2295 -10.6; 2455 -10.0; 2627 -9.2; 2811 -8.1; 3008 -5.9; 3219 -3.9; 3444 -2.1; 3685 -1.3; 3943 -1.5; 4219 -2.9; 4514 -4.0; 4830 -4.6; 5168 -4.9; 5530 -6.6; 5917 -8.0; 6331 -7.1; 6775 -5.6; 7249 -5.4; 7756 -5.8; 8299 -6.8; 8880 -7.9; 9502 -8.2; 10167 -6.3; 10879 -2.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.2; 15258 -1.4; 16326 -0.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple EarPods ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.66 | 7.0 dB   |
| Peaking | 657 Hz   | 0.75 | 2.6 dB   |
| Peaking | 2071 Hz  | 1.51 | -11.6 dB |
| Peaking | 7743 Hz  | 1.19 | -7.0 dB  |
| Peaking | 24000 Hz | 2.21 | -6.1 dB  |
| Peaking | 3778 Hz  | 3.48 | 4.8 dB   |
| Peaking | 6417 Hz  | 0.7  | -3.4 dB  |
| Peaking | 7412 Hz  | 3.44 | 5.1 dB   |
| Peaking | 9858 Hz  | 3.8  | -4.6 dB  |
| Peaking | 11364 Hz | 1.98 | 5.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20EarPods/Apple%20EarPods.png)