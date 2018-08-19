# HiSoundAudio Golden Crystal

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 10 -84; 20 -7.8; 22 -7.8; 23 -7.8; 25 -7.7; 26 -7.7; 28 -7.7; 30 -7.6; 32 -7.5; 35 -7.4; 37 -7.4; 40 -7.3; 42 -7.3; 45 -7.3; 49 -7.2; 52 -7.2; 56 -7.1; 59 -7.1; 64 -7.1; 68 -7.1; 73 -7.1; 78 -7.1; 83 -7.1; 89 -7.1; 95 -7.2; 102 -7.1; 109 -6.9; 117 -6.8; 125 -6.7; 134 -6.6; 143 -6.4; 153 -6.2; 164 -6.1; 175 -5.8; 188 -5.5; 201 -5.3; 215 -5.0; 230 -4.6; 246 -4.3; 263 -4.1; 282 -3.7; 301 -3.3; 323 -3.0; 345 -2.6; 369 -2.3; 395 -2.0; 423 -1.5; 452 -1.2; 484 -1.0; 518 -0.7; 554 -0.3; 593 0.2; 635 0.4; 679 0.4; 726 0.5; 777 0.8; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.1; 1336 -1.1; 1429 -2.0; 1529 -2.2; 1636 -2.8; 1751 -3.4; 1873 -3.6; 2004 -3.6; 2145 -2.4; 2295 0.4; 2455 2.7; 2627 2.0; 2811 0.6; 3008 1.0; 3219 1.6; 3444 2.3; 3685 2.6; 3943 2.5; 4219 1.5; 4514 0.6; 4830 0.5; 5168 0.6; 5530 0.0; 5917 -1.7; 6331 -5.0; 6775 -8.0; 7249 -8.0; 7756 -6.2; 8299 -3.9; 8880 -2.6; 9502 -3.1; 10167 -4.6; 10879 -4.5; 11640 -1.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -2.3; 17469 -4.3; 18692 -2.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.946748066830759dB` and instead set Global volume in the UI for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Golden Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.2dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 24 Hz    |  0.2  | -7.5 dB |
| Peaking | 164 Hz   |  0.78 | -3.3 dB |
| Peaking | 1798 Hz  |  4.64 | -4.1 dB |
| Peaking | 7252 Hz  |  3.6  | -8.7 dB |
| Peaking | 17695 Hz |  2.63 | -4.6 dB |
| Peaking | 740 Hz   |  3.11 | 1.4 dB  |
| Peaking | 2501 Hz  | 10.02 | 3.1 dB  |
| Peaking | 3796 Hz  |  2.85 | 3.1 dB  |
| Peaking | 10649 Hz |  3.67 | -6.0 dB |
| Peaking | 11829 Hz |  1.58 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Golden%20Crystal/HiSoundAudio%20Golden%20Crystal.png)