# RHA CL750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.4; 25 -6.6; 28 -6.7; 31 -6.8; 34 -6.8; 37 -6.8; 41 -6.9; 45 -6.9; 49 -7.0; 54 -7.0; 60 -7.1; 66 -7.3; 72 -7.5; 79 -7.7; 87 -8.0; 96 -8.2; 106 -8.5; 116 -8.7; 128 -9.0; 141 -9.2; 155 -9.3; 170 -9.4; 187 -9.4; 206 -9.3; 227 -9.3; 249 -9.4; 274 -9.3; 302 -9.0; 332 -8.6; 365 -8.2; 402 -7.8; 442 -7.4; 486 -7.0; 535 -6.4; 588 -5.9; 647 -5.3; 712 -4.6; 783 -3.9; 861 -3.3; 947 -2.9; 1042 -2.8; 1146 -2.9; 1261 -2.8; 1387 -2.4; 1526 -1.7; 1678 -0.8; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.1; 3270 -3.3; 3597 -5.3; 3957 -6.7; 4353 -7.9; 4788 -10.3; 5267 -14.1; 5793 -15.7; 6373 -12.7; 7010 -12.6; 7711 -13.9; 8482 -11.2; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -10.4; 13660 -25.1; 15026 -40.4; 16529 -46.8; 18182 -45.8; 20000 -41.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA CL750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA CL750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 221 Hz   | 0.44 | -6.0 dB  |
| Peaking | 2457 Hz  | 0.16 | 31.1 dB  |
| Peaking | 5559 Hz  | 2.67 | -7.5 dB  |
| Peaking | 11379 Hz | 1    | 31.8 dB  |
| Peaking | 16261 Hz | 0.12 | -62.7 dB |
| Peaking | 7777 Hz  | 8.97 | -2.4 dB  |
| Peaking | 9495 Hz  | 4.93 | 4.7 dB   |
| Peaking | 12808 Hz | 4.15 | 8.0 dB   |
| Peaking | 14910 Hz | 0.86 | -6.0 dB  |
| Peaking | 16395 Hz | 3.75 | 6.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 9.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 13.3 dB  |
| Peaking | 16000 Hz | 1.41 | -53.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/RHA%20CL750/RHA%20CL750.png)