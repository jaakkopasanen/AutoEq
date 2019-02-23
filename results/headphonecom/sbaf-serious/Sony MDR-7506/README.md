# Sony MDR-7506
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.9; 54 -1.7; 60 -2.5; 66 -2.4; 72 -2.3; 79 -2.8; 87 -3.3; 96 -3.5; 106 -3.7; 116 -3.7; 128 -3.8; 141 -3.7; 155 -3.6; 170 -3.5; 187 -3.4; 206 -3.1; 227 -3.2; 249 -3.7; 274 -4.6; 302 -5.1; 332 -6.2; 365 -7.1; 402 -8.0; 442 -8.2; 486 -8.6; 535 -8.7; 588 -8.1; 647 -7.7; 712 -7.6; 783 -7.4; 861 -7.1; 947 -6.4; 1042 -6.3; 1146 -6.4; 1261 -6.6; 1387 -7.2; 1526 -7.7; 1678 -8.0; 1846 -7.8; 2031 -7.5; 2234 -7.5; 2457 -7.4; 2703 -8.0; 2973 -8.7; 3270 -8.0; 3597 -7.4; 3957 -6.5; 4353 -9.6; 4788 -10.2; 5267 -6.0; 5793 -1.2; 6373 -3.2; 7010 -6.6; 7711 -6.4; 8482 -8.2; 9330 -11.7; 10263 -11.2; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7506 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7506 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.3  | 6.2 dB  |
| Peaking | 211 Hz  | 1.67 | 3.6 dB  |
| Peaking | 1055 Hz | 0.1  | -1.4 dB |
| Peaking | 5962 Hz | 6.76 | 7.4 dB  |
| Peaking | 9698 Hz | 5.28 | -5.9 dB |
| Peaking | 296 Hz  | 3.6  | 0.9 dB  |
| Peaking | 468 Hz  | 2.01 | -1.6 dB |
| Peaking | 1059 Hz | 2.51 | 1.7 dB  |
| Peaking | 4739 Hz | 5.73 | -5.9 dB |
| Peaking | 4875 Hz | 2.16 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 1.8 dB  |
| Peaking | 250 Hz   | 1.41 | 3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7506/Sony%20MDR-7506.png)