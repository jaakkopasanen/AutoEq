# Grado SR80e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.2; 37 -1.9; 41 -2.8; 45 -3.6; 49 -4.2; 54 -4.9; 60 -5.6; 66 -6.2; 72 -6.6; 79 -7.0; 87 -7.3; 96 -7.6; 106 -7.9; 116 -8.0; 128 -8.1; 141 -8.1; 155 -8.1; 170 -8.0; 187 -8.0; 206 -7.8; 227 -7.6; 249 -7.4; 274 -7.4; 302 -7.5; 332 -7.6; 365 -7.5; 402 -7.6; 442 -7.6; 486 -7.6; 535 -7.6; 588 -7.4; 647 -7.2; 712 -6.9; 783 -6.7; 861 -6.5; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.9; 1387 -7.4; 1526 -8.1; 1678 -9.4; 1846 -13.3; 2031 -15.8; 2234 -14.6; 2457 -12.8; 2703 -11.3; 2973 -10.0; 3270 -9.5; 3597 -10.3; 3957 -12.1; 4353 -9.9; 4788 -7.3; 5267 -8.6; 5793 -9.4; 6373 -11.7; 7010 -13.9; 7711 -13.4; 8482 -14.8; 9330 -15.2; 10263 -11.2; 11289 -8.1; 12418 -8.7; 13660 -8.5; 15026 -7.5; 16529 -7.1; 18182 -6.9; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR80e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR80e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.63 | 7.5 dB  |
| Peaking | 85 Hz    | 0.35 | -2.7 dB |
| Peaking | 2144 Hz  | 2.53 | -9.0 dB |
| Peaking | 7548 Hz  | 1.1  | -5.4 dB |
| Peaking | 9075 Hz  | 3.53 | -4.9 dB |
| Peaking | 1216 Hz  | 2.21 | 1.1 dB  |
| Peaking | 4074 Hz  | 4.04 | -5.5 dB |
| Peaking | 4700 Hz  | 2.66 | 3.8 dB  |
| Peaking | 6844 Hz  | 8.99 | -2.0 dB |
| Peaking | 13587 Hz | 6.09 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -7.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR80e/Grado%20SR80e.png)