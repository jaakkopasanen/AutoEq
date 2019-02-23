# Sony MDR-XB700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.8; 23 -14.6; 25 -14.4; 28 -13.8; 31 -13.4; 34 -13.6; 37 -14.2; 41 -14.5; 45 -13.7; 49 -12.2; 54 -11.0; 60 -12.1; 66 -14.3; 72 -15.7; 79 -16.5; 87 -16.7; 96 -16.7; 106 -16.3; 116 -15.6; 128 -14.7; 141 -13.6; 155 -13.0; 170 -12.8; 187 -12.2; 206 -10.9; 227 -9.6; 249 -8.2; 274 -7.3; 302 -6.2; 332 -5.2; 365 -4.8; 402 -4.6; 442 -4.2; 486 -3.5; 535 -2.4; 588 -1.7; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -1.9; 1042 -4.3; 1146 -5.9; 1261 -7.6; 1387 -9.0; 1526 -10.2; 1678 -10.7; 1846 -10.5; 2031 -9.9; 2234 -8.4; 2457 -6.1; 2703 -3.9; 2973 -1.1; 3270 -0.5; 3597 -0.9; 3957 -6.5; 4353 -5.9; 4788 -7.3; 5267 -10.2; 5793 -12.0; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.9; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.2; 16529 -6.5; 18182 -6.5; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 1.36 | -7.6 dB  |
| Peaking | 39 Hz   | 3.45 | -3.7 dB  |
| Peaking | 99 Hz   | 0.86 | -10.3 dB |
| Peaking | 658 Hz  | 1.68 | 7.1 dB   |
| Peaking | 3250 Hz | 5.62 | 7.2 dB   |
| Peaking | 905 Hz  | 5.39 | 3.0 dB   |
| Peaking | 1702 Hz | 1.46 | -7.1 dB  |
| Peaking | 3137 Hz | 0.29 | 2.3 dB   |
| Peaking | 5519 Hz | 6.96 | -8.6 dB  |
| Peaking | 9628 Hz | 4.94 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -8.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 5.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB700/Sony%20MDR-XB700.png)