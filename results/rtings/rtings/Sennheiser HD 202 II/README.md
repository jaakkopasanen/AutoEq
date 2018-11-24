# Sennheiser HD 202 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.9; 25 3.3; 28 2.5; 31 1.8; 34 1.2; 37 0.7; 41 0.1; 45 -0.5; 49 -1.0; 54 -1.7; 60 -2.3; 66 -2.8; 72 -3.0; 79 -3.1; 87 -3.3; 96 -3.4; 106 -3.3; 116 -2.9; 128 -2.4; 141 -1.8; 155 -1.3; 170 -0.5; 187 0.4; 206 1.4; 227 2.5; 249 3.6; 274 4.6; 302 4.8; 332 3.8; 365 3.7; 402 3.6; 442 3.2; 486 2.5; 535 1.8; 588 1.2; 647 0.9; 712 0.8; 783 0.6; 861 0.4; 947 0.1; 1042 -0.1; 1146 -0.6; 1261 -0.9; 1387 -1.6; 1526 -1.8; 1678 -1.6; 1846 -1.1; 2031 -0.0; 2234 1.1; 2457 2.1; 2703 3.8; 2973 5.1; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.1; 13660 -1.3; 15026 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.82 | 5.3 dB  |
| Peaking | 65 Hz   | 1.06 | -1.3 dB |
| Peaking | 104 Hz  | 0.7  | -3.4 dB |
| Peaking | 297 Hz  | 1.23 | 5.6 dB  |
| Peaking | 4381 Hz | 1.3  | 7.1 dB  |
| Peaking | 1604 Hz | 1.96 | -2.9 dB |
| Peaking | 3078 Hz | 2.74 | 2.7 dB  |
| Peaking | 4279 Hz | 3.7  | -1.3 dB |
| Peaking | 6213 Hz | 3.02 | 4.9 dB  |
| Peaking | 7195 Hz | 1.2  | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20HD%20202%20II/Sennheiser%20HD%20202%20II.png)