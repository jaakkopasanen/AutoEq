# Sony MDR-XB950N1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.4; 23 -15.6; 25 -15.7; 28 -15.8; 31 -15.9; 34 -15.8; 37 -15.7; 41 -15.6; 45 -15.4; 49 -15.3; 54 -15.1; 60 -15.0; 66 -15.0; 72 -15.1; 79 -15.4; 87 -15.8; 96 -16.2; 106 -16.4; 116 -16.2; 128 -15.9; 141 -15.4; 155 -14.8; 170 -14.1; 187 -13.2; 206 -12.1; 227 -10.9; 249 -9.6; 274 -8.3; 302 -7.2; 332 -6.7; 365 -6.6; 402 -7.0; 442 -7.5; 486 -8.0; 535 -8.3; 588 -8.5; 647 -8.5; 712 -8.5; 783 -8.4; 861 -8.3; 947 -8.4; 1042 -8.4; 1146 -8.6; 1261 -8.7; 1387 -8.4; 1526 -8.1; 1678 -8.0; 1846 -7.9; 2031 -7.0; 2234 -5.7; 2457 -4.0; 2703 -2.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.5; 4788 -5.7; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB950N1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB950N1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.34 | -9.1 dB |
| Peaking | 127 Hz   | 1.08 | -6.8 dB |
| Peaking | 1611 Hz  | 0.62 | -3.0 dB |
| Peaking | 3215 Hz  | 1.61 | 8.1 dB  |
| Peaking | 6031 Hz  | 4.45 | 5.8 dB  |
| Peaking | 203 Hz   | 3.17 | -1.5 dB |
| Peaking | 335 Hz   | 1.87 | 2.1 dB  |
| Peaking | 573 Hz   | 2.07 | -1.1 dB |
| Peaking | 8294 Hz  | 4.34 | -0.8 dB |
| Peaking | 17073 Hz | 2.17 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -9.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-XB950N1/Sony%20MDR-XB950N1.png)