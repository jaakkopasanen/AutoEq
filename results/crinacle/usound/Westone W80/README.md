# Westone W80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.3; 25 -8.3; 28 -8.5; 31 -8.6; 34 -8.7; 37 -8.9; 41 -9.0; 45 -9.1; 49 -9.2; 54 -9.4; 60 -9.6; 66 -9.9; 72 -10.2; 79 -10.5; 87 -10.8; 96 -11.3; 106 -11.6; 116 -11.9; 128 -12.1; 141 -12.3; 155 -12.5; 170 -12.5; 187 -12.6; 206 -12.5; 227 -12.4; 249 -12.3; 274 -12.1; 302 -11.8; 332 -11.6; 365 -11.3; 402 -11.0; 442 -10.6; 486 -10.3; 535 -9.9; 588 -9.5; 647 -9.0; 712 -8.5; 783 -8.0; 861 -7.7; 947 -7.5; 1042 -7.7; 1146 -8.3; 1261 -8.9; 1387 -9.0; 1526 -8.2; 1678 -6.7; 1846 -4.7; 2031 -2.7; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.1; 5267 -3.2; 5793 -1.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.09 | -1.4 dB |
| Peaking | 206 Hz   | 0.4  | -4.9 dB |
| Peaking | 1480 Hz  | 2.01 | -4.9 dB |
| Peaking | 2408 Hz  | 1.01 | 6.3 dB  |
| Peaking | 4638 Hz  | 1.28 | 3.9 dB  |
| Peaking | 502 Hz   | 4.5  | -0.2 dB |
| Peaking | 6441 Hz  | 5.15 | 4.8 dB  |
| Peaking | 7124 Hz  | 1.56 | -2.3 dB |
| Peaking | 19828 Hz | 1.99 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Westone%20W80/Westone%20W80.png)