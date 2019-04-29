# Hifiman RE400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.6; 25 -1.8; 28 -2.0; 31 -2.1; 34 -2.3; 37 -2.5; 41 -2.7; 45 -2.9; 49 -3.1; 54 -3.3; 60 -3.6; 66 -4.0; 72 -4.3; 79 -4.7; 87 -5.2; 96 -5.6; 106 -6.0; 116 -6.4; 128 -6.7; 141 -7.0; 155 -7.3; 170 -7.4; 187 -7.6; 206 -7.5; 227 -7.5; 249 -7.4; 274 -7.3; 302 -7.2; 332 -7.2; 365 -7.0; 402 -7.0; 442 -6.7; 486 -6.4; 535 -6.2; 588 -5.9; 647 -5.6; 712 -5.3; 783 -4.9; 861 -4.8; 947 -4.9; 1042 -5.3; 1146 -6.1; 1261 -7.0; 1387 -7.7; 1526 -8.0; 1678 -8.2; 1846 -8.5; 2031 -9.0; 2234 -8.5; 2457 -8.2; 2703 -6.6; 2973 -4.3; 3270 -2.3; 3597 -1.1; 3957 -0.5; 4353 -0.6; 4788 -1.5; 5267 -3.9; 5793 -8.4; 6373 -8.8; 7010 -5.3; 7711 -5.9; 8482 -7.1; 9330 -6.9; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.3; 16529 -7.7; 18182 -6.4; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman RE400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman RE400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.17 | 4.7 dB  |
| Peaking | 53 Hz    | 1.98 | 2.3 dB  |
| Peaking | 2161 Hz  | 1.71 | -4.3 dB |
| Peaking | 4022 Hz  | 1.52 | 7.0 dB  |
| Peaking | 6040 Hz  | 5.51 | -6.0 dB |
| Peaking | 227 Hz   | 0.93 | -1.6 dB |
| Peaking | 890 Hz   | 1.69 | 1.9 dB  |
| Peaking | 1386 Hz  | 3.18 | -1.3 dB |
| Peaking | 8815 Hz  | 7.61 | -2.0 dB |
| Peaking | 16594 Hz | 2.99 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hifiman%20RE400/Hifiman%20RE400.png)