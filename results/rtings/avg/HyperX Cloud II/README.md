# HyperX Cloud II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.5; 25 -9.9; 28 -10.4; 31 -10.8; 34 -11.0; 37 -11.2; 41 -11.3; 45 -11.3; 49 -11.3; 54 -11.2; 60 -11.3; 66 -11.4; 72 -11.6; 79 -11.8; 87 -12.2; 96 -12.5; 106 -12.9; 116 -13.2; 128 -13.3; 141 -13.0; 155 -12.8; 170 -12.5; 187 -11.8; 206 -11.0; 227 -10.2; 249 -9.5; 274 -9.1; 302 -9.0; 332 -9.1; 365 -9.2; 402 -9.2; 442 -9.1; 486 -9.2; 535 -9.3; 588 -9.2; 647 -9.0; 712 -8.7; 783 -8.3; 861 -8.0; 947 -7.0; 1042 -6.3; 1146 -6.7; 1261 -7.3; 1387 -7.9; 1526 -8.6; 1678 -9.7; 1846 -10.7; 2031 -11.9; 2234 -11.9; 2457 -10.6; 2703 -9.4; 2973 -8.7; 3270 -8.0; 3597 -5.2; 3957 -0.5; 4353 -1.7; 4788 -10.0; 5267 -9.7; 5793 -9.4; 6373 -11.3; 7010 -12.2; 7711 -13.4; 8482 -16.2; 9330 -16.6; 10263 -11.9; 11289 -7.7; 12418 -9.2; 13660 -13.8; 15026 -15.2; 16529 -13.4; 18182 -13.6; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.16 | -2.5 dB |
| Peaking | 120 Hz   | 0.42 | -6.1 dB |
| Peaking | 2094 Hz  | 2.81 | -5.7 dB |
| Peaking | 8573 Hz  | 2.67 | -9.0 dB |
| Peaking | 18802 Hz | 0.37 | -8.5 dB |
| Peaking | 607 Hz   | 3.1  | -1.5 dB |
| Peaking | 4081 Hz  | 4.77 | 9.9 dB  |
| Peaking | 4829 Hz  | 6.46 | -4.0 dB |
| Peaking | 8896 Hz  | 0.28 | -1.5 dB |
| Peaking | 11488 Hz | 4.35 | 5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.9 dB |
| Peaking | 16000 Hz | 1.41 | -9.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20II/HyperX%20Cloud%20II.png)