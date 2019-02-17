# Sony MDR-ZX700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.9; 60 -2.4; 66 -3.5; 72 -4.0; 79 -3.7; 87 -3.7; 96 -5.2; 106 -6.9; 116 -7.7; 128 -8.1; 141 -8.5; 155 -8.4; 170 -7.5; 187 -8.5; 206 -8.8; 227 -9.1; 249 -9.1; 274 -9.0; 302 -9.5; 332 -10.4; 365 -10.5; 402 -10.0; 442 -9.9; 486 -9.5; 535 -8.9; 588 -8.0; 647 -7.1; 712 -6.5; 783 -6.7; 861 -6.4; 947 -6.3; 1042 -6.6; 1146 -6.5; 1261 -6.8; 1387 -7.7; 1526 -9.0; 1678 -10.6; 1846 -12.3; 2031 -13.8; 2234 -13.7; 2457 -12.6; 2703 -11.4; 2973 -10.3; 3270 -8.0; 3597 -5.1; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -3.2; 5793 -2.7; 6373 -2.8; 7010 -4.0; 7711 -10.7; 8482 -17.2; 9330 -16.0; 10263 -9.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-ZX700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.99 | 7.2 dB   |
| Peaking | 2270 Hz  | 1.57 | -8.1 dB  |
| Peaking | 4251 Hz  | 3.16 | 6.6 dB   |
| Peaking | 6633 Hz  | 1.39 | 6.5 dB   |
| Peaking | 8635 Hz  | 3.35 | -16.0 dB |
| Peaking | 134 Hz   | 3.87 | -2.2 dB  |
| Peaking | 214 Hz   | 2.56 | -1.5 dB  |
| Peaking | 386 Hz   | 1.37 | -4.0 dB  |
| Peaking | 970 Hz   | 1.45 | 1.6 dB   |
| Peaking | 11047 Hz | 7.59 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)