# Sennheiser HD 598

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.0; 41 4.2; 45 3.5; 49 2.8; 54 2.0; 60 1.3; 66 0.7; 72 0.3; 79 -0.1; 87 -0.6; 96 -1.0; 106 -1.6; 116 -2.1; 128 -2.5; 141 -2.8; 155 -2.9; 170 -3.0; 187 -3.0; 206 -2.8; 227 -2.6; 249 -2.4; 274 -2.1; 302 -1.8; 332 -1.5; 365 -1.2; 402 -0.9; 442 -0.7; 486 -0.7; 535 -0.4; 588 0.3; 647 0.3; 712 0.3; 783 0.1; 861 -0.0; 947 -0.0; 1042 0.1; 1146 0.4; 1261 0.3; 1387 -0.1; 1526 -0.3; 1678 -0.3; 1846 -0.1; 2031 -0.3; 2234 -0.7; 2457 -0.6; 2703 -0.3; 2973 0.3; 3270 0.3; 3597 0.4; 3957 -1.0; 4353 -3.3; 4788 -1.0; 5267 2.0; 5793 2.5; 6373 3.5; 7010 2.5; 7711 0.3; 8482 -1.7; 9330 -3.4; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.78 | 6.6 dB  |
| Peaking | 162 Hz  | 0.78 | -3.4 dB |
| Peaking | 4393 Hz | 6.35 | -4.5 dB |
| Peaking | 6262 Hz | 2.17 | 3.8 dB  |
| Peaking | 8983 Hz | 5.45 | -4.7 dB |
| Peaking | 650 Hz  | 3.82 | 0.8 dB  |
| Peaking | 1185 Hz | 5.03 | 0.6 dB  |
| Peaking | 2649 Hz | 1.57 | -1.2 dB |
| Peaking | 3113 Hz | 2.37 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)