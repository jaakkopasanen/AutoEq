# Massdrop Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.8; 25 -6.1; 28 -6.4; 31 -6.7; 34 -6.9; 37 -7.1; 41 -7.3; 45 -7.5; 49 -7.8; 54 -8.0; 60 -8.2; 66 -8.5; 72 -8.8; 79 -9.1; 87 -9.5; 96 -9.8; 106 -10.1; 116 -10.5; 128 -10.7; 141 -10.8; 155 -10.9; 170 -10.9; 187 -10.9; 206 -10.8; 227 -10.6; 249 -10.3; 274 -10.0; 302 -9.7; 332 -9.4; 365 -9.0; 402 -8.6; 442 -8.1; 486 -7.7; 535 -7.3; 588 -6.8; 647 -6.3; 712 -5.8; 783 -5.3; 861 -4.9; 947 -4.8; 1042 -5.1; 1146 -6.0; 1261 -7.0; 1387 -7.7; 1526 -8.0; 1678 -7.9; 1846 -7.7; 2031 -7.4; 2234 -7.1; 2457 -6.5; 2703 -5.7; 2973 -4.8; 3270 -3.9; 3597 -3.0; 3957 -2.1; 4353 -1.3; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.88 | -1.2 dB |
| Peaking | 200 Hz  | 0.56 | -3.9 dB |
| Peaking | 939 Hz  | 1.29 | 3.1 dB  |
| Peaking | 1531 Hz | 1.36 | -2.8 dB |
| Peaking | 4938 Hz | 1.55 | 6.8 dB  |
| Peaking | 18 Hz   | 1.74 | 1.3 dB  |
| Peaking | 3550 Hz | 2.29 | 1.6 dB  |
| Peaking | 5100 Hz | 0.88 | -1.5 dB |
| Peaking | 6331 Hz | 3.5  | 3.6 dB  |
| Peaking | 7984 Hz | 2.92 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Massdrop%20Plus/Massdrop%20Plus.png)