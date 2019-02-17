# Denon AH-C751K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.4; 25 -9.5; 28 -9.7; 31 -9.8; 34 -9.7; 37 -9.7; 41 -9.6; 45 -9.7; 49 -10.0; 54 -10.1; 60 -10.1; 66 -10.0; 72 -10.0; 79 -9.9; 87 -9.9; 96 -9.8; 106 -9.5; 116 -9.1; 128 -8.7; 141 -8.1; 155 -9.1; 170 -9.1; 187 -8.5; 206 -7.9; 227 -7.3; 249 -6.6; 274 -6.1; 302 -5.3; 332 -4.6; 365 -3.9; 402 -3.3; 442 -2.8; 486 -2.3; 535 -1.8; 588 -1.3; 647 -0.9; 712 -0.7; 783 -0.5; 861 -0.6; 947 -1.0; 1042 -1.4; 1146 -1.9; 1261 -2.6; 1387 -3.6; 1526 -4.8; 1678 -5.6; 1846 -6.6; 2031 -7.6; 2234 -8.2; 2457 -9.1; 2703 -10.4; 2973 -10.5; 3270 -7.7; 3597 -5.0; 3957 -5.1; 4353 -7.3; 4788 -9.3; 5267 -11.3; 5793 -12.6; 6373 -9.9; 7010 -8.6; 7711 -10.6; 8482 -12.3; 9330 -8.1; 10263 -1.4; 11289 -1.2; 12418 -1.2; 13660 -1.2; 15026 -4.0; 16529 -1.5; 18182 -1.2; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C751K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C751K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.3  | -9.1 dB  |
| Peaking | 188 Hz   | 1.14 | -3.7 dB  |
| Peaking | 2493 Hz  | 1.69 | -7.6 dB  |
| Peaking | 6496 Hz  | 1.13 | -10.0 dB |
| Peaking | 20961 Hz | 2.37 | -8.1 dB  |
| Peaking | 3870 Hz  | 4.43 | 4.0 dB   |
| Peaking | 6015 Hz  | 1.03 | -3.5 dB  |
| Peaking | 6841 Hz  | 3.78 | 6.6 dB   |
| Peaking | 8762 Hz  | 3.42 | -7.2 dB  |
| Peaking | 10299 Hz | 2.13 | 6.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | -5.1 dB |
| Peaking | 8000 Hz  | 1.41 | -8.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C751K/Denon%20AH-C751K.png)