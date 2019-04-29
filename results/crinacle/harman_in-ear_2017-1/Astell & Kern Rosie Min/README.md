# Astell & Kern Rosie Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.5; 28 -5.7; 31 -6.1; 34 -6.4; 37 -6.8; 41 -7.2; 45 -7.5; 49 -7.8; 54 -8.1; 60 -8.6; 66 -8.9; 72 -9.3; 79 -9.7; 87 -10.1; 96 -10.7; 106 -11.1; 116 -11.3; 128 -11.6; 141 -11.9; 155 -12.0; 170 -12.1; 187 -12.1; 206 -12.0; 227 -11.8; 249 -11.7; 274 -11.4; 302 -11.1; 332 -10.6; 365 -10.1; 402 -9.7; 442 -9.3; 486 -8.7; 535 -8.1; 588 -7.5; 647 -6.9; 712 -6.2; 783 -5.5; 861 -5.0; 947 -4.7; 1042 -4.8; 1146 -5.3; 1261 -6.1; 1387 -6.2; 1526 -5.7; 1678 -5.1; 1846 -4.5; 2031 -3.6; 2234 -2.1; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.5; 4353 -0.5; 4788 -1.4; 5267 -4.3; 5793 -2.1; 6373 -1.0; 7010 -4.1; 7711 -9.2; 8482 -12.2; 9330 -12.0; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -11.9; 15026 -17.8; 16529 -18.1; 18182 -23.5; 20000 -31.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern Rosie Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern Rosie Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 139 Hz   | 0.72 | -5.0 dB  |
| Peaking | 294 Hz   | 1.23 | -2.9 dB  |
| Peaking | 3275 Hz  | 1    | 7.0 dB   |
| Peaking | 6280 Hz  | 6.93 | 5.5 dB   |
| Peaking | 19664 Hz | 0.58 | -24.6 dB |
| Peaking | 24 Hz    | 1.93 | 1.5 dB   |
| Peaking | 900 Hz   | 4.05 | 1.9 dB   |
| Peaking | 8803 Hz  | 3.29 | -7.5 dB  |
| Peaking | 12576 Hz | 1.26 | 8.8 dB   |
| Peaking | 14749 Hz | 1.96 | -8.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB   |
| Peaking | 62 Hz    | 1.41 | -1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -16.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Astell%20&%20Kern%20Rosie%20Min/Astell%20&%20Kern%20Rosie%20Min.png)