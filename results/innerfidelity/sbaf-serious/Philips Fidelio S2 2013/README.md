# Philips Fidelio S2 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 10 -84; 20 -0.6; 22 -0.9; 23 -1.0; 25 -1.1; 26 -1.2; 28 -1.4; 30 -1.5; 32 -1.6; 35 -1.7; 37 -1.8; 40 -2.0; 42 -2.1; 45 -2.2; 49 -2.3; 52 -2.4; 56 -2.5; 59 -2.6; 64 -2.8; 68 -2.9; 73 -3.1; 78 -3.2; 83 -3.4; 89 -3.5; 95 -3.7; 102 -3.7; 109 -3.7; 117 -3.6; 125 -3.7; 134 -3.7; 143 -3.6; 153 -3.6; 164 -3.5; 175 -3.3; 188 -3.2; 201 -3.0; 215 -2.8; 230 -2.6; 246 -2.4; 263 -2.2; 282 -1.9; 301 -1.7; 323 -1.4; 345 -1.1; 369 -1.0; 395 -0.8; 423 -0.5; 452 -0.3; 484 -0.2; 518 -0.0; 554 0.3; 593 0.7; 635 0.7; 679 0.7; 726 0.8; 777 0.9; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.8; 1336 -1.3; 1429 -1.8; 1529 -2.2; 1636 -2.4; 1751 -2.3; 1873 -2.0; 2004 -1.6; 2145 -1.0; 2295 -0.3; 2455 0.7; 2627 1.5; 2811 2.3; 3008 3.3; 3219 3.8; 3444 3.9; 3685 2.8; 3943 1.0; 4219 -1.9; 4514 -4.6; 4830 -5.6; 5168 -4.5; 5530 -2.3; 5917 -0.2; 6331 0.7; 6775 1.1; 7249 0.9; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.1057614672645055dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio S2 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.5dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 79 Hz   | 0.56 | -2.9 dB  |
| Peaking | 175 Hz  | 1.1  | -2.1 dB  |
| Peaking | 1882 Hz | 1.71 | -4.3 dB  |
| Peaking | 3716 Hz | 0.98 | 6.9 dB   |
| Peaking | 4680 Hz | 2.89 | -11.1 dB |
| Peaking | 720 Hz  | 2.08 | 1.2 dB   |
| Peaking | 1412 Hz | 4.43 | -0.7 dB  |
| Peaking | 5344 Hz | 5.02 | -2.0 dB  |
| Peaking | 6495 Hz | 1.38 | 2.2 dB   |
| Peaking | 7993 Hz | 1.31 | -1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20S2%202013/Philips%20Fidelio%20S2%202013.png)