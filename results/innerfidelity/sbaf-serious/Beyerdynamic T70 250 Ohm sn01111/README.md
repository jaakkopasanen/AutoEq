# Beyerdynamic T70 250 Ohm sn01111
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.0; 25 -3.2; 28 -3.5; 31 -3.8; 34 -4.0; 37 -4.2; 41 -4.4; 45 -4.6; 49 -4.8; 54 -5.0; 60 -5.2; 66 -5.5; 72 -5.6; 79 -6.0; 87 -6.1; 96 -6.4; 106 -6.5; 116 -6.9; 128 -7.7; 141 -8.4; 155 -8.6; 170 -7.6; 187 -8.4; 206 -8.2; 227 -7.8; 249 -7.5; 274 -7.5; 302 -7.5; 332 -7.7; 365 -7.9; 402 -8.1; 442 -7.4; 486 -7.3; 535 -7.0; 588 -7.0; 647 -7.2; 712 -7.4; 783 -7.2; 861 -7.4; 947 -7.5; 1042 -7.5; 1146 -7.5; 1261 -7.6; 1387 -7.9; 1526 -8.0; 1678 -7.8; 1846 -6.9; 2031 -5.8; 2234 -4.1; 2457 -3.1; 2703 -3.6; 2973 -3.4; 3270 -3.5; 3597 -3.2; 3957 -0.5; 4353 -2.8; 4788 -2.1; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -7.0; 7711 -12.3; 8482 -15.6; 9330 -15.4; 10263 -12.0; 11289 -6.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm sn01111 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm sn01111 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 1.05 | 3.6 dB   |
| Peaking | 3780 Hz  | 1.67 | 4.6 dB   |
| Peaking | 5401 Hz  | 3.73 | 4.2 dB   |
| Peaking | 6274 Hz  | 4.71 | 5.4 dB   |
| Peaking | 8686 Hz  | 2.54 | -11.2 dB |
| Peaking | 167 Hz   | 1.74 | -1.9 dB  |
| Peaking | 376 Hz   | 2.04 | -1.2 dB  |
| Peaking | 1653 Hz  | 0.9  | -2.1 dB  |
| Peaking | 2377 Hz  | 3.22 | 3.5 dB   |
| Peaking | 11844 Hz | 5.38 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm%20sn01111/Beyerdynamic%20T70%20250%20Ohm%20sn01111.png)