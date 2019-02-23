# Ortofon 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.4; 45 -2.2; 49 -2.9; 54 -3.5; 60 -3.9; 66 -3.3; 72 -3.0; 79 -3.6; 87 -4.3; 96 -4.4; 106 -4.3; 116 -4.1; 128 -4.2; 141 -4.4; 155 -4.4; 170 -4.1; 187 -4.2; 206 -4.8; 227 -5.0; 249 -6.4; 274 -7.6; 302 -9.3; 332 -10.7; 365 -11.4; 402 -11.1; 442 -10.7; 486 -10.4; 535 -10.2; 588 -9.9; 647 -9.5; 712 -9.3; 783 -9.2; 861 -9.3; 947 -9.5; 1042 -9.7; 1146 -9.6; 1261 -9.0; 1387 -9.1; 1526 -9.2; 1678 -10.2; 1846 -10.7; 2031 -10.0; 2234 -8.9; 2457 -7.5; 2703 -6.2; 2973 -6.2; 3270 -6.8; 3597 -5.4; 3957 -6.5; 4353 -2.0; 4788 -1.1; 5267 -3.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.9; 9330 -12.9; 10263 -13.6; 11289 -10.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ortofon 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.08 | 4.6 dB  |
| Peaking | 387 Hz  | 1.82 | -4.9 dB |
| Peaking | 1427 Hz | 0.49 | -3.5 dB |
| Peaking | 5708 Hz | 1.18 | 6.8 dB  |
| Peaking | 9808 Hz | 2.76 | -9.6 dB |
| Peaking | 31 Hz   | 0.94 | 3.5 dB  |
| Peaking | 50 Hz   | 0.62 | -2.4 dB |
| Peaking | 198 Hz  | 2.53 | 1.6 dB  |
| Peaking | 1884 Hz | 6.14 | -1.6 dB |
| Peaking | 2721 Hz | 7.57 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | 2.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | -4.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ortofon%202/Ortofon%202.png)