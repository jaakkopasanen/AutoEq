# Sony WI-C300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.8; 31 -2.4; 34 -2.9; 37 -3.4; 41 -4.0; 45 -4.5; 49 -5.0; 54 -5.5; 60 -6.1; 66 -6.6; 72 -7.1; 79 -7.6; 87 -8.1; 96 -8.6; 106 -9.0; 116 -9.3; 128 -9.5; 141 -9.6; 155 -9.6; 170 -9.5; 187 -9.3; 206 -9.1; 227 -8.7; 249 -8.3; 274 -7.8; 302 -7.3; 332 -7.1; 365 -6.8; 402 -6.4; 442 -6.0; 486 -5.5; 535 -4.9; 588 -4.4; 647 -3.8; 712 -3.2; 783 -2.8; 861 -2.9; 947 -3.4; 1042 -4.3; 1146 -5.3; 1261 -6.0; 1387 -6.3; 1526 -6.7; 1678 -7.2; 1846 -7.7; 2031 -8.0; 2234 -7.9; 2457 -7.3; 2703 -6.8; 2973 -6.5; 3270 -6.7; 3597 -7.1; 3957 -7.8; 4353 -8.8; 4788 -9.9; 5267 -9.3; 5793 -6.3; 6373 -3.1; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.8; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-C300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-C300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.64 | 6.1 dB  |
| Peaking | 139 Hz  | 0.75 | -3.7 dB |
| Peaking | 764 Hz  | 1.74 | 4.1 dB  |
| Peaking | 5341 Hz | 1.66 | -5.0 dB |
| Peaking | 6395 Hz | 3.47 | 7.1 dB  |
| Peaking | 493 Hz  | 3.82 | 0.4 dB  |
| Peaking | 974 Hz  | 6.14 | 0.9 dB  |
| Peaking | 2157 Hz | 1.56 | -2.1 dB |
| Peaking | 2928 Hz | 2.05 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-C300/Sony%20WI-C300.png)