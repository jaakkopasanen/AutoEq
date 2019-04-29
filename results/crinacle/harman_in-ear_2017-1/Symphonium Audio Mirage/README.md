# Symphonium Audio Mirage
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.7; 25 -3.9; 28 -4.3; 31 -4.6; 34 -4.9; 37 -5.2; 41 -5.5; 45 -5.8; 49 -6.0; 54 -6.3; 60 -6.6; 66 -7.0; 72 -7.4; 79 -7.8; 87 -8.3; 96 -8.8; 106 -9.2; 116 -9.7; 128 -10.1; 141 -10.4; 155 -10.7; 170 -11.0; 187 -11.1; 206 -11.2; 227 -11.3; 249 -11.3; 274 -11.3; 302 -11.2; 332 -11.0; 365 -10.8; 402 -10.6; 442 -10.5; 486 -10.2; 535 -9.9; 588 -9.6; 647 -9.3; 712 -8.8; 783 -8.4; 861 -8.0; 947 -7.9; 1042 -8.2; 1146 -8.8; 1261 -9.3; 1387 -9.4; 1526 -9.2; 1678 -8.8; 1846 -8.4; 2031 -7.9; 2234 -6.9; 2457 -5.1; 2703 -2.8; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.2; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.9; 16529 -7.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Symphonium Audio Mirage GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Symphonium Audio Mirage ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.23 | 3.4 dB  |
| Peaking | 241 Hz   | 0.39 | -5.1 dB |
| Peaking | 1801 Hz  | 1.01 | -7.4 dB |
| Peaking | 3994 Hz  | 0.47 | 10.6 dB |
| Peaking | 8959 Hz  | 0.51 | -4.5 dB |
| Peaking | 3007 Hz  | 7.23 | 1.6 dB  |
| Peaking | 6181 Hz  | 2.95 | 5.2 dB  |
| Peaking | 7026 Hz  | 1.14 | -4.5 dB |
| Peaking | 12698 Hz | 0.6  | 2.3 dB  |
| Peaking | 15280 Hz | 3.35 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Symphonium%20Audio%20Mirage/Symphonium%20Audio%20Mirage.png)