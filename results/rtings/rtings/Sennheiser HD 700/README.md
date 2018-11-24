# Sennheiser HD 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.3; 25 4.8; 28 4.2; 31 3.7; 34 3.3; 37 3.0; 41 2.7; 45 2.3; 49 1.9; 54 1.4; 60 0.9; 66 0.3; 72 -0.2; 79 -0.8; 87 -1.3; 96 -1.9; 106 -2.4; 116 -2.8; 128 -3.2; 141 -3.5; 155 -3.8; 170 -3.9; 187 -3.8; 206 -3.6; 227 -3.4; 249 -3.3; 274 -3.3; 302 -3.2; 332 -3.1; 365 -2.9; 402 -2.8; 442 -2.6; 486 -2.5; 535 -2.3; 588 -2.1; 647 -1.7; 712 -1.3; 783 -0.8; 861 -0.4; 947 -0.2; 1042 0.2; 1146 0.8; 1261 1.4; 1387 2.0; 1526 2.5; 1678 2.8; 1846 3.2; 2031 2.8; 2234 3.6; 2457 3.3; 2703 3.4; 2973 2.8; 3270 3.1; 3597 3.0; 3957 2.0; 4353 1.4; 4788 0.9; 5267 -1.3; 5793 -3.6; 6373 -9.1; 7010 -4.4; 7711 -1.6; 8482 -2.1; 9330 -0.7; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -4.1; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 1.76 | 1.2 dB   |
| Peaking | 20 Hz    | 0.31 | 5.5 dB   |
| Peaking | 177 Hz   | 0.3  | -4.3 dB  |
| Peaking | 2419 Hz  | 0.65 | 3.9 dB   |
| Peaking | 6420 Hz  | 4.1  | -10.0 dB |
| Peaking | 28 Hz    | 1.67 | -0.4 dB  |
| Peaking | 156 Hz   | 2.69 | -0.5 dB  |
| Peaking | 260 Hz   | 2.09 | 0.5 dB   |
| Peaking | 19329 Hz | 1.87 | -6.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)