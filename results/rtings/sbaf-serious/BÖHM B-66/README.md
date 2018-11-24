# BÖHM B-66

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.7; 25 0.9; 28 0.1; 31 -0.2; 34 -0.3; 37 -0.2; 41 -0.0; 45 0.0; 49 0.1; 54 0.2; 60 0.3; 66 0.3; 72 0.4; 79 0.3; 87 0.2; 96 0.0; 106 -0.2; 116 -0.5; 128 -0.8; 141 -1.0; 155 -1.1; 170 -1.2; 187 -1.2; 206 -1.2; 227 -1.2; 249 -1.2; 274 -1.1; 302 -1.0; 332 -0.9; 365 -0.4; 402 0.2; 442 1.2; 486 2.4; 535 3.5; 588 4.0; 647 3.9; 712 3.3; 783 2.3; 861 1.4; 947 0.5; 1042 -0.3; 1146 -0.5; 1261 -1.8; 1387 -3.5; 1526 -5.5; 1678 -6.6; 1846 -5.8; 2031 -4.3; 2234 -3.4; 2457 -1.3; 2703 -0.1; 2973 0.0; 3270 0.7; 3597 2.3; 3957 2.5; 4353 1.9; 4788 5.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.2; 8482 -2.5; 9330 -2.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BÖHM B-66 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BÖHM B-66 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 314 Hz  |  0.73 | -2.2 dB |
| Peaking | 601 Hz  |  1.36 | 5.5 dB  |
| Peaking | 1717 Hz |  2.01 | -7.3 dB |
| Peaking | 5706 Hz |  1.51 | 6.9 dB  |
| Peaking | 8587 Hz |  3.16 | -5.0 dB |
| Peaking | 17 Hz   |  2.58 | 3.5 dB  |
| Peaking | 76 Hz   |  3.06 | 0.5 dB  |
| Peaking | 2188 Hz | 13.4  | -1.1 dB |
| Peaking | 4105 Hz |  3    | 1.7 dB  |
| Peaking | 4308 Hz |  7.39 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/B%C3%96HM%20B-66/B%C3%96HM%20B-66.png)