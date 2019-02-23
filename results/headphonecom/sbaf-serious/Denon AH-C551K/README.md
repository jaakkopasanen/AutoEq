# Denon AH-C551K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.0; 25 -11.1; 28 -11.3; 31 -11.3; 34 -11.4; 37 -11.3; 41 -11.3; 45 -11.4; 49 -11.4; 54 -11.4; 60 -11.6; 66 -11.8; 72 -11.9; 79 -11.9; 87 -11.9; 96 -11.8; 106 -11.6; 116 -11.4; 128 -11.1; 141 -10.8; 155 -10.4; 170 -9.8; 187 -10.2; 206 -10.0; 227 -9.3; 249 -8.5; 274 -7.8; 302 -7.0; 332 -6.2; 365 -5.3; 402 -4.4; 442 -3.7; 486 -2.9; 535 -2.1; 588 -1.4; 647 -0.7; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.9; 1261 -1.4; 1387 -2.2; 1526 -3.8; 1678 -5.2; 1846 -6.2; 2031 -7.1; 2234 -8.1; 2457 -9.6; 2703 -11.5; 2973 -11.4; 3270 -7.4; 3597 -4.3; 3957 -4.4; 4353 -6.7; 4788 -9.1; 5267 -11.7; 5793 -12.6; 6373 -8.7; 7010 -7.2; 7711 -9.4; 8482 -11.6; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C551K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C551K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.47 | -3.2 dB |
| Peaking | 108 Hz  | 0.33 | -5.1 dB |
| Peaking | 759 Hz  | 0.65 | 7.3 dB  |
| Peaking | 2657 Hz | 3.41 | -6.6 dB |
| Peaking | 5622 Hz | 4.25 | -6.9 dB |
| Peaking | 1273 Hz | 3.79 | 1.1 dB  |
| Peaking | 1837 Hz | 3.57 | -1.6 dB |
| Peaking | 3019 Hz | 9.17 | -2.4 dB |
| Peaking | 3731 Hz | 4.63 | 3.7 dB  |
| Peaking | 8446 Hz | 6.6  | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C551K/Denon%20AH-C551K.png)