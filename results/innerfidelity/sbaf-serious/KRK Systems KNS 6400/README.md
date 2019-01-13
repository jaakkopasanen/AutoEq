# KRK Systems KNS 6400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.6; 28 5.3; 31 5.0; 34 4.9; 37 4.8; 41 5.0; 45 5.3; 49 5.7; 54 6.0; 60 6.0; 66 6.0; 72 5.8; 79 4.2; 87 2.4; 96 1.5; 106 1.1; 116 0.0; 128 -0.7; 141 -1.0; 155 -1.1; 170 -1.6; 187 -2.3; 206 -2.1; 227 -2.2; 249 -1.7; 274 -1.5; 302 -2.1; 332 -2.1; 365 -2.1; 402 -1.8; 442 -1.3; 486 -1.7; 535 -2.1; 588 -2.3; 647 -1.1; 712 0.0; 783 -0.2; 861 -0.3; 947 -0.0; 1042 -0.1; 1146 -0.5; 1261 -0.6; 1387 -0.7; 1526 -1.7; 1678 -2.4; 1846 -3.6; 2031 -3.8; 2234 -3.7; 2457 -4.2; 2703 -4.0; 2973 -2.1; 3270 -2.6; 3597 -0.7; 3957 0.1; 4353 1.5; 4788 3.4; 5267 4.6; 5793 3.2; 6373 1.7; 7010 1.6; 7711 0.3; 8482 -0.4; 9330 -2.3; 10263 -1.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.1; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK Systems KNS 6400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 6400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.45 | 5.8 dB  |
| Peaking | 65 Hz   | 1.44 | 5.3 dB  |
| Peaking | 209 Hz  | 0.5  | -2.6 dB |
| Peaking | 2384 Hz | 1.54 | -4.5 dB |
| Peaking | 5204 Hz | 3.15 | 5.4 dB  |
| Peaking | 575 Hz  | 4.05 | -1.9 dB |
| Peaking | 802 Hz  | 1.17 | 1.0 dB  |
| Peaking | 1814 Hz | 7.84 | -1.2 dB |
| Peaking | 7071 Hz | 5.53 | 0.8 dB  |
| Peaking | 9584 Hz | 5.07 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KRK%20Systems%20KNS%206400/KRK%20Systems%20KNS%206400.png)