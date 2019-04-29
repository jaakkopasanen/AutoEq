# Kinera Idun
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.6; 25 -1.8; 28 -2.1; 31 -2.3; 34 -2.4; 37 -2.6; 41 -2.8; 45 -3.0; 49 -3.2; 54 -3.4; 60 -3.6; 66 -3.9; 72 -4.2; 79 -4.5; 87 -4.9; 96 -5.3; 106 -5.7; 116 -6.0; 128 -6.3; 141 -6.5; 155 -6.7; 170 -6.8; 187 -6.8; 206 -6.8; 227 -6.7; 249 -6.5; 274 -6.3; 302 -6.0; 332 -5.7; 365 -5.4; 402 -5.0; 442 -4.5; 486 -4.1; 535 -3.8; 588 -3.6; 647 -3.3; 712 -3.1; 783 -3.1; 861 -3.3; 947 -4.1; 1042 -5.7; 1146 -7.3; 1261 -8.3; 1387 -8.6; 1526 -8.1; 1678 -6.9; 1846 -5.4; 2031 -4.1; 2234 -3.3; 2457 -3.2; 2703 -3.8; 2973 -4.7; 3270 -4.9; 3597 -3.9; 3957 -2.8; 4353 -1.4; 4788 -0.5; 5267 -2.4; 5793 -4.2; 6373 -3.9; 7010 -5.6; 7711 -7.9; 8482 -5.4; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera Idun GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera Idun ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.2  | 3.5 dB  |
| Peaking | 191 Hz  | 0.56 | -2.7 dB |
| Peaking | 1097 Hz | 0.58 | 4.8 dB  |
| Peaking | 1324 Hz | 1.69 | -8.5 dB |
| Peaking | 4661 Hz | 4.83 | 4.4 dB  |
| Peaking | 1691 Hz | 3.71 | -1.4 dB |
| Peaking | 2714 Hz | 1.16 | 1.9 dB  |
| Peaking | 3099 Hz | 3.13 | -2.8 dB |
| Peaking | 7712 Hz | 6.93 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kinera%20Idun/Kinera%20Idun.png)