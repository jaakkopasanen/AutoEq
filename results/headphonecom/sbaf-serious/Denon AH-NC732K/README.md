# Denon AH-NC732K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.7; 25 -7.3; 28 -7.8; 31 -8.2; 34 -8.6; 37 -8.8; 41 -8.7; 45 -8.4; 49 -8.2; 54 -7.9; 60 -7.6; 66 -7.3; 72 -7.2; 79 -7.4; 87 -7.4; 96 -7.3; 106 -7.2; 116 -7.1; 128 -6.9; 141 -6.8; 155 -6.4; 170 -6.7; 187 -6.5; 206 -6.6; 227 -6.6; 249 -6.5; 274 -6.3; 302 -6.4; 332 -6.4; 365 -6.5; 402 -6.7; 442 -6.8; 486 -7.2; 535 -7.6; 588 -7.9; 647 -8.3; 712 -8.4; 783 -8.6; 861 -9.8; 947 -11.4; 1042 -12.2; 1146 -12.8; 1261 -14.5; 1387 -15.9; 1526 -12.8; 1678 -12.5; 1846 -10.6; 2031 -6.8; 2234 -3.4; 2457 -3.6; 2703 -2.5; 2973 -1.7; 3270 -2.1; 3597 -2.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.2; 6373 -6.7; 7010 -8.0; 7711 -10.6; 8482 -10.5; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-NC732K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-NC732K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 40 Hz    |  1.55 | -2.3 dB  |
| Peaking | 92 Hz    |  2.46 | -0.6 dB  |
| Peaking | 1382 Hz  |  1.32 | -11.8 dB |
| Peaking | 3850 Hz  |  0.51 | 7.9 dB   |
| Peaking | 7791 Hz  |  2.2  | -8.6 dB  |
| Peaking | 1809 Hz  | 11.15 | -2.4 dB  |
| Peaking | 2228 Hz  |  7.31 | 2.1 dB   |
| Peaking | 3504 Hz  |  9.09 | -2.1 dB  |
| Peaking | 5438 Hz  | 10.17 | 2.2 dB   |
| Peaking | 13483 Hz |  1.65 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-NC732K/Denon%20AH-NC732K.png)