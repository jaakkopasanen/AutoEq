# Audeze LCD-X sample 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.0; 25 3.8; 28 3.5; 31 3.1; 34 2.5; 37 1.3; 41 0.1; 45 -0.1; 49 0.1; 54 0.4; 60 0.5; 66 0.4; 72 0.2; 79 0.1; 87 -0.2; 96 -0.5; 106 -0.7; 116 -1.0; 128 -1.3; 141 -1.5; 155 -1.7; 170 -1.8; 187 -2.0; 206 -2.1; 227 -2.1; 249 -2.2; 274 -2.1; 302 -2.0; 332 -1.8; 365 -1.5; 402 -1.2; 442 -1.2; 486 -1.6; 535 -1.5; 588 -0.9; 647 -1.2; 712 -1.3; 783 -0.9; 861 -0.5; 947 0.2; 1042 0.1; 1146 0.2; 1261 0.1; 1387 -0.5; 1526 -0.6; 1678 -0.4; 1846 -0.4; 2031 -0.6; 2234 -0.5; 2457 0.4; 2703 2.4; 2973 4.3; 3270 5.4; 3597 6.0; 3957 5.5; 4353 1.6; 4788 -0.8; 5267 5.4; 5793 5.9; 6373 3.8; 7010 2.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.3; 16529 -3.0; 18182 -4.6; 20000 -6.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.26 | 4.3 dB  |
| Peaking | 254 Hz   | 0.52 | -2.1 dB |
| Peaking | 3463 Hz  | 3.32 | 6.6 dB  |
| Peaking | 5805 Hz  | 4.68 | 6.1 dB  |
| Peaking | 19331 Hz | 1.25 | -6.2 dB |
| Peaking | 71 Hz    | 3.47 | 0.5 dB  |
| Peaking | 1069 Hz  | 5.34 | 0.7 dB  |
| Peaking | 2054 Hz  | 3.76 | -1.2 dB |
| Peaking | 14018 Hz | 3.73 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X%20sample%203/Audeze%20LCD-X%20sample%203.png)