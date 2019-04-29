# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.9; 28 -4.0; 31 -4.0; 34 -4.1; 37 -4.2; 41 -4.4; 45 -4.6; 49 -4.7; 54 -4.9; 60 -5.2; 66 -5.5; 72 -5.9; 79 -6.3; 87 -6.7; 96 -7.2; 106 -7.7; 116 -8.1; 128 -8.5; 141 -8.8; 155 -9.1; 170 -9.4; 187 -9.6; 206 -9.7; 227 -9.8; 249 -9.8; 274 -9.8; 302 -9.8; 332 -9.8; 365 -9.7; 402 -9.6; 442 -9.5; 486 -9.3; 535 -9.1; 588 -8.8; 647 -8.5; 712 -8.0; 783 -7.5; 861 -7.0; 947 -6.7; 1042 -6.7; 1146 -7.1; 1261 -7.5; 1387 -7.5; 1526 -7.0; 1678 -6.2; 1846 -5.5; 2031 -5.2; 2234 -4.8; 2457 -3.9; 2703 -3.2; 2973 -3.4; 3270 -4.1; 3597 -3.6; 3957 -2.0; 4353 -0.6; 4788 -0.5; 5267 -1.4; 5793 -1.9; 6373 -1.8; 7010 -4.7; 7711 -8.5; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 29 Hz    |  0.3  | 3.0 dB  |
| Peaking | 231 Hz   |  0.41 | -3.9 dB |
| Peaking | 2586 Hz  |  3.21 | 2.1 dB  |
| Peaking | 5056 Hz  |  1.29 | 6.1 dB  |
| Peaking | 7926 Hz  |  4.92 | -4.7 dB |
| Peaking | 986 Hz   |  1.95 | 2.6 dB  |
| Peaking | 1181 Hz  |  1.05 | -2.2 dB |
| Peaking | 1844 Hz  |  2.86 | 1.3 dB  |
| Peaking | 6488 Hz  | 11.5  | 1.5 dB  |
| Peaking | 11222 Hz |  1.47 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shure%20SE535/Shure%20SE535.png)