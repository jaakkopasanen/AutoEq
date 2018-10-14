# Audeze LCD-2 sn5325928

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.4; 25 4.4; 28 4.4; 31 4.4; 34 4.3; 37 4.2; 41 4.1; 45 4.0; 49 3.8; 54 3.6; 60 3.3; 66 3.1; 72 2.9; 79 2.7; 87 2.3; 96 2.0; 106 1.7; 116 1.5; 128 1.2; 141 1.0; 155 0.8; 170 0.7; 187 0.5; 206 0.4; 227 0.5; 249 0.3; 274 0.3; 302 0.4; 332 0.4; 365 0.3; 402 0.2; 442 0.2; 486 -0.0; 535 -0.1; 588 -0.2; 647 -0.4; 712 -0.2; 783 -0.1; 861 -0.3; 947 -0.2; 1042 0.2; 1146 0.0; 1261 0.1; 1387 -0.5; 1526 -1.0; 1678 -1.2; 1846 -0.2; 2031 0.3; 2234 0.9; 2457 2.0; 2703 2.6; 2973 3.5; 3270 4.8; 3597 6.0; 3957 6.0; 4353 4.9; 4788 4.1; 5267 5.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.2; 18182 -2.7; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sn5325928 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.38 | 4.5 dB  |
| Peaking | 1634 Hz  | 3.14 | -1.7 dB |
| Peaking | 3686 Hz  | 1.76 | 5.7 dB  |
| Peaking | 6097 Hz  | 2.54 | 6.6 dB  |
| Peaking | 7396 Hz  | 1.49 | -2.3 dB |
| Peaking | 749 Hz   | 1.65 | -0.4 dB |
| Peaking | 1163 Hz  | 3.27 | 0.3 dB  |
| Peaking | 18812 Hz | 1.79 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sn5325928/Audeze%20LCD-2%20sn5325928.png)