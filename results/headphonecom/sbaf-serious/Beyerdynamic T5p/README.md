# Beyerdynamic T5p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.7; 25 -9.7; 28 -9.6; 31 -9.3; 34 -9.0; 37 -8.7; 41 -8.4; 45 -8.3; 49 -8.0; 54 -7.2; 60 -6.3; 66 -5.3; 72 -4.8; 79 -5.8; 87 -8.4; 96 -10.1; 106 -9.8; 116 -10.4; 128 -10.0; 141 -9.3; 155 -8.4; 170 -8.8; 187 -8.9; 206 -8.2; 227 -7.6; 249 -7.1; 274 -6.8; 302 -6.4; 332 -6.3; 365 -6.3; 402 -6.5; 442 -6.7; 486 -7.0; 535 -7.0; 588 -5.0; 647 -4.1; 712 -5.4; 783 -5.5; 861 -5.2; 947 -5.3; 1042 -6.9; 1146 -9.9; 1261 -8.7; 1387 -9.0; 1526 -9.4; 1678 -9.4; 1846 -9.3; 2031 -11.2; 2234 -11.4; 2457 -8.1; 2703 -5.7; 2973 -5.5; 3270 -6.7; 3597 -6.8; 3957 -6.6; 4353 -5.4; 4788 -3.6; 5267 -0.5; 5793 -2.8; 6373 -5.2; 7010 -3.7; 7711 -5.8; 8482 -6.7; 9330 -6.8; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.44 | -3.9 dB |
| Peaking | 126 Hz  | 1.5  | -4.1 dB |
| Peaking | 1443 Hz | 2.49 | -3.2 dB |
| Peaking | 2129 Hz | 4.98 | -5.4 dB |
| Peaking | 5350 Hz | 5.48 | 6.4 dB  |
| Peaking | 71 Hz   | 6.1  | 2.9 dB  |
| Peaking | 633 Hz  | 6.09 | 3.9 dB  |
| Peaking | 779 Hz  | 1.13 | -2.1 dB |
| Peaking | 861 Hz  | 3.26 | 3.5 dB  |
| Peaking | 8920 Hz | 7.61 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T5p/Beyerdynamic%20T5p.png)