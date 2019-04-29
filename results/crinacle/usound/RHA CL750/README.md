# RHA CL750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.3; 25 -5.4; 28 -5.5; 31 -5.6; 34 -5.7; 37 -5.7; 41 -5.7; 45 -5.8; 49 -5.8; 54 -5.9; 60 -6.0; 66 -6.2; 72 -6.3; 79 -6.5; 87 -6.8; 96 -7.1; 106 -7.3; 116 -7.6; 128 -7.8; 141 -8.0; 155 -8.2; 170 -8.2; 187 -8.2; 206 -8.1; 227 -8.2; 249 -8.2; 274 -8.1; 302 -7.9; 332 -7.6; 365 -7.3; 402 -7.0; 442 -6.6; 486 -6.2; 535 -5.7; 588 -5.2; 647 -4.6; 712 -3.9; 783 -3.2; 861 -2.5; 947 -2.1; 1042 -1.9; 1146 -2.2; 1261 -2.3; 1387 -2.2; 1526 -1.8; 1678 -1.0; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.5; 2973 -3.4; 3270 -5.6; 3597 -7.3; 3957 -8.2; 4353 -9.1; 4788 -11.2; 5267 -15.0; 5793 -16.8; 6373 -14.2; 7010 -15.0; 7711 -16.8; 8482 -13.0; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -8.0; 13660 -16.2; 15026 -24.0; 16529 -27.9; 18182 -29.3; 20000 -30.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA CL750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA CL750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 229 Hz   | 0.78 | -2.1 dB  |
| Peaking | 961 Hz   | 1.17 | 3.7 dB   |
| Peaking | 2197 Hz  | 1.3  | 6.5 dB   |
| Peaking | 5800 Hz  | 2.18 | -9.3 dB  |
| Peaking | 18623 Hz | 0.71 | -26.3 dB |
| Peaking | 24 Hz    | 0.64 | 1.2 dB   |
| Peaking | 3686 Hz  | 4.28 | -1.5 dB  |
| Peaking | 7804 Hz  | 4.44 | -8.4 dB  |
| Peaking | 11568 Hz | 1.11 | 10.3 dB  |
| Peaking | 15302 Hz | 1.47 | -10.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB   |
| Peaking | 62 Hz    | 1.41 | 0.5 dB   |
| Peaking | 125 Hz   | 1.41 | -1.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 16000 Hz | 1.41 | -24.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/RHA%20CL750/RHA%20CL750.png)