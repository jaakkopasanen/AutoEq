# Massdrop x Sennheiser HD 58X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -1.9; 28 -2.7; 31 -3.2; 34 -3.5; 37 -3.9; 41 -4.4; 45 -4.8; 49 -5.0; 54 -5.2; 60 -5.5; 66 -5.4; 72 -5.1; 79 -6.5; 87 -7.4; 96 -7.9; 106 -8.3; 116 -8.6; 128 -8.9; 141 -9.2; 155 -9.3; 170 -9.2; 187 -9.3; 206 -9.3; 227 -9.2; 249 -9.1; 274 -8.9; 302 -8.7; 332 -8.3; 365 -8.0; 402 -7.8; 442 -7.6; 486 -7.5; 535 -7.3; 588 -7.0; 647 -7.0; 712 -7.1; 783 -7.1; 861 -7.0; 947 -7.0; 1042 -7.9; 1146 -8.2; 1261 -7.8; 1387 -7.4; 1526 -6.6; 1678 -5.8; 1846 -4.9; 2031 -4.0; 2234 -3.6; 2457 -3.3; 2703 -3.9; 2973 -4.9; 3270 -5.8; 3597 -6.0; 3957 -5.3; 4353 -3.6; 4788 -5.7; 5267 -9.3; 5793 -8.3; 6373 -2.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.9; 13660 -6.8; 15026 -6.5; 16529 -6.5; 18182 -9.6; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser HD 58X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser HD 58X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 179 Hz  | 0.57 | -3.1 dB |
| Peaking | 2099 Hz | 4.18 | 2.0 dB  |
| Peaking | 2579 Hz | 3.26 | 2.7 dB  |
| Peaking | 6622 Hz | 9.54 | 4.7 dB  |
| Peaking | 14 Hz   | 0.53 | 7.5 dB  |
| Peaking | 70 Hz   | 4.59 | 1.6 dB  |
| Peaking | 1175 Hz | 3.86 | -1.7 dB |
| Peaking | 4492 Hz | 6.34 | 3.6 dB  |
| Peaking | 5399 Hz | 6.37 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
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