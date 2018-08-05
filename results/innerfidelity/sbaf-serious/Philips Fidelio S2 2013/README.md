# Philips Fidelio S2 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 10 -84; 20 -0.6; 22 -0.8; 23 -0.9; 25 -1.0; 26 -1.1; 28 -1.2; 30 -1.3; 32 -1.4; 35 -1.5; 37 -1.5; 40 -1.6; 42 -1.6; 45 -1.6; 49 -1.6; 52 -1.5; 56 -1.5; 59 -1.5; 64 -1.5; 68 -1.5; 73 -1.5; 78 -1.6; 83 -1.7; 89 -1.9; 95 -2.3; 102 -2.7; 109 -2.9; 117 -3.3; 125 -3.7; 134 -4.0; 143 -4.1; 153 -4.1; 164 -4.0; 175 -3.8; 188 -3.7; 201 -3.5; 215 -3.2; 230 -2.9; 246 -2.7; 263 -2.4; 282 -2.1; 301 -1.9; 323 -1.6; 345 -1.3; 369 -1.0; 395 -0.9; 423 -0.5; 452 -0.3; 484 -0.2; 518 -0.1; 554 0.3; 593 0.6; 635 0.7; 679 0.7; 726 0.8; 777 0.9; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.8; 1336 -1.3; 1429 -1.8; 1529 -2.2; 1636 -2.4; 1751 -2.3; 1873 -2.0; 2004 -1.6; 2145 -1.0; 2295 -0.3; 2455 0.7; 2627 1.5; 2811 2.3; 3008 3.3; 3219 3.8; 3444 3.9; 3685 2.8; 3943 1.0; 4219 -1.9; 4514 -4.6; 4830 -5.6; 5168 -4.5; 5530 -2.3; 5917 -0.2; 6331 0.7; 6775 1.1; 7249 0.9; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.6dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio S2 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.84 | -1.3 dB  |
| Peaking | 160 Hz  | 0.99 | -4.2 dB  |
| Peaking | 1875 Hz | 1.7  | -4.4 dB  |
| Peaking | 3670 Hz | 0.97 | 6.8 dB   |
| Peaking | 4712 Hz | 2.89 | -11.0 dB |
| Peaking | 721 Hz  | 2.09 | 1.2 dB   |
| Peaking | 1410 Hz | 4.6  | -0.7 dB  |
| Peaking | 9073 Hz | 2.65 | 0.3 dB   |
| Peaking | 6800 Hz | 3.72 | 1.7 dB   |
| Peaking | 8015 Hz | 1.31 | -1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20S2%202013/Philips%20Fidelio%20S2%202013.png)