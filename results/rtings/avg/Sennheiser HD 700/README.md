# Sennheiser HD 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.3; 25 4.8; 28 4.2; 31 3.7; 34 3.3; 37 3.0; 41 2.7; 45 2.3; 49 1.9; 54 1.4; 60 0.9; 66 0.3; 72 -0.2; 79 -0.8; 87 -1.3; 96 -1.9; 106 -2.4; 116 -2.8; 128 -3.2; 141 -3.5; 155 -3.8; 170 -3.9; 187 -3.8; 206 -3.6; 227 -3.4; 249 -3.3; 274 -3.3; 302 -3.2; 332 -3.1; 365 -2.9; 402 -2.8; 442 -2.6; 486 -2.5; 535 -2.3; 588 -2.1; 647 -1.7; 712 -1.3; 783 -0.8; 861 -0.4; 947 -0.2; 1042 0.2; 1146 0.8; 1261 1.4; 1387 2.0; 1526 2.5; 1678 2.8; 1846 3.2; 2031 2.8; 2234 3.6; 2457 3.3; 2703 3.2; 2973 2.4; 3270 2.4; 3597 2.0; 3957 0.8; 4353 0.1; 4788 -0.8; 5267 -3.9; 5793 -6.1; 6373 -10.3; 7010 -5.3; 7711 -3.0; 8482 -2.8; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.9; 18182 -8.4; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 15 Hz   | 1.57 | 1.0 dB   |
| Peaking | 17 Hz   | 0.28 | 5.6 dB   |
| Peaking | 178 Hz  | 0.31 | -4.3 dB  |
| Peaking | 2238 Hz | 0.76 | 3.9 dB   |
| Peaking | 6313 Hz | 3.09 | -10.5 dB |
| Peaking | 62 Hz   | 2.87 | 0.4 dB   |
| Peaking | 280 Hz  | 3.26 | 0.4 dB   |
| Peaking | 3641 Hz | 3.37 | 0.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)