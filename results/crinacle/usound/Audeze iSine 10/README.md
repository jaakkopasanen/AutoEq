# Audeze iSine 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.1; 25 -1.1; 28 -1.2; 31 -1.3; 34 -1.4; 37 -1.5; 41 -1.7; 45 -1.8; 49 -2.0; 54 -2.2; 60 -2.5; 66 -2.9; 72 -3.2; 79 -3.6; 87 -4.2; 96 -4.6; 106 -5.0; 116 -5.5; 128 -5.9; 141 -6.4; 155 -6.8; 170 -7.0; 187 -7.3; 206 -7.5; 227 -7.8; 249 -8.0; 274 -8.2; 302 -8.4; 332 -8.6; 365 -8.8; 402 -9.1; 442 -9.4; 486 -9.7; 535 -10.2; 588 -10.5; 647 -10.8; 712 -11.4; 783 -12.1; 861 -12.2; 947 -12.4; 1042 -12.3; 1146 -12.3; 1261 -12.7; 1387 -12.9; 1526 -10.7; 1678 -9.9; 1846 -8.9; 2031 -5.8; 2234 -3.0; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -3.7; 7010 -7.9; 7711 -9.1; 8482 -8.9; 9330 -9.3; 10263 -8.2; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -7.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.61 | 5.2 dB   |
| Peaking | 62 Hz    | 1.11 | 2.3 dB   |
| Peaking | 1391 Hz  | 0.52 | -16.0 dB |
| Peaking | 2820 Hz  | 0.43 | 15.7 dB  |
| Peaking | 8544 Hz  | 1.52 | -7.6 dB  |
| Peaking | 2477 Hz  | 4.39 | 2.0 dB   |
| Peaking | 3650 Hz  | 1.01 | -1.6 dB  |
| Peaking | 6142 Hz  | 2.06 | 4.3 dB   |
| Peaking | 6940 Hz  | 4.66 | -5.1 dB  |
| Peaking | 14759 Hz | 3.03 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -7.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 9.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audeze%20iSine%2010/Audeze%20iSine%2010.png)