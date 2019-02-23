# Grado SR125e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.3; 54 -1.9; 60 -2.4; 66 -2.9; 72 -3.2; 79 -3.5; 87 -3.8; 96 -4.1; 106 -4.3; 116 -4.5; 128 -4.7; 141 -4.8; 155 -4.8; 170 -4.8; 187 -4.7; 206 -4.5; 227 -4.1; 249 -3.9; 274 -4.0; 302 -4.5; 332 -4.5; 365 -4.4; 402 -4.4; 442 -4.4; 486 -4.4; 535 -4.4; 588 -4.2; 647 -4.1; 712 -4.0; 783 -3.8; 861 -3.7; 947 -3.6; 1042 -3.6; 1146 -3.7; 1261 -4.1; 1387 -4.6; 1526 -5.5; 1678 -6.7; 1846 -10.7; 2031 -13.2; 2234 -12.1; 2457 -10.6; 2703 -9.2; 2973 -7.9; 3270 -7.4; 3597 -8.1; 3957 -10.7; 4353 -8.0; 4788 -4.2; 5267 -7.5; 5793 -8.6; 6373 -9.1; 7010 -11.4; 7711 -11.6; 8482 -13.4; 9330 -14.5; 10263 -11.0; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 27 Hz    |  0.39 | 6.2 dB  |
| Peaking | 897 Hz   |  0.41 | 3.3 dB  |
| Peaking | 2136 Hz  |  2.36 | -8.6 dB |
| Peaking | 7328 Hz  |  2.36 | -4.0 dB |
| Peaking | 9234 Hz  |  3.87 | -7.3 dB |
| Peaking | 245 Hz   |  4.26 | 1.1 dB  |
| Peaking | 1455 Hz  |  3.93 | 1.0 dB  |
| Peaking | 3969 Hz  |  6.99 | -4.2 dB |
| Peaking | 4813 Hz  | 10.23 | 4.0 dB  |
| Peaking | 11709 Hz |  5.39 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR125e/Grado%20SR125e.png)