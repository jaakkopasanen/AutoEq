# Shure SRH1540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.7; 25 -6.2; 28 -6.9; 31 -7.4; 34 -7.8; 37 -8.1; 41 -8.5; 45 -8.8; 49 -8.9; 54 -9.0; 60 -9.1; 66 -9.0; 72 -8.7; 79 -8.2; 87 -7.7; 96 -7.3; 106 -7.2; 116 -7.2; 128 -7.0; 141 -6.5; 155 -5.4; 170 -4.3; 187 -5.0; 206 -4.8; 227 -5.2; 249 -5.4; 274 -5.4; 302 -5.7; 332 -5.8; 365 -5.5; 402 -4.9; 442 -4.3; 486 -3.8; 535 -3.4; 588 -2.8; 647 -2.2; 712 -1.7; 783 -1.3; 861 -1.2; 947 -1.1; 1042 -1.4; 1146 -1.1; 1261 -1.1; 1387 -1.8; 1526 -2.8; 1678 -3.8; 1846 -4.5; 2031 -4.5; 2234 -3.7; 2457 -3.1; 2703 -2.1; 2973 -1.0; 3270 -1.4; 3597 -1.0; 3957 -1.9; 4353 -2.2; 4788 -1.9; 5267 -0.5; 5793 -2.9; 6373 -4.0; 7010 -2.2; 7711 -1.9; 8482 -3.7; 9330 -5.9; 10263 -3.6; 11289 -1.3; 12418 -1.3; 13660 -1.3; 15026 -1.3; 16529 -1.3; 18182 -1.9; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.59 | -5.4 dB |
| Peaking | 89 Hz    | 0.58 | -3.9 dB |
| Peaking | 340 Hz   | 1.28 | -3.5 dB |
| Peaking | 9314 Hz  | 3.8  | -4.8 dB |
| Peaking | 57 Hz    | 2.84 | -0.1 dB |
| Peaking | 1634 Hz  | 0.76 | 1.9 dB  |
| Peaking | 1909 Hz  | 1.9  | -5.1 dB |
| Peaking | 6179 Hz  | 9.51 | -3.2 dB |
| Peaking | 19930 Hz | 1.96 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1540/Shure%20SRH1540.png)