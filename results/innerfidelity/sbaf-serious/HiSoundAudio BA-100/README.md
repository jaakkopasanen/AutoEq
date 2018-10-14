# HiSoundAudio BA-100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 0.0; 23 3.5; 25 3.4; 28 3.3; 31 3.2; 34 3.1; 37 3.0; 41 2.8; 45 2.6; 49 2.4; 54 2.2; 60 1.8; 66 1.5; 72 1.2; 79 0.8; 87 0.4; 96 -0.0; 106 -0.3; 116 -0.6; 128 -0.9; 141 -1.3; 155 -1.5; 170 -1.7; 187 -1.7; 206 -1.9; 227 -1.8; 249 -1.9; 274 -1.8; 302 -1.7; 332 -1.6; 365 -1.4; 402 -1.2; 442 -0.9; 486 -0.8; 535 -0.5; 588 0.0; 647 0.2; 712 0.2; 783 0.6; 861 0.4; 947 0.2; 1042 -0.0; 1146 -0.3; 1261 -0.6; 1387 -1.1; 1526 -1.6; 1678 -1.9; 1846 -1.4; 2031 0.1; 2234 2.3; 2457 4.1; 2703 3.7; 2973 1.7; 3270 -0.5; 3597 0.1; 3957 0.7; 4353 -1.3; 4788 -3.3; 5267 -2.0; 5793 2.1; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio BA-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.02 | 3.8 dB  |
| Peaking | 1701 Hz | 2.5  | -2.5 dB |
| Peaking | 2501 Hz | 3.66 | 5.0 dB  |
| Peaking | 4956 Hz | 4.78 | -4.4 dB |
| Peaking | 6378 Hz | 5.13 | 5.8 dB  |
| Peaking | 62 Hz   | 1.37 | 1.3 dB  |
| Peaking | 224 Hz  | 0.62 | -2.0 dB |
| Peaking | 608 Hz  | 4.17 | 0.5 dB  |
| Peaking | 823 Hz  | 2.5  | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20BA-100/HiSoundAudio%20BA-100.png)