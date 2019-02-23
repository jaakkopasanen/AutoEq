# Sony MDR-V700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -2.3; 72 -3.7; 79 -5.2; 87 -6.3; 96 -7.1; 106 -7.1; 116 -7.2; 128 -7.2; 141 -6.9; 155 -6.7; 170 -6.1; 187 -5.8; 206 -5.6; 227 -5.2; 249 -4.5; 274 -4.0; 302 -3.8; 332 -3.6; 365 -3.9; 402 -2.4; 442 -3.1; 486 -4.9; 535 -7.1; 588 -8.2; 647 -8.2; 712 -7.7; 783 -6.5; 861 -8.4; 947 -8.0; 1042 -7.1; 1146 -6.4; 1261 -7.0; 1387 -8.5; 1526 -9.9; 1678 -11.0; 1846 -11.0; 2031 -11.7; 2234 -12.5; 2457 -12.2; 2703 -11.5; 2973 -9.9; 3270 -8.3; 3597 -6.8; 3957 -4.6; 4353 -2.7; 4788 -0.5; 5267 -0.5; 5793 -3.2; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -8.7; 9330 -11.9; 10263 -8.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.9  | 7.2 dB  |
| Peaking | 365 Hz  | 2.17 | 3.8 dB  |
| Peaking | 2463 Hz | 1.02 | -7.6 dB |
| Peaking | 4998 Hz | 1.17 | 7.9 dB  |
| Peaking | 9231 Hz | 4.02 | -7.1 dB |
| Peaking | 60 Hz   | 2.17 | 4.5 dB  |
| Peaking | 90 Hz   | 0.65 | -2.9 dB |
| Peaking | 224 Hz  | 0.98 | 1.5 dB  |
| Peaking | 609 Hz  | 4.31 | -2.3 dB |
| Peaking | 1183 Hz | 6.85 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | 2.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V700/Sony%20MDR-V700.png)