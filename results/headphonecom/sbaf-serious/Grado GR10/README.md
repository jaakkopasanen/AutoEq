# Grado GR10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -2.9; 25 -3.0; 28 -3.1; 31 -3.1; 34 -3.2; 37 -3.3; 41 -3.5; 45 -3.7; 49 -3.8; 54 -4.1; 60 -4.4; 66 -4.6; 72 -5.1; 79 -5.5; 87 -5.8; 96 -6.1; 106 -6.3; 116 -6.6; 128 -6.9; 141 -7.2; 155 -7.4; 170 -7.6; 187 -7.7; 206 -7.8; 227 -7.8; 249 -7.9; 274 -7.9; 302 -7.8; 332 -7.6; 365 -7.4; 402 -7.3; 442 -7.3; 486 -7.2; 535 -7.0; 588 -6.8; 647 -6.7; 712 -6.5; 783 -5.7; 861 -5.7; 947 -6.0; 1042 -6.5; 1146 -6.8; 1261 -7.1; 1387 -7.6; 1526 -8.1; 1678 -8.3; 1846 -8.1; 2031 -7.9; 2234 -7.7; 2457 -7.6; 2703 -7.5; 2973 -5.8; 3270 -1.1; 3597 -0.5; 3957 -1.1; 4353 -6.8; 4788 -5.1; 5267 -2.3; 5793 -1.1; 6373 -2.5; 7010 -7.3; 7711 -11.6; 8482 -11.3; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.19 | 3.7 dB  |
| Peaking | 51 Hz   | 2.01 | 2.0 dB  |
| Peaking | 3603 Hz | 2.8  | 11.9 dB |
| Peaking | 4844 Hz | 0.64 | -7.3 dB |
| Peaking | 5738 Hz | 3.15 | 11.8 dB |
| Peaking | 245 Hz  | 0.94 | -1.5 dB |
| Peaking | 858 Hz  | 3.49 | 1.5 dB  |
| Peaking | 6641 Hz | 7.4  | 3.3 dB  |
| Peaking | 8123 Hz | 2.59 | -6.2 dB |
| Peaking | 9676 Hz | 1.4  | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GR10/Grado%20GR10.png)