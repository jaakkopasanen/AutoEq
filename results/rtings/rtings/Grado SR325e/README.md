# Grado SR325e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.5; 37 4.8; 41 4.0; 45 3.3; 49 2.7; 54 2.1; 60 1.6; 66 1.1; 72 0.7; 79 0.4; 87 0.1; 96 -0.1; 106 -0.4; 116 -0.6; 128 -0.7; 141 -0.8; 155 -0.8; 170 -0.9; 187 -0.8; 206 -0.4; 227 -0.2; 249 -0.3; 274 -0.7; 302 -0.7; 332 -0.6; 365 -0.4; 402 -0.4; 442 -0.6; 486 -0.7; 535 -0.7; 588 -0.5; 647 -0.4; 712 -0.2; 783 -0.1; 861 0.0; 947 0.0; 1042 0.0; 1146 -0.1; 1261 -0.4; 1387 -1.0; 1526 -1.8; 1678 -3.0; 1846 -5.9; 2031 -9.0; 2234 -8.9; 2457 -7.0; 2703 -5.1; 2973 -3.7; 3270 -3.2; 3597 -2.4; 3957 -2.9; 4353 -4.0; 4788 -0.8; 5267 -0.4; 5793 -0.9; 6373 -0.6; 7010 -0.7; 7711 -2.3; 8482 -6.8; 9330 -11.8; 10263 -12.7; 11289 -8.5; 12418 -3.8; 13660 -1.1; 15026 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 26 Hz    |  0.63 | 6.8 dB   |
| Peaking | 90 Hz    |  0.4  | -1.5 dB  |
| Peaking | 2159 Hz  |  2.88 | -9.4 dB  |
| Peaking | 3559 Hz  |  2.02 | -1.8 dB  |
| Peaking | 10018 Hz |  3.02 | -14.3 dB |
| Peaking | 1119 Hz  |  2.79 | 0.8 dB   |
| Peaking | 4342 Hz  | 11.14 | -2.6 dB  |
| Peaking | 6961 Hz  |  1.84 | 1.8 dB   |
| Peaking | 8890 Hz  |  6.26 | -2.9 dB  |
| Peaking | 14885 Hz |  4.07 | 1.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Grado%20SR325e/Grado%20SR325e.png)