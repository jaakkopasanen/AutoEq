# HiSoundAudio Wooduo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -14.3; 23 -14.3; 25 -14.3; 28 -14.2; 31 -14.2; 34 -14.1; 37 -14.1; 41 -14.0; 45 -14.0; 49 -13.9; 54 -13.9; 60 -13.9; 66 -13.8; 72 -13.9; 79 -13.9; 87 -13.9; 96 -13.9; 106 -13.7; 116 -13.4; 128 -13.2; 141 -12.9; 155 -12.6; 170 -12.2; 187 -11.6; 206 -11.1; 227 -10.4; 249 -9.9; 274 -9.1; 302 -8.4; 332 -7.7; 365 -6.9; 402 -6.1; 442 -5.2; 486 -4.5; 535 -3.8; 588 -2.8; 647 -2.1; 712 -1.4; 783 -1.6; 861 0.2; 947 0.2; 1042 -0.0; 1146 -0.0; 1261 -0.1; 1387 -0.6; 1526 -1.0; 1678 -1.2; 1846 -1.2; 2031 -1.1; 2234 -1.1; 2457 -0.9; 2703 -0.7; 2973 -0.5; 3270 -0.4; 3597 -0.7; 3957 -1.6; 4353 -4.1; 4788 -6.0; 5267 -8.3; 5793 -9.7; 6373 -4.4; 7010 -0.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.0; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.9dB` and instead set Global volume in the UI for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Wooduo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 0.35 | -12.7 dB |
| Peaking | 107 Hz  | 0.28 | -12.0 dB |
| Peaking | 210 Hz  | 1.13 | -0.7 dB  |
| Peaking | 855 Hz  | 1.53 | 2.3 dB   |
| Peaking | 5467 Hz | 3.62 | -10.3 dB |
| Peaking | 1964 Hz | 2.4  | -0.8 dB  |
| Peaking | 3623 Hz | 3.37 | 0.8 dB   |
| Peaking | 4442 Hz | 6.08 | -1.9 dB  |
| Peaking | 7374 Hz | 6.36 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Wooduo/HiSoundAudio%20Wooduo.png)