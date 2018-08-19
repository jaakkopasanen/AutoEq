# HiSoundAudio Crystal

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.0; 22 -1.2; 23 -1.3; 25 -1.4; 26 -1.5; 28 -1.6; 30 -1.6; 32 -1.7; 35 -1.8; 37 -1.9; 40 -2.0; 42 -2.1; 45 -2.2; 49 -2.3; 52 -2.5; 56 -2.7; 59 -2.8; 64 -3.1; 68 -3.3; 73 -3.5; 78 -3.6; 83 -3.9; 89 -4.2; 95 -4.3; 102 -4.6; 109 -4.5; 117 -4.7; 125 -4.8; 134 -4.9; 143 -5.0; 153 -5.0; 164 -5.0; 175 -4.9; 188 -4.9; 201 -4.8; 215 -4.6; 230 -4.4; 246 -4.3; 263 -4.1; 282 -3.7; 301 -3.5; 323 -3.2; 345 -2.9; 369 -2.6; 395 -2.3; 423 -1.8; 452 -1.6; 484 -1.3; 518 -1.0; 554 -0.6; 593 -0.1; 635 0.2; 679 0.2; 726 0.4; 777 0.7; 832 0.6; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.4; 1167 -0.9; 1248 -1.5; 1336 -2.2; 1429 -3.0; 1529 -3.8; 1636 -4.4; 1751 -4.7; 1873 -4.6; 2004 -3.8; 2145 -2.6; 2295 -1.3; 2455 -0.1; 2627 5.0; 2811 5.7; 3008 2.0; 3219 -0.6; 3444 0.2; 3685 0.5; 3943 1.8; 4219 0.6; 4514 -0.9; 4830 -1.2; 5168 -1.3; 5530 -2.4; 5917 -4.3; 6331 -6.7; 6775 -5.9; 7249 -3.3; 7756 -0.6; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.7; 13327 -1.5; 14260 -1.6; 15258 -2.3; 16326 -3.1; 17469 -2.3; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.131995100421416dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 102 Hz   |  0.54 | -3.9 dB |
| Peaking | 225 Hz   |  1.09 | -2.7 dB |
| Peaking | 1787 Hz  |  2.46 | -5.2 dB |
| Peaking | 2740 Hz  |  7.12 | 7.6 dB  |
| Peaking | 6452 Hz  |  4.78 | -7.3 dB |
| Peaking | 26 Hz    |  1.75 | -0.6 dB |
| Peaking | 781 Hz   |  2.85 | 1.5 dB  |
| Peaking | 3968 Hz  | 10.51 | 2.2 dB  |
| Peaking | 8445 Hz  |  4.87 | 1.1 dB  |
| Peaking | 16190 Hz |  2.01 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Crystal/HiSoundAudio%20Crystal.png)