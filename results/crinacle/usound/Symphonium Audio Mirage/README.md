# Symphonium Audio Mirage
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.5; 25 -2.8; 28 -3.1; 31 -3.5; 34 -3.8; 37 -4.1; 41 -4.3; 45 -4.6; 49 -4.9; 54 -5.1; 60 -5.4; 66 -5.9; 72 -6.3; 79 -6.7; 87 -7.1; 96 -7.7; 106 -8.1; 116 -8.5; 128 -8.9; 141 -9.3; 155 -9.6; 170 -9.8; 187 -10.0; 206 -10.0; 227 -10.1; 249 -10.2; 274 -10.2; 302 -10.1; 332 -10.0; 365 -9.9; 402 -9.8; 442 -9.7; 486 -9.5; 535 -9.2; 588 -8.9; 647 -8.6; 712 -8.2; 783 -7.7; 861 -7.3; 947 -7.1; 1042 -7.4; 1146 -8.0; 1261 -8.8; 1387 -9.3; 1526 -9.3; 1678 -8.9; 1846 -8.6; 2031 -8.4; 2234 -8.0; 2457 -6.8; 2703 -4.9; 2973 -2.5; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -2.0; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Symphonium Audio Mirage GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Symphonium Audio Mirage ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.24 | 4.6 dB  |
| Peaking | 236 Hz  | 0.47 | -4.0 dB |
| Peaking | 1937 Hz | 1.2  | -3.8 dB |
| Peaking | 3710 Hz | 1.39 | 7.5 dB  |
| Peaking | 6089 Hz | 4.46 | 4.1 dB  |
| Peaking | 943 Hz  | 3.95 | 1.0 dB  |
| Peaking | 1344 Hz | 5.73 | -0.9 dB |
| Peaking | 4772 Hz | 8.12 | 1.5 dB  |
| Peaking | 6697 Hz | 6.28 | 2.1 dB  |
| Peaking | 7406 Hz | 1.67 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Symphonium%20Audio%20Mirage/Symphonium%20Audio%20Mirage.png)