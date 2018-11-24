# BÖHM B-66

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 0.6; 28 -0.1; 31 -0.3; 34 -0.2; 37 -0.1; 41 0.2; 45 0.3; 49 0.4; 54 0.6; 60 0.6; 66 0.5; 72 0.4; 79 0.1; 87 -0.1; 96 -0.4; 106 -0.7; 116 -1.0; 128 -1.3; 141 -1.5; 155 -1.7; 170 -1.8; 187 -1.8; 206 -1.7; 227 -1.7; 249 -1.7; 274 -1.8; 302 -1.8; 332 -1.9; 365 -1.4; 402 -0.8; 442 0.1; 486 1.2; 535 2.3; 588 2.9; 647 2.9; 712 2.5; 783 1.9; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.7; 1261 -2.0; 1387 -3.5; 1526 -5.1; 1678 -6.2; 1846 -5.9; 2031 -4.8; 2234 -3.9; 2457 -1.8; 2703 -0.7; 2973 -1.1; 3270 -1.1; 3597 0.1; 3957 1.3; 4353 1.9; 4788 5.2; 5267 5.9; 5793 5.4; 6373 3.6; 7010 1.0; 7711 -0.3; 8482 -2.9; 9330 -3.8; 10263 -0.4; 11289 0.0
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
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 359 Hz  | 0.6  | -3.6 dB |
| Peaking | 609 Hz  | 1.09 | 5.8 dB  |
| Peaking | 1744 Hz | 1.74 | -6.7 dB |
| Peaking | 5383 Hz | 2.53 | 6.9 dB  |
| Peaking | 8940 Hz | 4.31 | -4.8 dB |
| Peaking | 63 Hz   | 1.19 | 0.8 dB  |
| Peaking | 136 Hz  | 2.43 | -0.7 dB |
| Peaking | 2735 Hz | 6.8  | 1.2 dB  |
| Peaking | 3181 Hz | 6.26 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/B%C3%96HM%20B-66/B%C3%96HM%20B-66.png)