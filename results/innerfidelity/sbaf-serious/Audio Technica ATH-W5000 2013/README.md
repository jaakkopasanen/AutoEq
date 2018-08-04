# Audio Technica ATH-W5000 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.6; 59 5.0; 64 4.1; 68 4.0; 73 3.9; 78 3.4; 83 2.5; 89 1.5; 95 1.0; 102 0.5; 109 0.2; 117 -0.0; 125 -0.4; 134 -0.6; 143 -0.7; 153 -0.8; 164 -0.6; 175 -0.4; 188 -0.5; 201 -0.4; 215 -0.4; 230 -0.1; 246 -0.0; 263 -0.2; 282 -0.0; 301 0.1; 323 0.6; 345 1.1; 369 1.5; 395 2.0; 423 3.1; 452 4.3; 484 4.9; 518 5.2; 554 5.3; 593 4.9; 635 3.9; 679 3.2; 726 2.5; 777 2.3; 832 1.7; 890 0.9; 952 0.4; 1019 -0.1; 1090 -0.6; 1167 -0.9; 1248 -1.2; 1336 -1.4; 1429 -1.7; 1529 -2.0; 1636 -1.4; 1751 -0.7; 1873 -0.6; 2004 -1.1; 2145 -1.3; 2295 0.2; 2455 2.5; 2627 4.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 3.7; 4219 1.5; 4514 1.2; 4830 1.0; 5168 3.7; 5530 5.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.0; 9502 -1.8; 10167 -1.1; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W5000 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.43 | 8.2 dB  |
| Peaking | 546 Hz   | 0.89 | 9.5 dB  |
| Peaking | 626 Hz   | 0.08 | -4.9 dB |
| Peaking | 3124 Hz  | 1.81 | 10.3 dB |
| Peaking | 6001 Hz  | 3.08 | 8.0 dB  |
| Peaking | 214 Hz   | 4    | 0.8 dB  |
| Peaking | 9505 Hz  | 5.05 | -2.1 dB |
| Peaking | 9023 Hz  | 2.77 | 0.3 dB  |
| Peaking | 11530 Hz | 1.26 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-W5000%202013/Audio%20Technica%20ATH-W5000%202013.png)