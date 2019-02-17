# Massdrop x Sennheiser HD 58X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.6; 31 -2.1; 34 -2.4; 37 -2.8; 41 -3.3; 45 -3.7; 49 -3.9; 54 -4.1; 60 -4.5; 66 -4.3; 72 -4.0; 79 -5.5; 87 -6.3; 96 -6.8; 106 -7.2; 116 -7.5; 128 -7.8; 141 -8.1; 155 -8.2; 170 -8.1; 187 -8.2; 206 -8.2; 227 -8.1; 249 -8.0; 274 -7.8; 302 -7.6; 332 -7.2; 365 -6.9; 402 -6.7; 442 -6.5; 486 -6.4; 535 -6.2; 588 -5.9; 647 -5.9; 712 -6.0; 783 -6.0; 861 -5.9; 947 -5.9; 1042 -6.8; 1146 -7.1; 1261 -6.8; 1387 -6.3; 1526 -5.5; 1678 -4.8; 1846 -3.8; 2031 -2.9; 2234 -2.5; 2457 -2.2; 2703 -2.8; 2973 -3.8; 3270 -4.7; 3597 -4.9; 3957 -4.2; 4353 -2.5; 4788 -4.6; 5267 -8.2; 5793 -7.2; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.5; 20000 -16.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser HD 58X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser HD 58X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.28 | 6.0 dB  |
| Peaking | 57 Hz   | 2.78 | 1.7 dB  |
| Peaking | 2364 Hz | 2.08 | 4.6 dB  |
| Peaking | 4372 Hz | 7.72 | 3.8 dB  |
| Peaking | 6562 Hz | 9.32 | 5.0 dB  |
| Peaking | 72 Hz   | 5.48 | 1.9 dB  |
| Peaking | 177 Hz  | 0.78 | -1.9 dB |
| Peaking | 602 Hz  | 2.22 | 0.9 dB  |
| Peaking | 5339 Hz | 2.22 | 1.8 dB  |
| Peaking | 5398 Hz | 5.79 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Sennheiser%20HD%2058X/Massdrop%20x%20Sennheiser%20HD%2058X.png)