# Cardas EM5813
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.0; 25 -12.0; 28 -12.0; 31 -12.1; 34 -12.1; 37 -12.0; 41 -12.0; 45 -12.2; 49 -12.3; 54 -12.5; 60 -12.6; 66 -12.9; 72 -13.1; 79 -13.3; 87 -13.5; 96 -13.6; 106 -13.7; 116 -13.8; 128 -13.8; 141 -13.8; 155 -13.8; 170 -13.6; 187 -13.4; 206 -13.1; 227 -12.7; 249 -12.3; 274 -11.9; 302 -11.2; 332 -10.6; 365 -10.0; 402 -9.4; 442 -8.8; 486 -8.2; 535 -7.5; 588 -6.8; 647 -6.2; 712 -5.8; 783 -5.6; 861 -4.8; 947 -2.1; 1042 -3.8; 1146 -4.4; 1261 -4.8; 1387 -5.4; 1526 -6.2; 1678 -6.7; 1846 -7.0; 2031 -7.6; 2234 -8.6; 2457 -10.5; 2703 -9.1; 2973 -5.1; 3270 -2.6; 3597 -2.2; 3957 -5.1; 4353 -9.9; 4788 -7.6; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 33 Hz   | 0.29 | -5.4 dB |
| Peaking | 135 Hz  | 0.87 | -4.7 dB |
| Peaking | 261 Hz  | 1.55 | -3.2 dB |
| Peaking | 3465 Hz | 8.12 | 4.8 dB  |
| Peaking | 5960 Hz | 4.59 | 7.0 dB  |
| Peaking | 975 Hz  | 2.75 | 4.0 dB  |
| Peaking | 2553 Hz | 3.28 | -7.0 dB |
| Peaking | 2988 Hz | 2.29 | 3.9 dB  |
| Peaking | 4503 Hz | 6.78 | -5.9 dB |
| Peaking | 5266 Hz | 9.73 | 3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Cardas%20EM5813/Cardas%20EM5813.png)