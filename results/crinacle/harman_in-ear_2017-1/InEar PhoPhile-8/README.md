# InEar PhoPhile-8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.2; 25 -1.5; 28 -1.9; 31 -2.2; 34 -2.5; 37 -2.7; 41 -2.9; 45 -3.2; 49 -3.4; 54 -3.6; 60 -3.9; 66 -4.2; 72 -4.5; 79 -4.8; 87 -5.2; 96 -5.6; 106 -6.0; 116 -6.3; 128 -6.5; 141 -6.8; 155 -7.0; 170 -7.1; 187 -7.2; 206 -7.3; 227 -7.3; 249 -7.3; 274 -7.3; 302 -7.2; 332 -7.0; 365 -6.9; 402 -6.8; 442 -6.7; 486 -6.6; 535 -6.5; 588 -6.3; 647 -6.1; 712 -5.9; 783 -5.6; 861 -5.5; 947 -5.5; 1042 -5.9; 1146 -6.6; 1261 -7.1; 1387 -7.2; 1526 -6.8; 1678 -6.2; 1846 -5.4; 2031 -4.2; 2234 -2.9; 2457 -1.5; 2703 -0.6; 2973 -0.5; 3270 -1.0; 3597 -1.0; 3957 -0.9; 4353 -0.8; 4788 -1.4; 5267 -3.2; 5793 -4.7; 6373 -2.8; 7010 -2.7; 7711 -4.7; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -7.6; 15026 -16.3; 16529 -22.3; 18182 -25.3; 20000 -23.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar PhoPhile-8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar PhoPhile-8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.19 | 4.1 dB   |
| Peaking | 282 Hz   | 0.27 | -2.9 dB  |
| Peaking | 1465 Hz  | 1.48 | -5.5 dB  |
| Peaking | 5618 Hz  | 0.15 | 5.8 dB   |
| Peaking | 18371 Hz | 0.57 | -24.5 dB |
| Peaking | 5657 Hz  | 4.34 | -4.3 dB  |
| Peaking | 6659 Hz  | 0.95 | 1.9 dB   |
| Peaking | 8088 Hz  | 2.77 | -3.0 dB  |
| Peaking | 13070 Hz | 2.44 | 5.8 dB   |
| Peaking | 15761 Hz | 2.08 | -5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB   |
| Peaking | 62 Hz    | 1.41 | 0.7 dB   |
| Peaking | 125 Hz   | 1.41 | -1.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -19.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/InEar%20PhoPhile-8/InEar%20PhoPhile-8.png)