# Skullcandy Holua
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.3; 23 -16.3; 25 -16.3; 28 -16.2; 31 -16.1; 34 -16.1; 37 -16.0; 41 -15.9; 45 -15.9; 49 -15.8; 54 -15.8; 60 -15.8; 66 -15.8; 72 -15.7; 79 -15.7; 87 -15.6; 96 -15.4; 106 -15.2; 116 -14.9; 128 -14.7; 141 -14.5; 155 -14.1; 170 -13.8; 187 -13.3; 206 -12.8; 227 -12.3; 249 -11.7; 274 -11.2; 302 -10.5; 332 -9.8; 365 -9.1; 402 -8.5; 442 -8.2; 486 -7.7; 535 -7.1; 588 -6.6; 647 -6.2; 712 -5.8; 783 -5.7; 861 -5.8; 947 -6.2; 1042 -6.7; 1146 -7.0; 1261 -7.5; 1387 -8.5; 1526 -10.2; 1678 -11.8; 1846 -13.0; 2031 -14.3; 2234 -15.8; 2457 -15.1; 2703 -10.1; 2973 -5.7; 3270 -2.1; 3597 -0.5; 3957 -1.3; 4353 -4.2; 4788 -6.9; 5267 -8.1; 5793 -4.7; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Holua GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Holua ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 30 Hz   | 0.24 | -9.6 dB  |
| Peaking | 160 Hz  | 0.81 | -3.9 dB  |
| Peaking | 2289 Hz | 2.09 | -12.7 dB |
| Peaking | 3284 Hz | 1.67 | 6.5 dB   |
| Peaking | 3655 Hz | 4.74 | 3.5 dB   |
| Peaking | 295 Hz  | 2.53 | -0.8 dB  |
| Peaking | 788 Hz  | 1.38 | 1.8 dB   |
| Peaking | 1666 Hz | 5.15 | -1.9 dB  |
| Peaking | 5171 Hz | 5.43 | -3.7 dB  |
| Peaking | 6352 Hz | 5.7  | 5.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Holua/Skullcandy%20Holua.png)