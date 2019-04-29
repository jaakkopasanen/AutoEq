# Sennheiser IE80S Max
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.8; 25 -11.9; 28 -12.0; 31 -12.0; 34 -12.0; 37 -12.0; 41 -12.0; 45 -12.0; 49 -12.0; 54 -12.1; 60 -12.1; 66 -12.2; 72 -12.2; 79 -12.3; 87 -12.3; 96 -12.5; 106 -12.5; 116 -12.5; 128 -12.5; 141 -12.4; 155 -12.2; 170 -12.0; 187 -11.8; 206 -11.5; 227 -11.1; 249 -10.8; 274 -10.3; 302 -9.9; 332 -9.3; 365 -8.8; 402 -8.3; 442 -7.9; 486 -7.4; 535 -6.8; 588 -6.3; 647 -5.8; 712 -5.3; 783 -4.7; 861 -4.2; 947 -4.0; 1042 -3.8; 1146 -4.1; 1261 -4.5; 1387 -4.4; 1526 -3.9; 1678 -3.3; 1846 -2.7; 2031 -2.0; 2234 -1.4; 2457 -1.2; 2703 -1.5; 2973 -2.0; 3270 -2.6; 3597 -3.3; 3957 -4.6; 4353 -7.2; 4788 -9.8; 5267 -6.9; 5793 -1.5; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.1; 13660 -13.0; 15026 -17.3; 16529 -18.6; 18182 -22.1; 20000 -26.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80S Max GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80S Max ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.23 | -5.9 dB  |
| Peaking | 186 Hz   | 0.75 | -3.5 dB  |
| Peaking | 2212 Hz  | 1.02 | 4.7 dB   |
| Peaking | 6381 Hz  | 5.26 | 6.8 dB   |
| Peaking | 19253 Hz | 0.61 | -20.4 dB |
| Peaking | 874 Hz   | 3.04 | 1.7 dB   |
| Peaking | 3269 Hz  | 3.17 | 1.1 dB   |
| Peaking | 4758 Hz  | 6.14 | -5.7 dB  |
| Peaking | 12349 Hz | 1.49 | 7.1 dB   |
| Peaking | 14483 Hz | 1.62 | -7.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 16000 Hz | 1.41 | -17.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sennheiser%20IE80S%20Max/Sennheiser%20IE80S%20Max.png)