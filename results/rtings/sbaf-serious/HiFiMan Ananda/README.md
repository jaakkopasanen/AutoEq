# HiFiMan Ananda

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.8; 25 4.5; 28 4.0; 31 3.5; 34 3.2; 37 2.9; 41 2.5; 45 2.1; 49 1.8; 54 1.6; 60 1.4; 66 1.2; 72 1.1; 79 1.1; 87 1.0; 96 0.9; 106 0.6; 116 0.3; 128 0.1; 141 -0.2; 155 -0.4; 170 -0.6; 187 -0.7; 206 -0.7; 227 -0.8; 249 -0.6; 274 -0.4; 302 0.1; 332 0.9; 365 0.6; 402 -0.2; 442 -0.6; 486 -0.5; 535 -0.6; 588 -1.0; 647 0.2; 712 1.4; 783 1.2; 861 0.3; 947 -0.6; 1042 0.7; 1146 2.6; 1261 2.4; 1387 1.6; 1526 2.2; 1678 2.8; 1846 2.3; 2031 1.6; 2234 1.4; 2457 0.0; 2703 -0.1; 2973 -0.7; 3270 0.8; 3597 1.5; 3957 1.1; 4353 -0.1; 4788 1.1; 5267 4.5; 5793 5.8; 6373 1.5; 7010 0.8; 7711 -0.7; 8482 -2.8; 9330 -0.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Ananda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Ananda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.76 | 5.0 dB  |
| Peaking | 82 Hz   | 3.72 | 0.6 dB  |
| Peaking | 1548 Hz | 1.7  | 2.6 dB  |
| Peaking | 5635 Hz | 5.38 | 6.5 dB  |
| Peaking | 8439 Hz | 5.65 | -3.1 dB |
| Peaking | 241 Hz  | 1.15 | -3.0 dB |
| Peaking | 354 Hz  | 0.8  | 3.7 dB  |
| Peaking | 475 Hz  | 1.69 | -3.1 dB |
| Peaking | 3542 Hz | 2.13 | -2.2 dB |
| Peaking | 3649 Hz | 5.14 | 3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/HiFiMan%20Ananda/HiFiMan%20Ananda.png)