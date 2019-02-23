# Sony WH-1000XM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.7; 25 -9.7; 28 -9.6; 31 -9.6; 34 -9.5; 37 -9.4; 41 -9.3; 45 -9.1; 49 -9.0; 54 -9.0; 60 -9.1; 66 -9.4; 72 -9.6; 79 -9.9; 87 -10.2; 96 -10.6; 106 -10.8; 116 -10.9; 128 -10.8; 141 -10.4; 155 -9.9; 170 -9.0; 187 -8.1; 206 -7.1; 227 -6.3; 249 -5.5; 274 -5.0; 302 -4.6; 332 -4.4; 365 -4.3; 402 -4.4; 442 -4.5; 486 -4.8; 535 -5.0; 588 -5.0; 647 -5.0; 712 -4.1; 783 -4.0; 861 -3.9; 947 -3.3; 1042 -2.9; 1146 -2.5; 1261 -2.8; 1387 -3.2; 1526 -5.3; 1678 -5.9; 1846 -6.2; 2031 -6.8; 2234 -6.3; 2457 -4.5; 2703 -3.1; 2973 -3.1; 3270 -2.8; 3597 -3.1; 3957 -3.7; 4353 -2.3; 4788 -0.5; 5267 -2.8; 5793 -2.5; 6373 -3.9; 7010 -4.0; 7711 -6.3; 8482 -8.5; 9330 -8.7; 10263 -7.6; 11289 -5.7; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.52 | -4.4 dB |
| Peaking | 97 Hz   | 1.61 | -3.8 dB |
| Peaking | 145 Hz  | 2.53 | -3.5 dB |
| Peaking | 5150 Hz | 0.88 | 3.7 dB  |
| Peaking | 8905 Hz | 2.29 | -5.3 dB |
| Peaking | 345 Hz  | 2.37 | 1.3 dB  |
| Peaking | 1188 Hz | 1.58 | 3.4 dB  |
| Peaking | 2105 Hz | 1.54 | -4.8 dB |
| Peaking | 2593 Hz | 1.67 | 3.2 dB  |
| Peaking | 3900 Hz | 9.16 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-1000XM3/Sony%20WH-1000XM3.png)