# Nocs NS800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.5; 25 -7.5; 28 -7.5; 31 -7.5; 34 -7.6; 37 -7.7; 41 -7.8; 45 -7.9; 49 -8.0; 54 -8.3; 60 -8.5; 66 -8.7; 72 -8.9; 79 -9.2; 87 -9.4; 96 -9.6; 106 -9.9; 116 -9.9; 128 -10.2; 141 -10.2; 155 -10.5; 170 -10.4; 187 -10.5; 206 -10.4; 227 -10.3; 249 -10.2; 274 -10.0; 302 -9.8; 332 -9.5; 365 -9.1; 402 -8.9; 442 -8.6; 486 -8.4; 535 -8.0; 588 -7.7; 647 -7.3; 712 -6.9; 783 -6.7; 861 -6.9; 947 -7.0; 1042 -7.3; 1146 -7.6; 1261 -7.9; 1387 -8.3; 1526 -8.7; 1678 -8.8; 1846 -8.7; 2031 -8.4; 2234 -8.2; 2457 -8.0; 2703 -8.2; 2973 -7.7; 3270 -4.5; 3597 -0.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.47 | -2.5 dB |
| Peaking | 246 Hz  | 0.76 | -2.4 dB |
| Peaking | 1828 Hz | 1.49 | -3.2 dB |
| Peaking | 2849 Hz | 4.06 | -4.0 dB |
| Peaking | 4419 Hz | 1.22 | 7.5 dB  |
| Peaking | 21 Hz   | 1.45 | -0.6 dB |
| Peaking | 3640 Hz | 7.59 | 2.1 dB  |
| Peaking | 4396 Hz | 2.08 | -1.1 dB |
| Peaking | 6308 Hz | 2.84 | 4.6 dB  |
| Peaking | 7426 Hz | 1.65 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS800/Nocs%20NS800.png)