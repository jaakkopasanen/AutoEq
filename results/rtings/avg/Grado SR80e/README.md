# Grado SR80e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.3; 37 4.6; 41 3.7; 45 2.9; 49 2.3; 54 1.6; 60 0.9; 66 0.3; 72 -0.1; 79 -0.5; 87 -0.8; 96 -1.1; 106 -1.4; 116 -1.5; 128 -1.6; 141 -1.6; 155 -1.6; 170 -1.5; 187 -1.5; 206 -1.3; 227 -1.1; 249 -0.9; 274 -0.9; 302 -1.0; 332 -1.1; 365 -1.0; 402 -1.1; 442 -1.1; 486 -1.1; 535 -1.1; 588 -0.9; 647 -0.7; 712 -0.4; 783 -0.2; 861 0.0; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.4; 1387 -0.9; 1526 -1.6; 1678 -2.9; 1846 -6.8; 2031 -9.3; 2234 -8.1; 2457 -6.3; 2703 -4.8; 2973 -3.5; 3270 -3.0; 3597 -3.8; 3957 -5.6; 4353 -3.4; 4788 -0.8; 5267 -2.1; 5793 -2.9; 6373 -5.2; 7010 -7.4; 7711 -6.9; 8482 -8.3; 9330 -8.7; 10263 -4.7; 11289 -1.6; 12418 -2.2; 13660 -2.0; 15026 -1.0; 16529 -0.6; 18182 -0.4; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR80e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR80e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.63 | 7.4 dB  |
| Peaking | 88 Hz    | 0.37 | -2.6 dB |
| Peaking | 2149 Hz  | 2.49 | -9.0 dB |
| Peaking | 7600 Hz  | 1.23 | -5.8 dB |
| Peaking | 9131 Hz  | 4.16 | -4.6 dB |
| Peaking | 1229 Hz  | 2.21 | 1.1 dB  |
| Peaking | 4085 Hz  | 4.68 | -4.5 dB |
| Peaking | 4860 Hz  | 3.87 | 3.2 dB  |
| Peaking | 11280 Hz | 4.21 | 2.9 dB  |
| Peaking | 11845 Hz | 1.49 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR80e/Grado%20SR80e.png)