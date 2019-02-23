# Beyerdynamic T70p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.9; 25 -6.1; 28 -6.3; 31 -6.4; 34 -6.5; 37 -6.7; 41 -6.8; 45 -6.8; 49 -6.9; 54 -7.0; 60 -7.2; 66 -7.3; 72 -7.5; 79 -7.5; 87 -7.7; 96 -7.7; 106 -7.7; 116 -7.7; 128 -8.2; 141 -9.0; 155 -9.1; 170 -7.8; 187 -8.3; 206 -8.0; 227 -7.7; 249 -7.2; 274 -7.0; 302 -6.9; 332 -7.0; 365 -7.1; 402 -7.4; 442 -7.6; 486 -7.5; 535 -6.3; 588 -6.3; 647 -6.5; 712 -6.6; 783 -6.6; 861 -6.7; 947 -6.7; 1042 -6.8; 1146 -6.9; 1261 -7.1; 1387 -7.6; 1526 -8.2; 1678 -8.3; 1846 -7.4; 2031 -4.6; 2234 -2.4; 2457 -2.0; 2703 -2.7; 2973 -3.0; 3270 -3.3; 3597 -3.3; 3957 -0.5; 4353 -3.9; 4788 -2.6; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -8.8; 7711 -13.8; 8482 -16.6; 9330 -16.9; 10263 -14.0; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 148 Hz   | 0.76 | -1.9 dB  |
| Peaking | 2475 Hz  | 4.17 | 4.6 dB   |
| Peaking | 3867 Hz  | 3.03 | 4.1 dB   |
| Peaking | 5868 Hz  | 2.81 | 8.9 dB   |
| Peaking | 8687 Hz  | 2.25 | -12.9 dB |
| Peaking | 16 Hz    | 1.29 | 1.2 dB   |
| Peaking | 60 Hz    | 2.13 | -0.2 dB  |
| Peaking | 1599 Hz  | 4.17 | -2.5 dB  |
| Peaking | 10219 Hz | 4.87 | -4.3 dB  |
| Peaking | 11436 Hz | 2.19 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T70p/Beyerdynamic%20T70p.png)