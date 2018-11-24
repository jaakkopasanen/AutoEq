# Grado SR125e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.6; 34 4.9; 37 4.2; 41 3.5; 45 2.8; 49 2.3; 54 1.7; 60 1.2; 66 0.7; 72 0.4; 79 0.1; 87 -0.2; 96 -0.5; 106 -0.7; 116 -0.9; 128 -1.0; 141 -1.1; 155 -1.2; 170 -1.2; 187 -1.1; 206 -0.9; 227 -0.5; 249 -0.3; 274 -0.4; 302 -0.9; 332 -0.9; 365 -0.8; 402 -0.8; 442 -0.8; 486 -0.8; 535 -0.8; 588 -0.6; 647 -0.5; 712 -0.3; 783 -0.2; 861 -0.1; 947 -0.0; 1042 0.0; 1146 -0.1; 1261 -0.4; 1387 -1.0; 1526 -1.8; 1678 -3.1; 1846 -7.1; 2031 -9.5; 2234 -8.6; 2457 -7.0; 2703 -5.3; 2973 -3.8; 3270 -3.1; 3597 -3.5; 3957 -5.8; 4353 -3.0; 4788 1.2; 5267 -1.3; 5793 -2.6; 6373 -4.3; 7010 -6.9; 7711 -6.6; 8482 -9.1; 9330 -12.2; 10263 -9.1; 11289 -2.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.71 | 6.5 dB   |
| Peaking | 121 Hz   | 0.5  | -1.5 dB  |
| Peaking | 2150 Hz  | 2.59 | -9.7 dB  |
| Peaking | 3905 Hz  | 6.33 | -4.4 dB  |
| Peaking | 9078 Hz  | 2.47 | -12.3 dB |
| Peaking | 1207 Hz  | 1.26 | 1.7 dB   |
| Peaking | 1682 Hz  | 0.3  | -0.8 dB  |
| Peaking | 4871 Hz  | 9.63 | 4.2 dB   |
| Peaking | 6848 Hz  | 8.08 | -3.1 dB  |
| Peaking | 12358 Hz | 3.89 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Grado%20SR125e/Grado%20SR125e.png)