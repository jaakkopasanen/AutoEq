# Sennheiser CX 680
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.0; 25 -2.4; 28 -2.8; 31 -3.2; 34 -3.6; 37 -3.9; 41 -4.2; 45 -4.6; 49 -4.9; 54 -5.3; 60 -5.8; 66 -6.2; 72 -6.7; 79 -7.1; 87 -7.6; 96 -8.0; 106 -8.3; 116 -8.8; 128 -9.1; 141 -9.6; 155 -9.9; 170 -10.3; 187 -10.4; 206 -10.5; 227 -10.5; 249 -10.5; 274 -10.3; 302 -10.0; 332 -9.5; 365 -8.9; 402 -8.3; 442 -7.7; 486 -7.1; 535 -6.4; 588 -5.8; 647 -4.9; 712 -3.6; 783 -3.4; 861 -3.4; 947 -3.7; 1042 -4.1; 1146 -4.5; 1261 -5.1; 1387 -5.8; 1526 -6.7; 1678 -7.4; 1846 -7.8; 2031 -8.2; 2234 -8.3; 2457 -8.0; 2703 -6.9; 2973 -4.8; 3270 -2.3; 3597 -0.8; 3957 -2.0; 4353 -5.3; 4788 -8.8; 5267 -9.8; 5793 -4.6; 6373 -0.5; 7010 -1.3; 7711 -3.6; 8482 -3.8; 9330 -4.9; 10263 -4.5; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 680 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 198 Hz  | 0.61 | -7.1 dB |
| Peaking | 2205 Hz | 1.77 | -5.1 dB |
| Peaking | 3647 Hz | 3.18 | 5.4 dB  |
| Peaking | 5085 Hz | 3.45 | -7.7 dB |
| Peaking | 6460 Hz | 4.75 | 5.9 dB  |
| Peaking | 21 Hz   | 1.77 | 2.5 dB  |
| Peaking | 419 Hz  | 1.59 | -1.1 dB |
| Peaking | 801 Hz  | 1.87 | 2.2 dB  |
| Peaking | 1565 Hz | 4.44 | -1.2 dB |
| Peaking | 9696 Hz | 9.07 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20680/Sennheiser%20CX%20680.png)