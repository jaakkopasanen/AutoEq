# Sennheiser HD 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.7; 41 5.1; 45 4.5; 49 4.0; 54 3.5; 60 2.8; 66 2.2; 72 1.6; 79 1.0; 87 0.4; 96 -0.1; 106 -0.6; 116 -1.0; 128 -1.4; 141 -1.7; 155 -1.9; 170 -2.0; 187 -2.0; 206 -1.8; 227 -1.6; 249 -1.4; 274 -1.2; 302 -1.1; 332 -1.2; 365 -1.2; 402 -1.1; 442 -1.1; 486 -1.2; 535 -1.1; 588 -1.0; 647 -0.9; 712 -0.7; 783 -0.7; 861 -0.7; 947 -0.4; 1042 -0.3; 1146 -0.9; 1261 -1.4; 1387 -2.1; 1526 -2.6; 1678 -3.0; 1846 -3.4; 2031 -3.8; 2234 -2.8; 2457 -2.5; 2703 -2.3; 2973 -2.7; 3270 -3.2; 3597 -2.8; 3957 -1.7; 4353 -0.2; 4788 0.2; 5267 1.0; 5793 1.8; 6373 0.1; 7010 -0.3; 7711 -0.0; 8482 -1.1; 9330 -0.4; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.3; 16529 0.0; 18182 -0.0; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.39 | 6.9 dB  |
| Peaking | 122 Hz  | 0.45 | -3.5 dB |
| Peaking | 1898 Hz | 1.61 | -3.4 dB |
| Peaking | 3364 Hz | 3.14 | -2.6 dB |
| Peaking | 5539 Hz | 4.89 | 2.1 dB  |
| Peaking | 289 Hz  | 1.75 | 0.7 dB  |
| Peaking | 415 Hz  | 0.7  | -0.5 dB |
| Peaking | 1010 Hz | 6.73 | 0.8 dB  |
| Peaking | 8719 Hz | 7.69 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)