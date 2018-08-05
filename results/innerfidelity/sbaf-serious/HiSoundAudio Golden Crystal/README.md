# HiSoundAudio Golden Crystal

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 10 -84; 20 -7.7; 22 -7.7; 23 -7.7; 25 -7.6; 26 -7.6; 28 -7.5; 30 -7.4; 32 -7.3; 35 -7.1; 37 -7.0; 40 -6.9; 42 -6.8; 45 -6.7; 49 -6.5; 52 -6.3; 56 -6.1; 59 -6.0; 64 -5.8; 68 -5.7; 73 -5.5; 78 -5.5; 83 -5.5; 89 -5.5; 95 -5.8; 102 -6.0; 109 -6.2; 117 -6.4; 125 -6.7; 134 -6.9; 143 -6.9; 153 -6.8; 164 -6.6; 175 -6.3; 188 -6.0; 201 -5.8; 215 -5.3; 230 -4.9; 246 -4.6; 263 -4.3; 282 -3.9; 301 -3.5; 323 -3.1; 345 -2.8; 369 -2.4; 395 -2.0; 423 -1.6; 452 -1.3; 484 -1.0; 518 -0.7; 554 -0.3; 593 0.1; 635 0.4; 679 0.4; 726 0.5; 777 0.8; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.1; 1336 -1.1; 1429 -2.0; 1529 -2.2; 1636 -2.8; 1751 -3.4; 1873 -3.6; 2004 -3.6; 2145 -2.4; 2295 0.4; 2455 2.7; 2627 2.0; 2811 0.6; 3008 1.0; 3219 1.6; 3444 2.3; 3685 2.6; 3943 2.5; 4219 1.5; 4514 0.6; 4830 0.5; 5168 0.6; 5530 0.0; 5917 -1.7; 6331 -5.0; 6775 -8.0; 7249 -8.0; 7756 -6.2; 8299 -3.9; 8880 -2.6; 9502 -3.1; 10167 -4.6; 10879 -4.5; 11640 -1.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -2.3; 17469 -4.3; 18692 -2.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.4dB` and instead set Global volume in the UI for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Golden Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 9 Hz     | 0.76 | -7.1 dB |
| Peaking | 31 Hz    | 0.38 | -6.1 dB |
| Peaking | 166 Hz   | 0.85 | -5.5 dB |
| Peaking | 1796 Hz  | 4.58 | -4.1 dB |
| Peaking | 7267 Hz  | 3.45 | -8.7 dB |
| Peaking | 742 Hz   | 3.16 | 1.4 dB  |
| Peaking | 3435 Hz  | 1.93 | 1.6 dB  |
| Peaking | 3981 Hz  | 2.05 | 1.5 dB  |
| Peaking | 10501 Hz | 5.79 | -4.6 dB |
| Peaking | 30296 Hz | 3.13 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Golden%20Crystal/HiSoundAudio%20Golden%20Crystal.png)