# Earsonics EM32
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -12.2; 25 -12.4; 28 -12.5; 31 -12.6; 34 -12.7; 37 -12.8; 41 -12.9; 45 -12.9; 49 -12.9; 54 -12.8; 60 -12.8; 66 -12.9; 72 -12.9; 79 -12.9; 87 -12.8; 96 -12.7; 106 -12.5; 116 -12.2; 128 -11.7; 141 -11.2; 155 -10.5; 170 -9.6; 187 -8.7; 206 -7.5; 227 -6.5; 249 -5.5; 274 -4.8; 302 -4.5; 332 -4.6; 365 -5.0; 402 -5.5; 442 -6.0; 486 -6.5; 535 -6.9; 588 -7.2; 647 -7.4; 712 -7.6; 783 -7.7; 861 -7.7; 947 -8.0; 1042 -8.6; 1146 -9.5; 1261 -10.3; 1387 -10.6; 1526 -10.1; 1678 -9.0; 1846 -7.1; 2031 -4.3; 2234 -2.4; 2457 -2.5; 2703 -2.1; 2973 -1.9; 3270 -3.2; 3597 -4.6; 3957 -3.5; 4353 -3.2; 4788 -4.6; 5267 -1.7; 5793 -0.5; 6373 -2.9; 7010 -6.5; 7711 -6.7; 8482 -7.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.6; 16529 -12.5; 18182 -7.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics EM32 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics EM32 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.56 | -6.4 dB |
| Peaking | 105 Hz   | 1.42 | -4.3 dB |
| Peaking | 4370 Hz  | 0.99 | 4.1 dB  |
| Peaking | 14114 Hz | 2.78 | 3.7 dB  |
| Peaking | 15765 Hz | 1.64 | -7.7 dB |
| Peaking | 309 Hz   | 2.3  | 3.1 dB  |
| Peaking | 1546 Hz  | 1.21 | -6.7 dB |
| Peaking | 2287 Hz  | 1.49 | 6.7 dB  |
| Peaking | 5519 Hz  | 1.25 | -5.1 dB |
| Peaking | 5750 Hz  | 3.67 | 8.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Earsonics%20EM32/Earsonics%20EM32.png)