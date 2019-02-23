# Phiaton MS 300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.6; 34 -2.6; 37 -3.5; 41 -4.4; 45 -5.2; 49 -6.2; 54 -7.0; 60 -7.7; 66 -8.2; 72 -8.4; 79 -8.4; 87 -8.5; 96 -8.8; 106 -9.0; 116 -9.1; 128 -9.2; 141 -9.2; 155 -9.1; 170 -9.0; 187 -8.9; 206 -8.5; 227 -8.2; 249 -8.2; 274 -8.1; 302 -8.2; 332 -8.2; 365 -8.1; 402 -7.5; 442 -7.7; 486 -7.3; 535 -6.9; 588 -6.7; 647 -6.5; 712 -7.0; 783 -8.3; 861 -9.3; 947 -10.5; 1042 -11.8; 1146 -12.9; 1261 -13.3; 1387 -13.4; 1526 -12.7; 1678 -12.2; 1846 -12.1; 2031 -10.2; 2234 -7.9; 2457 -4.8; 2703 -2.2; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.4; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton MS 300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.69 | 7.1 dB  |
| Peaking | 60 Hz   | 0.79 | -3.1 dB |
| Peaking | 153 Hz  | 0.86 | -2.2 dB |
| Peaking | 1534 Hz | 1.12 | -9.4 dB |
| Peaking | 3598 Hz | 0.91 | 8.6 dB  |
| Peaking | 653 Hz  | 3.63 | 1.8 dB  |
| Peaking | 1086 Hz | 4.65 | -1.5 dB |
| Peaking | 4034 Hz | 3.57 | -1.9 dB |
| Peaking | 6318 Hz | 1.23 | 4.4 dB  |
| Peaking | 7739 Hz | 1.38 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.1 dB |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 9.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20300/Phiaton%20MS%20300.png)