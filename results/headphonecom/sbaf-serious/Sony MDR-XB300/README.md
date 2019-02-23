# Sony MDR-XB300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.7; 25 -2.7; 28 -4.0; 31 -5.1; 34 -6.1; 37 -7.1; 41 -8.4; 45 -9.5; 49 -10.3; 54 -10.9; 60 -10.9; 66 -11.3; 72 -12.2; 79 -13.0; 87 -13.6; 96 -13.8; 106 -13.9; 116 -13.6; 128 -13.3; 141 -12.9; 155 -13.0; 170 -13.1; 187 -13.0; 206 -12.8; 227 -11.6; 249 -9.7; 274 -9.9; 302 -9.2; 332 -8.1; 365 -7.1; 402 -6.0; 442 -5.0; 486 -4.2; 535 -3.5; 588 -3.0; 647 -2.6; 712 -2.4; 783 -2.5; 861 -3.4; 947 -5.2; 1042 -6.7; 1146 -7.6; 1261 -8.3; 1387 -9.8; 1526 -10.1; 1678 -10.3; 1846 -10.7; 2031 -10.9; 2234 -11.0; 2457 -10.1; 2703 -8.8; 2973 -6.8; 3270 -4.9; 3597 -2.9; 3957 -2.1; 4353 -1.6; 4788 -0.5; 5267 -0.5; 5793 -0.9; 6373 -5.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.95 | 7.6 dB  |
| Peaking | 54 Hz   | 1.02 | -3.9 dB |
| Peaking | 105 Hz  | 1.33 | -6.2 dB |
| Peaking | 192 Hz  | 2.19 | -5.2 dB |
| Peaking | 4965 Hz | 2.65 | 7.0 dB  |
| Peaking | 297 Hz  | 3    | -2.0 dB |
| Peaking | 700 Hz  | 1.17 | 5.8 dB  |
| Peaking | 1926 Hz | 0.79 | -5.9 dB |
| Peaking | 3623 Hz | 2.33 | 4.4 dB  |
| Peaking | 8800 Hz | 5.56 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB300/Sony%20MDR-XB300.png)