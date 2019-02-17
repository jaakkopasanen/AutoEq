# Sennheiser PMX100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.9; 25 -5.5; 28 -6.3; 31 -6.9; 34 -7.4; 37 -7.8; 41 -8.3; 45 -8.6; 49 -9.0; 54 -9.4; 60 -9.8; 66 -10.1; 72 -10.4; 79 -10.7; 87 -11.1; 96 -11.3; 106 -11.4; 116 -11.4; 128 -11.6; 141 -11.7; 155 -11.6; 170 -11.4; 187 -11.1; 206 -11.0; 227 -10.7; 249 -10.1; 274 -9.6; 302 -9.2; 332 -8.7; 365 -8.4; 402 -8.1; 442 -7.8; 486 -7.5; 535 -7.1; 588 -6.9; 647 -6.7; 712 -6.5; 783 -6.3; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -7.1; 1387 -7.8; 1526 -8.8; 1678 -9.5; 1846 -9.9; 2031 -9.7; 2234 -8.0; 2457 -6.3; 2703 -4.6; 2973 -1.6; 3270 -0.5; 3597 -0.5; 3957 -6.3; 4353 -13.7; 4788 -9.2; 5267 -3.2; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PMX100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PMX100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 128 Hz  | 0.56 | -5.4 dB  |
| Peaking | 1922 Hz | 2.33 | -4.7 dB  |
| Peaking | 3505 Hz | 2.13 | 9.6 dB   |
| Peaking | 4355 Hz | 4.28 | -13.5 dB |
| Peaking | 5821 Hz | 3.4  | 7.2 dB   |
| Peaking | 18 Hz   | 1.4  | 3.3 dB   |
| Peaking | 49 Hz   | 1.68 | -0.7 dB  |
| Peaking | 231 Hz  | 3.97 | -0.5 dB  |
| Peaking | 776 Hz  | 1.98 | 0.8 dB   |
| Peaking | 8254 Hz | 4.59 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PMX100/Sennheiser%20PMX100.png)