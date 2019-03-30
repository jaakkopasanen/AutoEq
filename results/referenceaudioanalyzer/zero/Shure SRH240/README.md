# Shure SRH240
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.9; 34 -3.2; 37 -4.3; 41 -5.7; 45 -6.8; 49 -7.8; 54 -8.6; 60 -9.1; 66 -9.4; 72 -9.5; 79 -9.6; 87 -9.9; 96 -10.1; 106 -9.8; 116 -9.5; 128 -9.2; 141 -8.6; 155 -7.7; 170 -6.4; 187 -5.0; 206 -3.5; 227 -2.1; 249 -1.4; 274 -1.5; 302 -3.1; 332 -5.3; 365 -7.0; 402 -7.9; 442 -8.4; 486 -8.6; 535 -8.8; 588 -8.5; 647 -8.4; 712 -8.1; 783 -7.9; 861 -7.7; 947 -7.5; 1042 -7.5; 1146 -7.5; 1261 -7.8; 1387 -8.2; 1526 -8.5; 1678 -8.7; 1846 -8.5; 2031 -8.2; 2234 -7.8; 2457 -7.3; 2703 -6.8; 2973 -6.4; 3270 -5.8; 3597 -5.0; 3957 -4.0; 4353 -2.6; 4788 -1.9; 5267 -3.4; 5793 -4.6; 6373 -4.7; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -9.1; 10263 -11.7; 11289 -12.0; 12418 -10.5; 13660 -9.0; 15026 -7.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH240 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH240 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1    | 9.6 dB  |
| Peaking | 135 Hz   | 0.16 | -5.4 dB |
| Peaking | 248 Hz   | 1.4  | 10.5 dB |
| Peaking | 4836 Hz  | 2.01 | 4.8 dB  |
| Peaking | 11201 Hz | 2.14 | -6.3 dB |
| Peaking | 453 Hz   | 1.76 | -1.2 dB |
| Peaking | 1374 Hz  | 0.53 | 2.7 dB  |
| Peaking | 1760 Hz  | 1.04 | -3.9 dB |
| Peaking | 5628 Hz  | 5.31 | -1.2 dB |
| Peaking | 6948 Hz  | 4.06 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 6.3 dB  |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SRH240/Shure%20SRH240.png)