# Sennheiser HD 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.3; 34 4.8; 37 4.3; 41 3.8; 45 3.3; 49 3.0; 54 2.9; 60 2.7; 66 2.2; 72 1.5; 79 1.1; 87 0.6; 96 -0.0; 106 -0.5; 116 -0.9; 128 -1.1; 141 -1.3; 155 -1.4; 170 -1.4; 187 -1.3; 206 -1.3; 227 -1.2; 249 -1.0; 274 -0.7; 302 -0.5; 332 -0.2; 365 0.1; 402 0.3; 442 0.4; 486 0.5; 535 0.6; 588 0.7; 647 0.8; 712 0.8; 783 0.9; 861 0.9; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -0.6; 1526 -0.3; 1678 -0.0; 1846 -0.3; 2031 0.0; 2234 0.3; 2457 -0.2; 2703 -1.1; 2973 -1.7; 3270 -2.0; 3597 -0.7; 3957 1.7; 4353 2.9; 4788 0.7; 5267 -0.1; 5793 -2.2; 6373 0.4; 7010 1.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.1; 12418 -4.3; 13660 -5.8; 15026 -3.2; 16529 -5.0; 18182 -8.4; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  1.31 | 6.5 dB  |
| Peaking | 54 Hz    |  2.79 | 2.0 dB  |
| Peaking | 13212 Hz |  3.06 | -7.7 dB |
| Peaking | 13382 Hz |  0.89 | 3.8 dB  |
| Peaking | 18544 Hz |  0.96 | -9.6 dB |
| Peaking | 173 Hz   |  1.25 | -1.7 dB |
| Peaking | 624 Hz   |  1.66 | 1.0 dB  |
| Peaking | 3214 Hz  |  3.36 | -2.6 dB |
| Peaking | 4202 Hz  |  5.23 | 3.6 dB  |
| Peaking | 5787 Hz  | 11.09 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)