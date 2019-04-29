# Shure SE425
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.2; 31 -1.7; 34 -2.1; 37 -2.4; 41 -2.8; 45 -3.1; 49 -3.4; 54 -3.8; 60 -4.3; 66 -4.8; 72 -5.2; 79 -5.7; 87 -6.3; 96 -6.9; 106 -7.4; 116 -7.9; 128 -8.3; 141 -8.8; 155 -9.1; 170 -9.4; 187 -9.6; 206 -9.8; 227 -9.8; 249 -9.9; 274 -9.9; 302 -9.9; 332 -9.7; 365 -9.5; 402 -9.4; 442 -9.2; 486 -9.0; 535 -8.8; 588 -8.4; 647 -8.1; 712 -7.6; 783 -7.2; 861 -6.8; 947 -6.6; 1042 -6.8; 1146 -7.3; 1261 -7.6; 1387 -7.4; 1526 -6.8; 1678 -6.1; 1846 -5.5; 2031 -4.9; 2234 -4.4; 2457 -4.3; 2703 -4.4; 2973 -4.5; 3270 -5.0; 3597 -6.1; 3957 -6.3; 4353 -4.2; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.5; 16529 -7.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.57 | 6.0 dB  |
| Peaking | 60 Hz    | 1.04 | 1.2 dB  |
| Peaking | 239 Hz   | 0.48 | -3.7 dB |
| Peaking | 2393 Hz  | 2.52 | 2.4 dB  |
| Peaking | 5556 Hz  | 2.77 | 6.9 dB  |
| Peaking | 938 Hz   | 2.17 | 1.9 dB  |
| Peaking | 1269 Hz  | 1.04 | -1.7 dB |
| Peaking | 1800 Hz  | 2.21 | 1.3 dB  |
| Peaking | 14501 Hz | 4.96 | -1.6 dB |
| Peaking | 15391 Hz | 5.64 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shure%20SE425/Shure%20SE425.png)