# Grado SR60e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.5; 34 4.8; 37 4.0; 41 3.1; 45 2.3; 49 1.7; 54 1.0; 60 0.3; 66 -0.3; 72 -0.8; 79 -1.1; 87 -1.4; 96 -1.7; 106 -1.9; 116 -2.1; 128 -2.2; 141 -2.2; 155 -2.1; 170 -1.9; 187 -1.8; 206 -1.5; 227 -1.4; 249 -1.4; 274 -1.3; 302 -1.1; 332 -1.1; 365 -1.8; 402 -1.9; 442 -1.7; 486 -1.4; 535 -1.2; 588 -1.1; 647 -0.8; 712 -0.6; 783 -0.4; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.0; 1261 -0.3; 1387 -0.8; 1526 -1.6; 1678 -2.8; 1846 -6.5; 2031 -8.8; 2234 -7.8; 2457 -6.1; 2703 -4.4; 2973 -3.0; 3270 -2.4; 3597 -4.4; 3957 -5.8; 4353 -2.1; 4788 1.0; 5267 -0.5; 5793 -1.3; 6373 -4.4; 7010 -6.5; 7711 -7.2; 8482 -9.8; 9330 -12.2; 10263 -9.4; 11289 -3.1; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.72 | 7.7 dB   |
| Peaking | 90 Hz    | 0.29 | -2.8 dB  |
| Peaking | 2128 Hz  | 2.91 | -9.1 dB  |
| Peaking | 3842 Hz  | 6.78 | -5.0 dB  |
| Peaking | 9071 Hz  | 2.5  | -12.7 dB |
| Peaking | 450 Hz   | 3.17 | -0.8 dB  |
| Peaking | 1185 Hz  | 2    | 1.1 dB   |
| Peaking | 5027 Hz  | 2.89 | 5.7 dB   |
| Peaking | 5498 Hz  | 1.16 | -3.3 dB  |
| Peaking | 12561 Hz | 3.31 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Grado%20SR60e/Grado%20SR60e.png)