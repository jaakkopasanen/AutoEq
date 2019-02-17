# Sony MDR-G75
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.6; 49 -2.7; 54 -4.0; 60 -5.3; 66 -6.4; 72 -7.3; 79 -8.2; 87 -8.9; 96 -9.5; 106 -9.9; 116 -10.3; 128 -10.4; 141 -10.5; 155 -10.5; 170 -10.4; 187 -10.1; 206 -9.8; 227 -9.4; 249 -9.0; 274 -8.6; 302 -7.8; 332 -7.3; 365 -6.7; 402 -6.3; 442 -6.7; 486 -6.6; 535 -6.4; 588 -6.2; 647 -6.1; 712 -6.0; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -6.8; 1261 -7.0; 1387 -7.7; 1526 -8.8; 1678 -10.0; 1846 -9.8; 2031 -7.9; 2234 -5.8; 2457 -3.3; 2703 -1.3; 2973 -1.1; 3270 -2.1; 3597 -5.2; 3957 -8.6; 4353 -8.1; 4788 -3.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-G75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-G75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.71 | 7.2 dB  |
| Peaking | 122 Hz  | 0.78 | -5.2 dB |
| Peaking | 2957 Hz | 2.35 | 12.8 dB |
| Peaking | 3910 Hz | 0.72 | -9.8 dB |
| Peaking | 5638 Hz | 1.93 | 13.0 dB |
| Peaking | 232 Hz  | 1.63 | -1.5 dB |
| Peaking | 707 Hz  | 0.26 | 1.2 dB  |
| Peaking | 1742 Hz | 3.28 | -3.4 dB |
| Peaking | 2384 Hz | 5.76 | 1.4 dB  |
| Peaking | 4165 Hz | 9.91 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-G75/Sony%20MDR-G75.png)