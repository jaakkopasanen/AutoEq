# Sony MDR-XB300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -2.1; 25 -3.2; 28 -4.4; 31 -5.6; 34 -6.6; 37 -7.6; 41 -8.9; 45 -10.0; 49 -10.8; 54 -11.4; 60 -11.4; 66 -11.7; 72 -12.7; 79 -13.5; 87 -14.0; 96 -14.3; 106 -14.3; 116 -14.1; 128 -13.7; 141 -13.4; 155 -13.5; 170 -13.6; 187 -13.5; 206 -13.2; 227 -12.0; 249 -10.2; 274 -10.4; 302 -9.7; 332 -8.6; 365 -7.5; 402 -6.5; 442 -5.5; 486 -4.6; 535 -4.0; 588 -3.5; 647 -3.0; 712 -2.8; 783 -2.9; 861 -3.8; 947 -5.6; 1042 -7.1; 1146 -8.1; 1261 -8.7; 1387 -10.2; 1526 -10.6; 1678 -10.8; 1846 -11.1; 2031 -11.3; 2234 -11.4; 2457 -10.6; 2703 -9.3; 2973 -7.3; 3270 -5.3; 3597 -3.4; 3957 -2.5; 4353 -2.1; 4788 -0.5; 5267 -0.5; 5793 -1.0; 6373 -5.6; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.7
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
| Peaking | 18 Hz   | 0.94 | 7.3 dB  |
| Peaking | 53 Hz   | 0.99 | -4.0 dB |
| Peaking | 104 Hz  | 1.25 | -6.4 dB |
| Peaking | 194 Hz  | 1.99 | -5.4 dB |
| Peaking | 5015 Hz | 2.96 | 7.0 dB  |
| Peaking | 303 Hz  | 3.09 | -2.0 dB |
| Peaking | 727 Hz  | 1.04 | 6.9 dB  |
| Peaking | 2046 Hz | 0.47 | -7.0 dB |
| Peaking | 3606 Hz | 2.06 | 6.4 dB  |
| Peaking | 6206 Hz | 1.59 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB300/Sony%20MDR-XB300.png)