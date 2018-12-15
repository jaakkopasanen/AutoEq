# Grado SR60e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.5; 34 4.8; 37 4.0; 41 3.1; 45 2.3; 49 1.7; 54 1.0; 60 0.3; 66 -0.3; 72 -0.8; 79 -1.1; 87 -1.4; 96 -1.7; 106 -1.9; 116 -2.1; 128 -2.2; 141 -2.2; 155 -2.1; 170 -1.9; 187 -1.8; 206 -1.5; 227 -1.4; 249 -1.4; 274 -1.3; 302 -1.1; 332 -1.1; 365 -1.8; 402 -1.9; 442 -1.7; 486 -1.4; 535 -1.2; 588 -1.1; 647 -0.8; 712 -0.6; 783 -0.4; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.0; 1261 -0.3; 1387 -0.8; 1526 -1.6; 1678 -2.8; 1846 -6.5; 2031 -8.8; 2234 -7.8; 2457 -6.1; 2703 -4.7; 2973 -3.5; 3270 -3.1; 3597 -5.4; 3957 -7.0; 4353 -3.4; 4788 -0.8; 5267 -3.1; 5793 -3.7; 6373 -5.6; 7010 -7.4; 7711 -8.6; 8482 -10.5; 9330 -10.8; 10263 -7.6; 11289 -3.9; 12418 -1.3; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.69 | 7.6 dB  |
| Peaking | 90 Hz    | 0.32 | -2.9 dB |
| Peaking | 2179 Hz  | 2.23 | -8.2 dB |
| Peaking | 7670 Hz  | 1.3  | -6.7 dB |
| Peaking | 9285 Hz  | 3.54 | -6.5 dB |
| Peaking | 448 Hz   | 2.91 | -0.9 dB |
| Peaking | 1215 Hz  | 1.99 | 1.3 dB  |
| Peaking | 3909 Hz  | 5.99 | -5.8 dB |
| Peaking | 4757 Hz  | 5.34 | 2.9 dB  |
| Peaking | 13719 Hz | 3.2  | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR60e/Grado%20SR60e.png)