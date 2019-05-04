# Sony MDR-XB950B1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.5; 23 -14.7; 25 -14.9; 28 -15.1; 31 -15.1; 34 -15.1; 37 -15.0; 41 -14.9; 45 -14.9; 49 -14.8; 54 -14.9; 60 -15.0; 66 -15.2; 72 -15.4; 79 -15.7; 87 -16.1; 96 -16.4; 106 -16.6; 116 -16.7; 128 -16.7; 141 -16.4; 155 -15.8; 170 -15.1; 187 -14.9; 206 -14.0; 227 -12.8; 249 -11.3; 274 -9.4; 302 -7.0; 332 -4.5; 365 -3.2; 402 -4.4; 442 -6.6; 486 -8.3; 535 -9.1; 588 -9.4; 647 -9.4; 712 -9.3; 783 -9.1; 861 -8.8; 947 -8.5; 1042 -8.0; 1146 -7.3; 1261 -7.2; 1387 -6.9; 1526 -6.6; 1678 -6.4; 1846 -6.1; 2031 -6.1; 2234 -5.8; 2457 -4.6; 2703 -2.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.1; 4353 -5.3; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB950B1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB950B1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.35 | -8.4 dB |
| Peaking | 137 Hz  | 1.14 | -7.5 dB |
| Peaking | 2841 Hz | 0.29 | -2.1 dB |
| Peaking | 3197 Hz | 1.74 | 8.0 dB  |
| Peaking | 5787 Hz | 2.54 | 7.1 dB  |
| Peaking | 43 Hz   | 2.86 | 0.6 dB  |
| Peaking | 222 Hz  | 3.11 | -2.4 dB |
| Peaking | 365 Hz  | 2.63 | 7.0 dB  |
| Peaking | 580 Hz  | 1.09 | -2.7 dB |
| Peaking | 1418 Hz | 2.07 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB  |
| Peaking | 62 Hz    | 1.41 | -5.4 dB  |
| Peaking | 125 Hz   | 1.41 | -10.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20MDR-XB950B1/Sony%20MDR-XB950B1.png)