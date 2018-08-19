# HiSoundAudio Hiphone HP4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -10.0; 22 -10.0; 23 -10.1; 25 -10.1; 26 -10.1; 28 -10.2; 30 -10.2; 32 -10.2; 35 -10.2; 37 -10.3; 40 -10.3; 42 -10.3; 45 -10.4; 49 -10.4; 52 -10.5; 56 -10.6; 59 -10.6; 64 -10.7; 68 -10.8; 73 -10.9; 78 -11.1; 83 -11.2; 89 -11.3; 95 -11.4; 102 -11.4; 109 -11.3; 117 -11.2; 125 -11.2; 134 -11.1; 143 -11.0; 153 -10.9; 164 -10.7; 175 -10.4; 188 -10.1; 201 -9.8; 215 -9.5; 230 -9.1; 246 -8.7; 263 -8.4; 282 -7.8; 301 -7.4; 323 -6.9; 345 -6.4; 369 -6.0; 395 -5.4; 423 -4.8; 452 -4.3; 484 -3.9; 518 -3.4; 554 -2.8; 593 -2.1; 635 -1.7; 679 -1.3; 726 -0.8; 777 -0.3; 832 -0.2; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.4; 1336 0.5; 1429 0.8; 1529 1.2; 1636 1.5; 1751 1.8; 1873 2.3; 2004 2.7; 2145 1.9; 2295 0.9; 2455 1.8; 2627 2.9; 2811 3.7; 3008 5.1; 3219 5.7; 3444 6.0; 3685 5.9; 3943 5.1; 4219 3.4; 4514 2.0; 4830 1.4; 5168 1.0; 5530 -0.1; 5917 -2.0; 6331 -4.7; 6775 -4.0; 7249 -1.6; 7756 0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.6; 17469 -1.5; 18692 -0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999973023095dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Hiphone HP4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.21 | -9.6 dB |
| Peaking | 143 Hz   | 0.65 | -6.1 dB |
| Peaking | 306 Hz   | 1.13 | -3.3 dB |
| Peaking | 3409 Hz  | 1.45 | 6.0 dB  |
| Peaking | 6426 Hz  | 4.59 | -6.1 dB |
| Peaking | 485 Hz   | 5.89 | -0.6 dB |
| Peaking | 1991 Hz  | 1.8  | 2.2 dB  |
| Peaking | 2384 Hz  | 3.46 | -3.0 dB |
| Peaking | 3495 Hz  | 3.84 | 0.2 dB  |
| Peaking | 17081 Hz | 4.77 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Hiphone%20HP4/HiSoundAudio%20Hiphone%20HP4.png)