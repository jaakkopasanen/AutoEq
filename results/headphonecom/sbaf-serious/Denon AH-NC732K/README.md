# Denon AH-NC732K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -1.9; 28 -2.4; 31 -2.8; 34 -3.2; 37 -3.4; 41 -3.3; 45 -3.0; 49 -2.9; 54 -2.6; 60 -2.2; 66 -1.9; 72 -1.8; 79 -2.0; 87 -2.0; 96 -1.9; 106 -1.8; 116 -1.7; 128 -1.6; 141 -1.4; 155 -1.0; 170 -1.3; 187 -1.2; 206 -1.2; 227 -1.2; 249 -1.2; 274 -1.0; 302 -1.0; 332 -1.1; 365 -1.2; 402 -1.3; 442 -1.4; 486 -1.8; 535 -2.2; 588 -2.5; 647 -3.0; 712 -3.0; 783 -3.2; 861 -4.4; 947 -6.0; 1042 -6.9; 1146 -7.4; 1261 -9.1; 1387 -10.5; 1526 -7.4; 1678 -7.1; 1846 -5.3; 2031 -1.4; 2234 -0.6; 2457 -0.6; 2703 -0.6; 2973 -0.6; 3270 -0.6; 3597 -0.6; 3957 -0.6; 4353 -0.6; 4788 -0.6; 5267 -0.6; 5793 -0.6; 6373 -1.5; 7010 -4.1; 7711 -6.3; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-NC732K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-NC732K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.55 | 5.6 dB  |
| Peaking | 89 Hz   | 0.36 | 3.9 dB  |
| Peaking | 393 Hz  | 0.49 | 4.0 dB  |
| Peaking | 1366 Hz | 1.93 | -7.8 dB |
| Peaking | 3114 Hz | 0.62 | 7.1 dB  |
| Peaking | 1801 Hz | 8.53 | -3.7 dB |
| Peaking | 2006 Hz | 1.9  | 3.6 dB  |
| Peaking | 2651 Hz | 0.86 | -2.0 dB |
| Peaking | 6254 Hz | 1.72 | 6.1 dB  |
| Peaking | 7407 Hz | 1.4  | -5.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 3.9 dB  |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 5.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-NC732K/Denon%20AH-NC732K.png)