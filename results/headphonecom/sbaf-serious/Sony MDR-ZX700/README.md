# Sony MDR-ZX700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -1.9; 72 -2.4; 79 -2.1; 87 -2.1; 96 -3.7; 106 -5.3; 116 -6.1; 128 -6.6; 141 -6.9; 155 -6.9; 170 -5.9; 187 -6.9; 206 -7.2; 227 -7.5; 249 -7.5; 274 -7.4; 302 -8.0; 332 -8.8; 365 -8.9; 402 -8.4; 442 -8.3; 486 -8.0; 535 -7.3; 588 -6.4; 647 -5.5; 712 -4.9; 783 -5.1; 861 -4.8; 947 -4.8; 1042 -5.0; 1146 -5.0; 1261 -5.3; 1387 -6.1; 1526 -7.5; 1678 -9.0; 1846 -10.7; 2031 -12.2; 2234 -12.2; 2457 -11.0; 2703 -9.8; 2973 -8.7; 3270 -6.4; 3597 -3.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -1.1; 6373 -0.9; 7010 -4.0; 7711 -9.1; 8482 -15.7; 9330 -14.4; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.7  | 7.0 dB   |
| Peaking | 2253 Hz | 2.37 | -6.8 dB  |
| Peaking | 4230 Hz | 2.78 | 6.1 dB   |
| Peaking | 6292 Hz | 2.1  | 6.4 dB   |
| Peaking | 8663 Hz | 3.8  | -12.5 dB |
| Peaking | 87 Hz   | 2.54 | 2.6 dB   |
| Peaking | 119 Hz  | 1.95 | -1.9 dB  |
| Peaking | 223 Hz  | 2.54 | -0.5 dB  |
| Peaking | 384 Hz  | 1.58 | -2.7 dB  |
| Peaking | 893 Hz  | 1.46 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)