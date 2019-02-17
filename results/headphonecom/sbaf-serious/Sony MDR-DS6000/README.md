# Sony MDR-DS6000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.5; 60 -2.5; 66 -3.9; 72 -5.3; 79 -6.5; 87 -7.5; 96 -8.3; 106 -8.8; 116 -9.2; 128 -9.3; 141 -9.2; 155 -9.1; 170 -8.7; 187 -8.7; 206 -8.1; 227 -8.0; 249 -8.0; 274 -7.7; 302 -7.3; 332 -7.1; 365 -6.9; 402 -6.7; 442 -6.2; 486 -6.5; 535 -6.9; 588 -7.1; 647 -7.4; 712 -7.9; 783 -8.1; 861 -7.7; 947 -6.4; 1042 -7.0; 1146 -8.1; 1261 -9.2; 1387 -9.4; 1526 -10.2; 1678 -11.1; 1846 -11.7; 2031 -12.2; 2234 -11.3; 2457 -9.3; 2703 -6.9; 2973 -5.1; 3270 -3.2; 3597 -1.0; 3957 -0.5; 4353 -2.3; 4788 -1.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-DS6000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS6000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.42 | 8.5 dB  |
| Peaking | 106 Hz  | 0.72 | -7.4 dB |
| Peaking | 1989 Hz | 1.42 | -6.6 dB |
| Peaking | 3696 Hz | 1.92 | 6.6 dB  |
| Peaking | 5754 Hz | 2.96 | 5.6 dB  |
| Peaking | 14 Hz   | 2.35 | 1.0 dB  |
| Peaking | 448 Hz  | 3.63 | 1.0 dB  |
| Peaking | 861 Hz  | 1.93 | -1.6 dB |
| Peaking | 969 Hz  | 4.88 | 2.6 dB  |
| Peaking | 8220 Hz | 4.65 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -7.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-DS6000/Sony%20MDR-DS6000.png)