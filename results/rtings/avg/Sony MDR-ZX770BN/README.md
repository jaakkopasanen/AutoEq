# Sony MDR-ZX770BN
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -7.1; 25 -7.7; 28 -8.5; 31 -9.1; 34 -9.4; 37 -9.6; 41 -9.7; 45 -9.8; 49 -9.7; 54 -9.7; 60 -9.5; 66 -9.4; 72 -9.2; 79 -9.0; 87 -8.7; 96 -8.5; 106 -8.5; 116 -8.6; 128 -8.7; 141 -8.4; 155 -7.9; 170 -8.2; 187 -9.0; 206 -8.8; 227 -8.4; 249 -8.2; 274 -7.9; 302 -7.4; 332 -6.7; 365 -5.7; 402 -4.6; 442 -3.6; 486 -2.7; 535 -1.8; 588 -1.9; 647 -1.9; 712 -2.1; 783 -2.3; 861 -2.1; 947 -2.1; 1042 -2.2; 1146 -2.7; 1261 -2.7; 1387 -2.5; 1526 -3.1; 1678 -5.0; 1846 -7.8; 2031 -9.8; 2234 -8.9; 2457 -7.1; 2703 -6.0; 2973 -6.2; 3270 -4.5; 3597 -0.5; 3957 -7.4; 4353 -11.2; 4788 -12.3; 5267 -10.1; 5793 -5.2; 6373 -3.4; 7010 -4.4; 7711 -8.1; 8482 -11.6; 9330 -12.1; 10263 -11.2; 11289 -10.1; 12418 -8.2; 13660 -7.0; 15026 -9.6; 16529 -13.8; 18182 -14.0; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX770BN GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX770BN ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 67 Hz    |  0.23 | -7.6 dB  |
| Peaking | 2112 Hz  |  3.13 | -7.8 dB  |
| Peaking | 4689 Hz  |  4.3  | -10.3 dB |
| Peaking | 9387 Hz  |  2.17 | -9.0 dB  |
| Peaking | 17721 Hz |  0.79 | -13.0 dB |
| Peaking | 271 Hz   |  0.91 | -6.7 dB  |
| Peaking | 328 Hz   |  0.48 | 5.0 dB   |
| Peaking | 3600 Hz  | 10.39 | 6.4 dB   |
| Peaking | 4456 Hz  |  0.67 | -1.9 dB  |
| Peaking | 6405 Hz  |  3.97 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.8 dB  |
| Peaking | 62 Hz    | 1.41 | -5.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -6.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB  |
| Peaking | 16000 Hz | 1.41 | -14.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-ZX770BN/Sony%20MDR-ZX770BN.png)