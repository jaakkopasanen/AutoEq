# Audio Technica ATH-CKM500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.2dB
GraphicEQ: 21 -2.7; 23 -3.3; 25 -3.8; 28 -4.4; 31 -4.9; 34 -5.4; 37 -5.8; 41 -6.4; 45 -6.8; 49 -7.3; 54 -7.8; 60 -8.3; 66 -8.8; 72 -9.3; 79 -9.8; 87 -10.3; 96 -10.7; 106 -11.0; 116 -11.2; 128 -11.5; 141 -11.7; 155 -11.7; 170 -11.7; 187 -11.6; 206 -11.4; 227 -11.0; 249 -10.7; 274 -10.2; 302 -9.6; 332 -9.0; 365 -8.2; 402 -7.4; 442 -6.4; 486 -5.6; 535 -4.6; 588 -3.3; 647 -2.3; 712 -1.5; 783 -0.5; 861 -0.1; 947 0.1; 1042 -0.0; 1146 -0.4; 1261 -1.2; 1387 -2.1; 1526 -3.1; 1678 -3.8; 1846 -4.2; 2031 -4.7; 2234 -5.3; 2457 -5.4; 2703 -5.8; 2973 -6.0; 3270 -5.4; 3597 -4.7; 3957 -4.6; 4353 -6.5; 4788 -7.7; 5267 -8.2; 5793 -9.4; 6373 -7.7; 7010 -6.0; 7711 -4.3; 8482 -4.0; 9330 -5.9; 10263 -7.4; 11289 -2.8; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.2dB` and instead set Global volume in the UI for both channels to **-2**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-CKM500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 97 Hz    | 0.41 | -9.7 dB |
| Peaking | 261 Hz   | 0.88 | -5.8 dB |
| Peaking | 2504 Hz  | 1.48 | -5.0 dB |
| Peaking | 5643 Hz  | 1.63 | -8.6 dB |
| Peaking | 10057 Hz | 4.78 | -6.6 dB |
| Peaking | 27 Hz    | 2.17 | -0.5 dB |
| Peaking | 474 Hz   | 2.18 | -1.5 dB |
| Peaking | 916 Hz   | 1.25 | 2.3 dB  |
| Peaking | 1596 Hz  | 2.76 | -1.7 dB |
| Peaking | 12404 Hz | 5.15 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-CKM500/Audio%20Technica%20ATH-CKM500.png)