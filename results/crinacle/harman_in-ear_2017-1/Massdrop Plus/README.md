# Massdrop Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.2; 28 -7.6; 31 -7.9; 34 -8.1; 37 -8.2; 41 -8.4; 45 -8.7; 49 -8.9; 54 -9.2; 60 -9.4; 66 -9.7; 72 -10.0; 79 -10.3; 87 -10.6; 96 -11.0; 106 -11.3; 116 -11.6; 128 -11.8; 141 -12.0; 155 -12.0; 170 -12.1; 187 -12.0; 206 -12.0; 227 -11.8; 249 -11.5; 274 -11.2; 302 -10.8; 332 -10.3; 365 -9.8; 402 -9.4; 442 -9.0; 486 -8.5; 535 -8.0; 588 -7.5; 647 -7.0; 712 -6.5; 783 -6.0; 861 -5.6; 947 -5.6; 1042 -6.0; 1146 -6.7; 1261 -7.5; 1387 -7.9; 1526 -7.9; 1678 -7.7; 1846 -7.5; 2031 -6.9; 2234 -5.9; 2457 -4.8; 2703 -3.6; 2973 -2.5; 3270 -1.6; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -12.3; 16529 -12.7; 18182 -7.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 118 Hz   | 0.55 | -4.5 dB |
| Peaking | 255 Hz   | 1.06 | -2.8 dB |
| Peaking | 1731 Hz  | 2.37 | -2.6 dB |
| Peaking | 4384 Hz  | 1.02 | 6.8 dB  |
| Peaking | 16053 Hz | 2.12 | -7.7 dB |
| Peaking | 893 Hz   | 2.76 | 1.5 dB  |
| Peaking | 1321 Hz  | 5.13 | -1.0 dB |
| Peaking | 6373 Hz  | 3.52 | 4.3 dB  |
| Peaking | 7293 Hz  | 1.78 | -3.2 dB |
| Peaking | 13426 Hz | 5.45 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -6.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Massdrop%20Plus/Massdrop%20Plus.png)