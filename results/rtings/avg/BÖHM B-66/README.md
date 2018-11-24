# BÖHM B-66

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 0.6; 28 -0.1; 31 -0.3; 34 -0.2; 37 -0.1; 41 0.2; 45 0.3; 49 0.4; 54 0.6; 60 0.6; 66 0.5; 72 0.4; 79 0.1; 87 -0.1; 96 -0.4; 106 -0.7; 116 -1.0; 128 -1.3; 141 -1.5; 155 -1.7; 170 -1.8; 187 -1.8; 206 -1.7; 227 -1.7; 249 -1.7; 274 -1.8; 302 -1.8; 332 -1.9; 365 -1.4; 402 -0.8; 442 0.1; 486 1.2; 535 2.3; 588 2.9; 647 2.9; 712 2.5; 783 1.9; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.7; 1261 -2.0; 1387 -3.5; 1526 -5.1; 1678 -6.2; 1846 -5.9; 2031 -4.8; 2234 -3.9; 2457 -1.8; 2703 -0.9; 2973 -1.5; 3270 -1.9; 3597 -0.9; 3957 0.1; 4353 0.6; 4788 3.4; 5267 3.4; 5793 2.9; 6373 2.3; 7010 0.3; 7711 -0.7; 8482 -2.0; 9330 -1.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BÖHM B-66 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BÖHM B-66 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 345 Hz  | 0.6  | -3.3 dB |
| Peaking | 611 Hz  | 1.18 | 5.4 dB  |
| Peaking | 1722 Hz | 1.99 | -6.4 dB |
| Peaking | 5373 Hz | 1.89 | 7.8 dB  |
| Peaking | 5554 Hz | 0.81 | -3.7 dB |
| Peaking | 60 Hz   | 2.22 | 0.9 dB  |
| Peaking | 2762 Hz | 5.97 | 2.1 dB  |
| Peaking | 3000 Hz | 3.06 | -1.4 dB |
| Peaking | 8619 Hz | 3.99 | -2.9 dB |
| Peaking | 9223 Hz | 1.38 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/B%C3%96HM%20B-66/B%C3%96HM%20B-66.png)