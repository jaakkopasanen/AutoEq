# AKG K271 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.6; 87 -1.6; 96 -2.6; 106 -3.4; 116 -4.2; 128 -4.9; 141 -5.8; 155 -6.3; 170 -5.8; 187 -6.3; 206 -6.7; 227 -6.2; 249 -6.4; 274 -6.1; 302 -6.6; 332 -6.9; 365 -7.0; 402 -7.1; 442 -7.5; 486 -7.8; 535 -7.9; 588 -8.3; 647 -9.7; 712 -6.6; 783 -5.3; 861 -5.4; 947 -5.8; 1042 -6.7; 1146 -7.3; 1261 -7.9; 1387 -8.8; 1526 -9.4; 1678 -9.5; 1846 -9.0; 2031 -6.5; 2234 -4.3; 2457 -6.1; 2703 -6.5; 2973 -6.1; 3270 -3.7; 3597 -3.1; 3957 -4.2; 4353 -5.8; 4788 -4.2; 5267 -1.7; 5793 -0.7; 6373 -1.9; 7010 -4.2; 7711 -10.1; 8482 -14.3; 9330 -14.7; 10263 -11.1; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K271 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.56 | 7.0 dB   |
| Peaking | 1572 Hz | 3.27 | -3.5 dB  |
| Peaking | 3487 Hz | 5.4  | 3.3 dB   |
| Peaking | 6058 Hz | 2.31 | 7.5 dB   |
| Peaking | 8813 Hz | 2.85 | -10.8 dB |
| Peaking | 20 Hz   | 2.95 | 1.6 dB   |
| Peaking | 79 Hz   | 4.92 | 1.8 dB   |
| Peaking | 715 Hz  | 1.76 | -5.2 dB  |
| Peaking | 747 Hz  | 7.48 | 4.4 dB   |
| Peaking | 868 Hz  | 2.85 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K271%20MKII/AKG%20K271%20MKII.png)