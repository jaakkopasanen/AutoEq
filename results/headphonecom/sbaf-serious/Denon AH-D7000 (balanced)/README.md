# Denon AH-D7000 (balanced)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.9; 28 -3.5; 31 -4.8; 34 -5.7; 37 -6.3; 41 -6.3; 45 -6.6; 49 -7.1; 54 -7.3; 60 -7.0; 66 -7.1; 72 -7.2; 79 -7.2; 87 -7.2; 96 -7.0; 106 -6.8; 116 -6.6; 128 -6.7; 141 -6.7; 155 -6.6; 170 -6.3; 187 -6.3; 206 -6.1; 227 -5.9; 249 -5.6; 274 -5.3; 302 -4.9; 332 -4.5; 365 -4.2; 402 -4.1; 442 -4.5; 486 -5.3; 535 -6.2; 588 -6.9; 647 -7.2; 712 -7.8; 783 -8.4; 861 -7.6; 947 -7.0; 1042 -7.5; 1146 -7.2; 1261 -6.5; 1387 -6.2; 1526 -6.2; 1678 -5.7; 1846 -5.3; 2031 -5.5; 2234 -4.9; 2457 -4.2; 2703 -3.8; 2973 -4.7; 3270 -6.3; 3597 -7.0; 3957 -6.5; 4353 -6.6; 4788 -9.2; 5267 -8.0; 5793 -8.9; 6373 -9.9; 7010 -9.5; 7711 -8.2; 8482 -6.3; 9330 -6.3; 10263 -6.4; 11289 -6.8; 12418 -6.7; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -7.6; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7000 (balanced) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  2.87 | 5.9 dB  |
| Peaking | 385 Hz   |  1.97 | 2.6 dB  |
| Peaking | 758 Hz   |  1.95 | -2.0 dB |
| Peaking | 2562 Hz  |  2.86 | 2.8 dB  |
| Peaking | 6236 Hz  |  2.08 | -3.6 dB |
| Peaking | 27 Hz    |  2.91 | 1.4 dB  |
| Peaking | 62 Hz    |  0.81 | -1.1 dB |
| Peaking | 4784 Hz  | 16.04 | -1.8 dB |
| Peaking | 8626 Hz  |  6.62 | 1.2 dB  |
| Peaking | 18431 Hz |  3.26 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7000%20(balanced)/Denon%20AH-D7000%20(balanced).png)