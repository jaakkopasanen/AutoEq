# Sennheiser HD 201

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.9; 87 5.7; 96 5.5; 106 5.3; 116 5.0; 128 4.8; 141 4.7; 155 4.7; 170 4.8; 187 4.7; 206 4.6; 227 4.8; 249 5.1; 274 5.3; 302 3.9; 332 3.4; 365 2.9; 402 2.3; 442 1.8; 486 1.4; 535 1.3; 588 1.5; 647 1.8; 712 1.6; 783 1.0; 861 0.4; 947 0.1; 1042 -0.1; 1146 -0.1; 1261 0.3; 1387 -0.3; 1526 -1.7; 1678 1.6; 1846 -0.5; 2031 -0.8; 2234 -0.3; 2457 1.2; 2703 2.6; 2973 2.8; 3270 2.6; 3597 3.0; 3957 4.6; 4353 6.0; 4788 6.0; 5267 4.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.1; 9330 -1.3; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 201 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.21 | 5.3 dB  |
| Peaking | 121 Hz  | 0.36 | 3.4 dB  |
| Peaking | 264 Hz  | 2.18 | 2.3 dB  |
| Peaking | 4420 Hz | 2.16 | 5.8 dB  |
| Peaking | 6062 Hz | 4.64 | 4.5 dB  |
| Peaking | 691 Hz  | 3.63 | 1.4 dB  |
| Peaking | 1114 Hz | 0.8  | -0.7 dB |
| Peaking | 2096 Hz | 6.22 | -1.5 dB |
| Peaking | 2788 Hz | 5.14 | 2.1 dB  |
| Peaking | 8891 Hz | 5.43 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)