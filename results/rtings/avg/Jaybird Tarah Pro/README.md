# Jaybird Tarah Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.6; 25 -6.6; 28 -6.6; 31 -6.6; 34 -6.7; 37 -6.7; 41 -6.7; 45 -6.7; 49 -6.8; 54 -6.8; 60 -6.9; 66 -7.1; 72 -7.2; 79 -7.3; 87 -7.4; 96 -7.6; 106 -7.6; 116 -7.6; 128 -7.7; 141 -7.8; 155 -7.8; 170 -7.8; 187 -7.7; 206 -7.4; 227 -7.0; 249 -6.6; 274 -6.1; 302 -5.6; 332 -5.1; 365 -4.5; 402 -4.0; 442 -3.4; 486 -2.8; 535 -2.3; 588 -1.9; 647 -1.4; 712 -0.9; 783 -0.5; 861 -0.5; 947 -1.2; 1042 -2.3; 1146 -3.3; 1261 -3.8; 1387 -4.3; 1526 -4.6; 1678 -4.9; 1846 -5.4; 2031 -6.1; 2234 -6.7; 2457 -6.9; 2703 -6.6; 2973 -5.2; 3270 -3.4; 3597 -2.1; 3957 -1.5; 4353 -1.4; 4788 -1.8; 5267 -2.2; 5793 -3.6; 6373 -8.1; 7010 -11.0; 7711 -6.3; 8482 -4.5; 9330 -4.5; 10263 -5.5; 11289 -9.3; 12418 -6.7; 13660 -4.5; 15026 -5.9; 16529 -6.6; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Tarah Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Tarah Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 104 Hz   | 0.32 | -3.3 dB |
| Peaking | 703 Hz   | 1.4  | 4.7 dB  |
| Peaking | 4572 Hz  | 2.73 | 3.8 dB  |
| Peaking | 6852 Hz  | 6.38 | -7.9 dB |
| Peaking | 11496 Hz | 5.17 | -5.3 dB |
| Peaking | 20 Hz    | 2.21 | -1.1 dB |
| Peaking | 923 Hz   | 5.44 | 1.3 dB  |
| Peaking | 2502 Hz  | 1.79 | -3.3 dB |
| Peaking | 3527 Hz  | 3.06 | 2.4 dB  |
| Peaking | 15905 Hz | 4.21 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Tarah%20Pro/Jaybird%20Tarah%20Pro.png)