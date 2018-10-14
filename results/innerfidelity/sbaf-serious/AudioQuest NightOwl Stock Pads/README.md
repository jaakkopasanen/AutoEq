# AudioQuest NightOwl Stock Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.1; 25 -1.0; 28 -0.9; 31 -0.9; 34 -0.8; 37 -0.7; 41 -0.6; 45 -0.5; 49 -0.4; 54 -0.3; 60 -0.1; 66 -0.1; 72 -0.3; 79 -0.8; 87 -1.5; 96 -2.8; 106 -2.9; 116 -2.9; 128 -3.7; 141 -3.9; 155 -3.3; 170 -3.1; 187 -3.6; 206 -3.3; 227 -2.9; 249 -2.7; 274 -2.3; 302 -1.9; 332 -1.6; 365 -1.2; 402 -1.0; 442 -0.6; 486 -0.7; 535 -0.6; 588 -0.3; 647 -0.1; 712 0.3; 783 0.5; 861 0.0; 947 -0.0; 1042 0.0; 1146 0.4; 1261 0.9; 1387 1.2; 1526 1.8; 1678 3.1; 1846 4.6; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 5.8; 3597 5.4; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.4; 6373 2.7; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioQuest NightOwl Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.14 | -0.9 dB |
| Peaking | 68 Hz   | 1.61 | 2.2 dB  |
| Peaking | 135 Hz  | 0.79 | -2.0 dB |
| Peaking | 149 Hz  | 0.38 | -2.0 dB |
| Peaking | 3249 Hz | 0.74 | 6.8 dB  |
| Peaking | 1299 Hz | 1.88 | -1.1 dB |
| Peaking | 2018 Hz | 3.89 | 2.1 dB  |
| Peaking | 3420 Hz | 4.49 | -1.6 dB |
| Peaking | 5409 Hz | 2.84 | 2.6 dB  |
| Peaking | 8536 Hz | 1.6  | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioQuest%20NightOwl%20Stock%20Pads/AudioQuest%20NightOwl%20Stock%20Pads.png)