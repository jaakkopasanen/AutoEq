# Vision Ears VE8 custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.5; 25 -3.9; 28 -4.4; 31 -4.7; 34 -4.9; 37 -5.1; 41 -5.4; 45 -5.6; 49 -5.9; 54 -6.1; 60 -6.4; 66 -6.7; 72 -7.0; 79 -7.3; 87 -7.7; 96 -8.0; 106 -8.3; 116 -8.6; 128 -8.8; 141 -9.0; 155 -9.1; 170 -9.1; 187 -9.1; 206 -9.1; 227 -9.0; 249 -8.7; 274 -8.6; 302 -8.4; 332 -8.1; 365 -7.8; 402 -7.5; 442 -7.2; 486 -6.9; 535 -6.6; 588 -6.2; 647 -5.7; 712 -5.3; 783 -4.8; 861 -4.5; 947 -4.4; 1042 -4.7; 1146 -5.5; 1261 -6.4; 1387 -6.9; 1526 -6.8; 1678 -5.8; 1846 -4.4; 2031 -2.9; 2234 -2.0; 2457 -1.6; 2703 -1.4; 2973 -1.4; 3270 -1.5; 3597 -1.6; 3957 -1.4; 4353 -0.9; 4788 -0.6; 5267 -0.5; 5793 -0.6; 6373 -0.9; 7010 -2.7; 7711 -4.9; 8482 -5.1; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears VE8 custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears VE8 custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.62 | 3.2 dB  |
| Peaking | 195 Hz  | 0.41 | -4.2 dB |
| Peaking | 1510 Hz | 1.63 | -7.4 dB |
| Peaking | 1862 Hz | 0.59 | 6.2 dB  |
| Peaking | 5437 Hz | 2.2  | 3.6 dB  |
| Peaking | 6622 Hz | 6.65 | 2.3 dB  |
| Peaking | 7943 Hz | 2.03 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vision%20Ears%20VE8%20custom/Vision%20Ears%20VE8%20custom.png)