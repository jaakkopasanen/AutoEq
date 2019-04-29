# InEar PhoPhile-8 Bass Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.5; 25 -5.7; 28 -6.0; 31 -6.3; 34 -6.5; 37 -6.7; 41 -6.9; 45 -7.0; 49 -7.2; 54 -7.4; 60 -7.6; 66 -7.9; 72 -8.2; 79 -8.4; 87 -8.7; 96 -9.1; 106 -9.3; 116 -9.4; 128 -9.5; 141 -9.5; 155 -9.4; 170 -9.3; 187 -9.1; 206 -8.8; 227 -8.4; 249 -8.0; 274 -7.7; 302 -7.4; 332 -7.0; 365 -6.6; 402 -6.4; 442 -6.2; 486 -6.1; 535 -5.9; 588 -5.7; 647 -5.6; 712 -5.3; 783 -5.1; 861 -5.0; 947 -5.1; 1042 -5.5; 1146 -6.2; 1261 -6.7; 1387 -6.8; 1526 -6.5; 1678 -5.8; 1846 -5.1; 2031 -4.0; 2234 -2.7; 2457 -1.4; 2703 -0.6; 2973 -0.5; 3270 -1.1; 3597 -1.1; 3957 -1.0; 4353 -0.9; 4788 -1.7; 5267 -3.6; 5793 -4.9; 6373 -3.5; 7010 -4.1; 7711 -5.6; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -9.2; 15026 -18.5; 16529 -25.6; 18182 -29.2; 20000 -27.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar PhoPhile-8 Bass Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar PhoPhile-8 Bass Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 99 Hz    | 0.69 | -3.0 dB  |
| Peaking | 185 Hz   | 1.17 | -2.1 dB  |
| Peaking | 3698 Hz  | 0.64 | 10.7 dB  |
| Peaking | 12338 Hz | 0.51 | 25.0 dB  |
| Peaking | 17390 Hz | 0.18 | -35.9 dB |
| Peaking | 956 Hz   | 1.02 | 2.8 dB   |
| Peaking | 1316 Hz  | 1.9  | -2.0 dB  |
| Peaking | 1523 Hz  | 0.37 | -1.4 dB  |
| Peaking | 2541 Hz  | 2.82 | 2.4 dB   |
| Peaking | 6751 Hz  | 8    | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -23.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/InEar%20PhoPhile-8%20Bass%20Treble/InEar%20PhoPhile-8%20Bass%20Treble.png)