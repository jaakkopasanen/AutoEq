# Cardas EM5813
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.0; 23 -15.0; 25 -15.0; 28 -15.0; 31 -15.1; 34 -15.0; 37 -15.0; 41 -15.0; 45 -15.2; 49 -15.3; 54 -15.5; 60 -15.6; 66 -15.9; 72 -16.1; 79 -16.3; 87 -16.5; 96 -16.6; 106 -16.7; 116 -16.7; 128 -16.8; 141 -16.8; 155 -16.8; 170 -16.6; 187 -16.4; 206 -16.1; 227 -15.7; 249 -15.3; 274 -14.9; 302 -14.2; 332 -13.6; 365 -13.0; 402 -12.3; 442 -11.7; 486 -11.2; 535 -10.5; 588 -9.8; 647 -9.2; 712 -8.8; 783 -8.6; 861 -7.8; 947 -5.1; 1042 -6.8; 1146 -7.4; 1261 -7.8; 1387 -8.4; 1526 -9.2; 1678 -9.7; 1846 -10.0; 2031 -10.6; 2234 -11.6; 2457 -13.5; 2703 -12.1; 2973 -8.1; 3270 -5.6; 3597 -5.2; 3957 -8.1; 4353 -12.9; 4788 -10.6; 5267 -3.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cardas EM5813 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cardas EM5813 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.19 | -7.9 dB |
| Peaking | 141 Hz  | 0.6  | -5.8 dB |
| Peaking | 308 Hz  | 0.82 | -4.0 dB |
| Peaking | 2361 Hz | 2.2  | -6.3 dB |
| Peaking | 6083 Hz | 5.38 | 7.3 dB  |
| Peaking | 953 Hz  | 6.04 | 3.3 dB  |
| Peaking | 1291 Hz | 0.52 | -0.6 dB |
| Peaking | 3478 Hz | 3.99 | 4.6 dB  |
| Peaking | 4482 Hz | 4.7  | -8.0 dB |
| Peaking | 5418 Hz | 7.58 | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -7.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Cardas%20EM5813/Cardas%20EM5813.png)