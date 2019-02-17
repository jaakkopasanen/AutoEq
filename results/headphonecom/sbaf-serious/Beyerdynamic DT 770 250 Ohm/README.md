# Beyerdynamic DT 770 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.3; 25 -8.6; 28 -8.9; 31 -9.1; 34 -9.2; 37 -9.2; 41 -8.7; 45 -7.7; 49 -7.3; 54 -7.2; 60 -3.5; 66 -2.8; 72 -6.9; 79 -9.3; 87 -10.4; 96 -10.9; 106 -11.2; 116 -11.1; 128 -10.6; 141 -9.4; 155 -7.8; 170 -7.6; 187 -6.5; 206 -5.7; 227 -5.7; 249 -6.0; 274 -6.5; 302 -6.6; 332 -6.7; 365 -6.9; 402 -7.0; 442 -7.1; 486 -7.1; 535 -7.3; 588 -7.3; 647 -7.4; 712 -7.4; 783 -7.4; 861 -7.1; 947 -6.4; 1042 -6.4; 1146 -6.2; 1261 -6.1; 1387 -5.9; 1526 -6.3; 1678 -7.0; 1846 -7.3; 2031 -7.2; 2234 -6.6; 2457 -5.4; 2703 -4.5; 2973 -3.7; 3270 -3.0; 3597 -0.5; 3957 -0.6; 4353 -5.7; 4788 -9.4; 5267 -8.1; 5793 -9.4; 6373 -12.8; 7010 -10.5; 7711 -10.9; 8482 -13.4; 9330 -14.3; 10263 -11.5; 11289 -9.8; 12418 -11.4; 13660 -9.9; 15026 -6.5; 16529 -7.8; 18182 -14.7; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 31 Hz    |  1.24 | -2.8 dB  |
| Peaking | 63 Hz    |  6.11 | 6.5 dB   |
| Peaking | 103 Hz   |  1.83 | -5.2 dB  |
| Peaking | 3638 Hz  |  2.17 | 9.8 dB   |
| Peaking | 8432 Hz  |  0.37 | -6.0 dB  |
| Peaking | 216 Hz   |  4.58 | 1.6 dB   |
| Peaking | 2627 Hz  |  7.16 | 1.2 dB   |
| Peaking | 7385 Hz  | 11.35 | 2.0 dB   |
| Peaking | 15676 Hz |  1.1  | 10.9 dB  |
| Peaking | 19052 Hz |  0.39 | -11.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20770%20250%20Ohm/Beyerdynamic%20DT%20770%20250%20Ohm.png)