# Custom Art FIBAE ME
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.8; 25 -11.0; 28 -11.3; 31 -11.5; 34 -11.6; 37 -11.8; 41 -12.0; 45 -12.1; 49 -12.3; 54 -12.4; 60 -12.7; 66 -13.0; 72 -13.3; 79 -13.6; 87 -13.9; 96 -14.3; 106 -14.5; 116 -14.8; 128 -14.9; 141 -15.1; 155 -15.2; 170 -15.1; 187 -15.0; 206 -14.8; 227 -14.6; 249 -14.2; 274 -13.9; 302 -13.3; 332 -12.7; 365 -12.1; 402 -11.5; 442 -10.9; 486 -10.1; 535 -9.3; 588 -8.5; 647 -7.7; 712 -6.8; 783 -5.9; 861 -5.1; 947 -4.7; 1042 -4.8; 1146 -5.3; 1261 -6.0; 1387 -6.7; 1526 -7.4; 1678 -8.4; 1846 -9.0; 2031 -6.7; 2234 -4.0; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -2.1; 3597 -2.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -8.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.7; 15026 -19.9; 16529 -25.0; 18182 -25.6; 20000 -24.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE ME GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE ME ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 64 Hz    | 0.28 | -5.6 dB  |
| Peaking | 215 Hz   | 0.67 | -5.4 dB  |
| Peaking | 5228 Hz  | 0.68 | 12.4 dB  |
| Peaking | 12374 Hz | 1.46 | 13.7 dB  |
| Peaking | 17373 Hz | 0.24 | -22.2 dB |
| Peaking | 948 Hz   | 1.36 | 4.9 dB   |
| Peaking | 1241 Hz  | 0.48 | -2.8 dB  |
| Peaking | 1823 Hz  | 3.83 | -3.6 dB  |
| Peaking | 2605 Hz  | 3.09 | 4.8 dB   |
| Peaking | 10282 Hz | 9.14 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -7.0 dB  |
| Peaking | 250 Hz   | 1.41 | -6.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 16000 Hz | 1.41 | -21.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Custom%20Art%20FIBAE%20ME/Custom%20Art%20FIBAE%20ME.png)