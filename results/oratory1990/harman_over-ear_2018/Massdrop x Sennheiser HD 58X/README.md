# Massdrop x Sennheiser HD 58X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.0; 28 -2.8; 31 -3.3; 34 -3.7; 37 -4.0; 41 -4.5; 45 -4.9; 49 -5.1; 54 -5.4; 60 -5.6; 66 -5.4; 72 -5.4; 79 -6.5; 87 -7.6; 96 -8.0; 106 -8.4; 116 -8.7; 128 -9.0; 141 -9.3; 155 -9.4; 170 -9.3; 187 -9.4; 206 -9.4; 227 -9.3; 249 -9.2; 274 -9.0; 302 -8.8; 332 -8.4; 365 -8.1; 402 -7.9; 442 -7.7; 486 -7.6; 535 -7.4; 588 -7.1; 647 -7.1; 712 -7.2; 783 -7.2; 861 -7.1; 947 -7.2; 1042 -8.0; 1146 -8.3; 1261 -8.0; 1387 -7.5; 1526 -6.7; 1678 -6.0; 1846 -5.0; 2031 -4.1; 2234 -3.6; 2457 -3.4; 2703 -4.0; 2973 -5.0; 3270 -5.9; 3597 -6.1; 3957 -5.4; 4353 -3.7; 4788 -5.8; 5267 -9.4; 5793 -8.3; 6373 -3.0; 7010 -4.1; 7711 -6.3; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -7.0; 13660 -6.9; 15026 -6.6; 16529 -6.6; 18182 -9.7; 20000 -17.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser HD 58X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser HD 58X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 179 Hz  | 0.57 | -3.1 dB |
| Peaking | 2100 Hz | 4.21 | 2.0 dB  |
| Peaking | 2600 Hz | 3.24 | 2.7 dB  |
| Peaking | 6609 Hz | 9.5  | 4.6 dB  |
| Peaking | 13 Hz   | 0.53 | 7.7 dB  |
| Peaking | 70 Hz   | 4.18 | 1.5 dB  |
| Peaking | 1175 Hz | 3.9  | -1.7 dB |
| Peaking | 4428 Hz | 6.38 | 3.4 dB  |
| Peaking | 5364 Hz | 6.76 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Sennheiser%20HD%2058X/Massdrop%20x%20Sennheiser%20HD%2058X.png)