# Sony WH-1000XM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.0; 25 -8.9; 28 -8.9; 31 -8.8; 34 -8.8; 37 -8.7; 41 -8.5; 45 -8.4; 49 -8.3; 54 -8.3; 60 -8.4; 66 -8.6; 72 -8.8; 79 -9.1; 87 -9.4; 96 -9.8; 106 -10.0; 116 -10.1; 128 -10.0; 141 -9.6; 155 -9.1; 170 -8.3; 187 -7.3; 206 -6.4; 227 -5.6; 249 -4.8; 274 -4.3; 302 -4.0; 332 -3.8; 365 -3.7; 402 -3.8; 442 -4.0; 486 -4.3; 535 -4.4; 588 -4.5; 647 -4.5; 712 -3.7; 783 -3.5; 861 -3.4; 947 -2.8; 1042 -2.4; 1146 -2.0; 1261 -2.3; 1387 -2.9; 1526 -4.9; 1678 -5.6; 1846 -6.0; 2031 -6.7; 2234 -6.5; 2457 -4.8; 2703 -3.0; 2973 -2.5; 3270 -2.0; 3597 -2.3; 3957 -2.8; 4353 -1.2; 4788 -0.5; 5267 -2.5; 5793 -2.0; 6373 -2.4; 7010 -3.6; 7711 -6.6; 8482 -7.7; 9330 -6.4; 10263 -6.4; 11289 -5.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.5  | -4.2 dB |
| Peaking | 99 Hz   | 1.59 | -3.6 dB |
| Peaking | 145 Hz  | 2.56 | -3.2 dB |
| Peaking | 1074 Hz | 2.56 | 2.8 dB  |
| Peaking | 4591 Hz | 2.29 | 4.0 dB  |
| Peaking | 349 Hz  | 2.03 | 1.4 dB  |
| Peaking | 2100 Hz | 3.05 | -3.0 dB |
| Peaking | 2950 Hz | 3.09 | 2.3 dB  |
| Peaking | 6658 Hz | 2.95 | 4.6 dB  |
| Peaking | 7899 Hz | 1.68 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-1000XM3/Sony%20WH-1000XM3.png)