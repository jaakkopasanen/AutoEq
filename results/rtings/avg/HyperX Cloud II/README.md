# HyperX Cloud II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.2; 25 -6.6; 28 -7.1; 31 -7.5; 34 -7.7; 37 -7.9; 41 -8.0; 45 -8.1; 49 -8.0; 54 -8.0; 60 -8.0; 66 -8.1; 72 -8.3; 79 -8.5; 87 -8.8; 96 -9.2; 106 -9.5; 116 -9.8; 128 -9.9; 141 -9.7; 155 -9.5; 170 -9.2; 187 -8.6; 206 -7.7; 227 -7.0; 249 -6.3; 274 -5.9; 302 -5.8; 332 -5.9; 365 -6.0; 402 -6.0; 442 -6.0; 486 -6.2; 535 -6.2; 588 -6.1; 647 -6.0; 712 -5.8; 783 -5.4; 861 -5.0; 947 -4.1; 1042 -3.4; 1146 -3.7; 1261 -4.4; 1387 -5.0; 1526 -5.8; 1678 -6.8; 1846 -7.9; 2031 -9.2; 2234 -9.6; 2457 -8.5; 2703 -6.9; 2973 -5.7; 3270 -4.8; 3597 -1.8; 3957 -0.5; 4353 -0.5; 4788 -7.4; 5267 -7.1; 5793 -6.4; 6373 -7.3; 7010 -9.2; 7711 -11.2; 8482 -12.9; 9330 -11.8; 10263 -8.1; 11289 -6.5; 12418 -6.7; 13660 -10.1; 15026 -11.6; 16529 -10.0; 18182 -10.4; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 116 Hz   | 1.13 | -3.5 dB |
| Peaking | 1047 Hz  | 2.9  | 3.4 dB  |
| Peaking | 3986 Hz  | 4.84 | 7.4 dB  |
| Peaking | 8431 Hz  | 3.33 | -6.3 dB |
| Peaking | 19923 Hz | 0.28 | -5.2 dB |
| Peaking | 42 Hz    | 1.85 | -1.2 dB |
| Peaking | 317 Hz   | 1.97 | 1.2 dB  |
| Peaking | 2172 Hz  | 4.26 | -3.8 dB |
| Peaking | 11858 Hz | 3.39 | 2.7 dB  |
| Peaking | 14538 Hz | 3.47 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20II/HyperX%20Cloud%20II.png)