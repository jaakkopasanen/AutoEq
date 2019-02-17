# Nocs NS200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.3; 23 -14.1; 25 -13.9; 28 -13.6; 31 -13.3; 34 -13.1; 37 -12.9; 41 -12.6; 45 -12.3; 49 -12.1; 54 -12.0; 60 -11.8; 66 -11.7; 72 -11.6; 79 -11.6; 87 -11.5; 96 -11.4; 106 -11.3; 116 -11.2; 128 -11.1; 141 -11.1; 155 -11.0; 170 -10.8; 187 -10.6; 206 -10.3; 227 -10.0; 249 -9.6; 274 -9.2; 302 -8.7; 332 -8.2; 365 -7.6; 402 -7.1; 442 -6.6; 486 -6.2; 535 -5.6; 588 -5.1; 647 -4.6; 712 -4.1; 783 -3.9; 861 -4.0; 947 -4.2; 1042 -4.6; 1146 -5.0; 1261 -5.6; 1387 -6.3; 1526 -6.9; 1678 -7.6; 1846 -7.9; 2031 -8.2; 2234 -8.5; 2457 -8.3; 2703 -7.6; 2973 -5.5; 3270 -2.6; 3597 -0.5; 3957 -1.0; 4353 -3.1; 4788 -4.9; 5267 -6.0; 5793 -7.5; 6373 -5.8; 7010 -3.1; 7711 -4.1; 8482 -4.3; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -4.3; 16529 -4.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.14 | -9.3 dB |
| Peaking | 199 Hz  | 0.81 | -4.0 dB |
| Peaking | 2264 Hz | 1.55 | -4.9 dB |
| Peaking | 3657 Hz | 3.38 | 5.8 dB  |
| Peaking | 5727 Hz | 5.77 | -3.5 dB |
| Peaking | 21 Hz   | 1.8  | -0.8 dB |
| Peaking | 380 Hz  | 1.72 | -0.7 dB |
| Peaking | 799 Hz  | 1.72 | 1.5 dB  |
| Peaking | 1529 Hz | 3.59 | -1.0 dB |
| Peaking | 7120 Hz | 9.3  | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS200/Nocs%20NS200.png)