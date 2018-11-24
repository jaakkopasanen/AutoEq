# RHA T20 Bass Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 -5.2; 23 -5.4; 25 -5.6; 28 -5.8; 31 -6.0; 34 -6.1; 37 -6.2; 41 -6.3; 45 -6.3; 49 -6.3; 54 -6.3; 60 -6.3; 66 -6.3; 72 -6.4; 79 -6.4; 87 -6.4; 96 -6.4; 106 -6.2; 116 -6.0; 128 -5.9; 141 -5.6; 155 -5.4; 170 -5.0; 187 -4.6; 206 -4.2; 227 -3.7; 249 -3.3; 274 -2.8; 302 -2.3; 332 -1.8; 365 -1.4; 402 -1.0; 442 -0.4; 486 -0.2; 535 0.2; 588 0.8; 647 1.0; 712 1.0; 783 1.2; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.8; 1261 -1.7; 1387 -3.2; 1526 -4.0; 1678 -3.0; 1846 0.0; 2031 -2.0; 2234 -2.4; 2457 -2.5; 2703 -2.3; 2973 -1.1; 3270 -0.1; 3597 -0.5; 3957 -3.0; 4353 -7.0; 4788 -6.2; 5267 -0.6; 5793 4.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.0; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA T20 Bass Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Bass Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.36 | -6.1 dB |
| Peaking | 148 Hz  | 0.89 | -3.2 dB |
| Peaking | 1521 Hz | 3.65 | -4.1 dB |
| Peaking | 4558 Hz | 4.18 | -8.8 dB |
| Peaking | 6137 Hz | 4.09 | 7.1 dB  |
| Peaking | 274 Hz  | 2.13 | -0.7 dB |
| Peaking | 714 Hz  | 1.49 | 1.8 dB  |
| Peaking | 1853 Hz | 8.38 | 2.9 dB  |
| Peaking | 2407 Hz | 1.52 | -2.6 dB |
| Peaking | 3381 Hz | 4.01 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Bass%20Filter/RHA%20T20%20Bass%20Filter.png)