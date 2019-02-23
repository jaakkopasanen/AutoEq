# Sony MDR-XB950N1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.6; 23 -15.8; 25 -15.9; 28 -16.0; 31 -16.1; 34 -16.0; 37 -15.9; 41 -15.7; 45 -15.6; 49 -15.4; 54 -15.3; 60 -15.2; 66 -15.2; 72 -15.3; 79 -15.6; 87 -16.0; 96 -16.4; 106 -16.6; 116 -16.5; 128 -16.1; 141 -15.6; 155 -15.0; 170 -14.2; 187 -13.4; 206 -12.3; 227 -11.0; 249 -9.7; 274 -8.3; 302 -7.2; 332 -6.7; 365 -6.7; 402 -7.0; 442 -7.5; 486 -7.9; 535 -8.2; 588 -8.4; 647 -8.4; 712 -8.3; 783 -8.2; 861 -8.2; 947 -8.2; 1042 -8.3; 1146 -8.5; 1261 -8.5; 1387 -8.2; 1526 -8.0; 1678 -7.9; 1846 -7.6; 2031 -6.6; 2234 -4.9; 2457 -3.0; 2703 -1.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -2.6; 4788 -5.5; 5267 -2.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB950N1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB950N1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.34 | -9.2 dB |
| Peaking | 127 Hz   | 1.07 | -7.0 dB |
| Peaking | 1490 Hz  | 0.73 | -2.8 dB |
| Peaking | 3152 Hz  | 1.54 | 7.6 dB  |
| Peaking | 6012 Hz  | 4.4  | 5.7 dB  |
| Peaking | 201 Hz   | 3.36 | -1.4 dB |
| Peaking | 333 Hz   | 2.02 | 2.1 dB  |
| Peaking | 574 Hz   | 2.24 | -1.0 dB |
| Peaking | 13333 Hz | 2.2  | -0.4 dB |
| Peaking | 22042 Hz | 1.71 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -9.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-XB950N1/Sony%20MDR-XB950N1.png)