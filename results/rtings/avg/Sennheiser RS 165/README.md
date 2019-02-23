# Sennheiser RS 165
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.3; 25 -10.2; 28 -10.2; 31 -10.0; 34 -9.7; 37 -9.4; 41 -8.9; 45 -8.5; 49 -8.0; 54 -7.6; 60 -7.5; 66 -7.9; 72 -8.3; 79 -8.8; 87 -9.6; 96 -10.4; 106 -11.1; 116 -11.5; 128 -11.6; 141 -11.5; 155 -11.1; 170 -10.6; 187 -9.8; 206 -8.7; 227 -7.5; 249 -6.4; 274 -6.4; 302 -6.7; 332 -6.3; 365 -5.4; 402 -4.2; 442 -3.7; 486 -4.1; 535 -4.7; 588 -5.3; 647 -5.7; 712 -5.5; 783 -6.4; 861 -7.2; 947 -8.1; 1042 -8.4; 1146 -8.1; 1261 -8.4; 1387 -8.3; 1526 -7.8; 1678 -6.8; 1846 -6.7; 2031 -6.4; 2234 -5.8; 2457 -5.3; 2703 -5.1; 2973 -4.4; 3270 -3.3; 3597 -2.1; 3957 -1.5; 4353 -0.5; 4788 -1.6; 5267 -6.3; 5793 -6.2; 6373 -8.2; 7010 -7.1; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -6.5; 11289 -6.8; 12418 -7.1; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 165 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 165 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.18 | -3.9 dB |
| Peaking | 130 Hz  | 1.2  | -5.4 dB |
| Peaking | 460 Hz  | 1.48 | 3.1 dB  |
| Peaking | 1159 Hz | 1.79 | -2.4 dB |
| Peaking | 4027 Hz | 2.63 | 6.2 dB  |
| Peaking | 249 Hz  | 1.94 | -1.5 dB |
| Peaking | 250 Hz  | 3.97 | 2.5 dB  |
| Peaking | 3095 Hz | 1.77 | 1.6 dB  |
| Peaking | 4628 Hz | 7.32 | 4.9 dB  |
| Peaking | 4834 Hz | 1.37 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20165/Sennheiser%20RS%20165.png)