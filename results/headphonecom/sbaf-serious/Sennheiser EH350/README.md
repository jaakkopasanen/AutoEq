# Sennheiser EH350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.9; 79 -1.7; 87 -2.7; 96 -3.7; 106 -4.6; 116 -5.0; 128 -5.6; 141 -5.1; 155 -5.2; 170 -5.6; 187 -5.9; 206 -6.0; 227 -6.1; 249 -6.3; 274 -6.5; 302 -6.6; 332 -6.7; 365 -6.9; 402 -6.9; 442 -7.2; 486 -7.1; 535 -6.7; 588 -6.8; 647 -6.4; 712 -6.7; 783 -7.5; 861 -7.6; 947 -7.7; 1042 -7.5; 1146 -7.4; 1261 -8.2; 1387 -8.7; 1526 -9.2; 1678 -9.2; 1846 -7.7; 2031 -7.1; 2234 -6.5; 2457 -6.2; 2703 -6.4; 2973 -6.4; 3270 -6.8; 3597 -5.0; 3957 -0.6; 4353 -7.0; 4788 -8.5; 5267 -5.7; 5793 -3.7; 6373 -1.9; 7010 -7.1; 7711 -10.6; 8482 -9.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.0; 13660 -15.5; 15026 -15.8; 16529 -13.2; 18182 -12.1; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser EH350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 38 Hz    |  0.53 | 6.8 dB  |
| Peaking | 4486 Hz  |  0.62 | 7.0 dB  |
| Peaking | 10842 Hz |  0.09 | -5.6 dB |
| Peaking | 11680 Hz |  2.07 | 7.9 dB  |
| Peaking | 13925 Hz |  1.56 | -7.7 dB |
| Peaking | 1588 Hz  |  5.51 | -1.8 dB |
| Peaking | 4622 Hz  | 10.32 | -7.7 dB |
| Peaking | 5457 Hz  |  0.68 | 1.5 dB  |
| Peaking | 6303 Hz  |  8.16 | 4.4 dB  |
| Peaking | 7707 Hz  |  4.91 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 5.2 dB   |
| Peaking | 125 Hz   | 1.41 | 0.3 dB   |
| Peaking | 250 Hz   | 1.41 | -0.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -10.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH350/Sennheiser%20EH350.png)