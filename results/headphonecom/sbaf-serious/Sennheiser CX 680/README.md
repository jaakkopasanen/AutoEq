# Sennheiser CX 680
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.7; 25 -2.0; 28 -2.5; 31 -2.9; 34 -3.2; 37 -3.5; 41 -3.9; 45 -4.2; 49 -4.6; 54 -5.0; 60 -5.5; 66 -5.9; 72 -6.4; 79 -6.8; 87 -7.2; 96 -7.7; 106 -8.0; 116 -8.4; 128 -8.8; 141 -9.3; 155 -9.5; 170 -10.0; 187 -10.1; 206 -10.2; 227 -10.2; 249 -10.2; 274 -10.0; 302 -9.6; 332 -9.1; 365 -8.5; 402 -8.0; 442 -7.4; 486 -6.8; 535 -6.1; 588 -5.4; 647 -4.5; 712 -3.3; 783 -3.1; 861 -3.1; 947 -3.3; 1042 -3.8; 1146 -4.2; 1261 -4.7; 1387 -5.5; 1526 -6.4; 1678 -7.1; 1846 -7.5; 2031 -7.8; 2234 -8.0; 2457 -7.7; 2703 -6.5; 2973 -4.5; 3270 -2.0; 3597 -0.5; 3957 -1.7; 4353 -5.0; 4788 -8.5; 5267 -9.5; 5793 -4.3; 6373 -0.7; 7010 -3.6; 7711 -5.8; 8482 -6.0; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 680 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.37 | 5.4 dB  |
| Peaking | 210 Hz   | 0.58 | -4.4 dB |
| Peaking | 796 Hz   | 1.77 | 4.2 dB  |
| Peaking | 3608 Hz  | 5.41 | 6.4 dB  |
| Peaking | 21408 Hz | 2.29 | 2.1 dB  |
| Peaking | 1181 Hz  | 2.97 | 1.3 dB  |
| Peaking | 2340 Hz  | 1.42 | -3.9 dB |
| Peaking | 3125 Hz  | 1.44 | 2.8 dB  |
| Peaking | 5115 Hz  | 5.28 | -5.7 dB |
| Peaking | 6330 Hz  | 5.31 | 6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20680/Sennheiser%20CX%20680.png)