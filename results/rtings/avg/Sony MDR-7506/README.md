# Sony MDR-7506
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.6; 25 -7.1; 28 -7.7; 31 -8.2; 34 -8.6; 37 -8.7; 41 -8.8; 45 -8.8; 49 -8.8; 54 -8.7; 60 -8.5; 66 -8.3; 72 -8.1; 79 -7.8; 87 -7.8; 96 -7.7; 106 -7.7; 116 -7.4; 128 -6.9; 141 -6.4; 155 -5.9; 170 -5.2; 187 -4.3; 206 -3.3; 227 -2.0; 249 -0.5; 274 -1.2; 302 -3.5; 332 -4.2; 365 -4.4; 402 -4.6; 442 -4.6; 486 -4.6; 535 -4.5; 588 -4.3; 647 -3.9; 712 -3.6; 783 -3.4; 861 -2.9; 947 -2.6; 1042 -2.8; 1146 -3.2; 1261 -3.5; 1387 -3.9; 1526 -4.7; 1678 -5.4; 1846 -6.2; 2031 -7.0; 2234 -6.6; 2457 -6.2; 2703 -7.1; 2973 -8.3; 3270 -8.2; 3597 -7.3; 3957 -7.9; 4353 -10.3; 4788 -8.0; 5267 -4.0; 5793 -1.1; 6373 -1.7; 7010 -3.8; 7711 -5.7; 8482 -7.7; 9330 -10.0; 10263 -11.0; 11289 -7.5; 12418 -2.7; 13660 -2.7; 15026 -2.7; 16529 -2.7; 18182 -2.7; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.48 | -6.5 dB |
| Peaking | 486 Hz  | 2.84 | -1.8 dB |
| Peaking | 2683 Hz | 1.24 | -4.9 dB |
| Peaking | 4378 Hz | 5.89 | -6.1 dB |
| Peaking | 9838 Hz | 3.12 | -9.1 dB |
| Peaking | 237 Hz  | 0.79 | -1.9 dB |
| Peaking | 247 Hz  | 2.95 | 5.4 dB  |
| Peaking | 984 Hz  | 3.86 | 1.0 dB  |
| Peaking | 5926 Hz | 1.24 | -2.1 dB |
| Peaking | 6011 Hz | 3.64 | 5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-7506/Sony%20MDR-7506.png)