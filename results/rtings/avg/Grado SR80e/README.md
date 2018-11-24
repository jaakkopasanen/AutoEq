# Grado SR80e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.3; 37 4.6; 41 3.7; 45 2.9; 49 2.3; 54 1.6; 60 0.9; 66 0.3; 72 -0.1; 79 -0.5; 87 -0.8; 96 -1.1; 106 -1.4; 116 -1.5; 128 -1.6; 141 -1.6; 155 -1.6; 170 -1.5; 187 -1.5; 206 -1.3; 227 -1.1; 249 -0.9; 274 -0.9; 302 -1.0; 332 -1.1; 365 -1.0; 402 -1.1; 442 -1.1; 486 -1.1; 535 -1.1; 588 -0.9; 647 -0.7; 712 -0.4; 783 -0.2; 861 0.0; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.4; 1387 -0.9; 1526 -1.6; 1678 -2.9; 1846 -6.8; 2031 -9.3; 2234 -8.1; 2457 -6.3; 2703 -4.8; 2973 -3.5; 3270 -3.0; 3597 -3.8; 3957 -5.6; 4353 -3.4; 4788 -0.8; 5267 -2.1; 5793 -3.0; 6373 -5.2; 7010 -7.1; 7711 -5.9; 8482 -6.7; 9330 -7.4; 10263 -4.2; 11289 -1.6; 12418 -2.2; 13660 -2.0; 15026 -0.9; 16529 -0.6; 18182 -0.4; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR80e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR80e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.64 | 7.4 dB  |
| Peaking | 89 Hz    | 0.36 | -2.6 dB |
| Peaking | 2121 Hz  | 2.85 | -8.9 dB |
| Peaking | 6947 Hz  | 0.68 | -3.7 dB |
| Peaking | 8822 Hz  | 2.81 | -4.2 dB |
| Peaking | 1195 Hz  | 2.27 | 1.0 dB  |
| Peaking | 4046 Hz  | 4.44 | -4.5 dB |
| Peaking | 4730 Hz  | 3.24 | 3.9 dB  |
| Peaking | 6803 Hz  | 8.56 | -2.8 dB |
| Peaking | 11151 Hz | 9.5  | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR80e/Grado%20SR80e.png)