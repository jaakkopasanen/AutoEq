# Kinera Idun sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.9; 25 -2.1; 28 -2.4; 31 -2.6; 34 -2.8; 37 -3.0; 41 -3.2; 45 -3.4; 49 -3.5; 54 -3.8; 60 -4.0; 66 -4.3; 72 -4.6; 79 -4.9; 87 -5.3; 96 -5.6; 106 -6.0; 116 -6.3; 128 -6.6; 141 -6.8; 155 -6.9; 170 -7.0; 187 -7.0; 206 -7.0; 227 -6.8; 249 -6.6; 274 -6.4; 302 -6.1; 332 -5.7; 365 -5.3; 402 -4.9; 442 -4.4; 486 -3.8; 535 -3.3; 588 -3.1; 647 -2.7; 712 -2.2; 783 -2.0; 861 -2.2; 947 -2.8; 1042 -4.7; 1146 -7.3; 1261 -9.0; 1387 -10.1; 1526 -10.2; 1678 -9.1; 1846 -7.5; 2031 -5.9; 2234 -4.8; 2457 -4.5; 2703 -4.9; 2973 -5.7; 3270 -6.2; 3597 -5.5; 3957 -4.3; 4353 -2.1; 4788 -0.5; 5267 -2.4; 5793 -3.8; 6373 -3.7; 7010 -5.9; 7711 -7.8; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.9; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera Idun sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera Idun sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.22 | 3.6 dB  |
| Peaking | 183 Hz  | 0.61 | -2.5 dB |
| Peaking | 874 Hz  | 0.84 | 5.1 dB  |
| Peaking | 1381 Hz | 1.88 | -8.4 dB |
| Peaking | 4781 Hz | 4.76 | 5.1 dB  |
| Peaking | 1728 Hz | 4.73 | -1.1 dB |
| Peaking | 2385 Hz | 2.12 | 1.4 dB  |
| Peaking | 3239 Hz | 3.89 | -1.8 dB |
| Peaking | 6561 Hz | 3.59 | 1.6 dB  |
| Peaking | 7474 Hz | 5.99 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kinera%20Idun%20sample%201/Kinera%20Idun%20sample%201.png)