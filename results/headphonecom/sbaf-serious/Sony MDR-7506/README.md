# Sony MDR-7506
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.1; 54 -2.0; 60 -2.7; 66 -2.6; 72 -2.5; 79 -3.1; 87 -3.5; 96 -3.8; 106 -4.0; 116 -4.0; 128 -4.1; 141 -3.9; 155 -3.9; 170 -3.7; 187 -3.6; 206 -3.4; 227 -3.5; 249 -3.9; 274 -4.8; 302 -5.3; 332 -6.4; 365 -7.3; 402 -8.2; 442 -8.5; 486 -8.9; 535 -8.9; 588 -8.3; 647 -7.9; 712 -7.9; 783 -7.7; 861 -7.3; 947 -6.6; 1042 -6.5; 1146 -6.6; 1261 -6.8; 1387 -7.4; 1526 -8.0; 1678 -8.2; 1846 -8.0; 2031 -7.7; 2234 -7.8; 2457 -7.6; 2703 -8.3; 2973 -8.9; 3270 -8.3; 3597 -7.6; 3957 -6.8; 4353 -9.8; 4788 -10.5; 5267 -6.2; 5793 -1.4; 6373 -3.5; 7010 -6.8; 7711 -6.7; 8482 -8.4; 9330 -12.0; 10263 -11.5; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.3  | 6.2 dB  |
| Peaking | 211 Hz  | 1.64 | 3.7 dB  |
| Peaking | 1055 Hz | 0.1  | -1.6 dB |
| Peaking | 5933 Hz | 6.85 | 7.4 dB  |
| Peaking | 9651 Hz | 5.2  | -6.0 dB |
| Peaking | 487 Hz  | 3.01 | -1.6 dB |
| Peaking | 1058 Hz | 2.71 | 1.7 dB  |
| Peaking | 3166 Hz | 2.97 | -2.4 dB |
| Peaking | 4211 Hz | 1.47 | 3.6 dB  |
| Peaking | 4605 Hz | 4.61 | -6.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7506/Sony%20MDR-7506.png)