# Grado SR225e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.2; 41 4.3; 45 3.6; 49 2.9; 54 2.3; 60 1.7; 66 1.1; 72 0.7; 79 0.4; 87 0.0; 96 -0.2; 106 -0.4; 116 -0.7; 128 -0.8; 141 -0.9; 155 -0.9; 170 -0.9; 187 -0.8; 206 -0.6; 227 -0.3; 249 -0.3; 274 -1.0; 302 -0.9; 332 -0.6; 365 -0.6; 402 -0.6; 442 -0.7; 486 -0.7; 535 -0.7; 588 -0.6; 647 -0.4; 712 -0.3; 783 -0.1; 861 -0.0; 947 0.0; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -1.0; 1526 -1.6; 1678 -2.6; 1846 -6.1; 2031 -9.1; 2234 -8.7; 2457 -7.0; 2703 -5.0; 2973 -3.6; 3270 -2.9; 3597 -0.8; 3957 0.1; 4353 -5.1; 4788 -3.6; 5267 -2.0; 5793 -2.9; 6373 -1.7; 7010 -0.6; 7711 -2.3; 8482 -6.4; 9330 -11.1; 10263 -12.7; 11289 -9.6; 12418 -5.4; 13660 -1.7; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.61 | 7.2 dB   |
| Peaking | 82 Hz    | 0.37 | -1.8 dB  |
| Peaking | 2197 Hz  | 2.43 | -9.4 dB  |
| Peaking | 9806 Hz  | 2.86 | -11.3 dB |
| Peaking | 11232 Hz | 3.46 | -4.8 dB  |
| Peaking | 1223 Hz  | 2.13 | 1.0 dB   |
| Peaking | 3932 Hz  | 6.59 | 5.5 dB   |
| Peaking | 4332 Hz  | 3.67 | -5.6 dB  |
| Peaking | 7211 Hz  | 7.62 | 2.4 dB   |
| Peaking | 14896 Hz | 4.29 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Grado%20SR225e/Grado%20SR225e.png)