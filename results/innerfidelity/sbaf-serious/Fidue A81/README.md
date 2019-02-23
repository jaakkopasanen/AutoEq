# Fidue A81
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.1; 28 -4.5; 31 -4.8; 34 -5.0; 37 -5.3; 41 -5.6; 45 -5.8; 49 -6.1; 54 -6.4; 60 -6.7; 66 -7.0; 72 -7.2; 79 -7.6; 87 -7.9; 96 -8.2; 106 -8.3; 116 -8.4; 128 -8.5; 141 -8.5; 155 -8.4; 170 -8.3; 187 -8.0; 206 -7.8; 227 -7.3; 249 -7.0; 274 -6.5; 302 -6.0; 332 -5.4; 365 -4.8; 402 -4.3; 442 -3.6; 486 -3.2; 535 -2.7; 588 -1.9; 647 -1.5; 712 -1.3; 783 -0.8; 861 -0.8; 947 -1.1; 1042 -1.3; 1146 -1.6; 1261 -2.1; 1387 -2.9; 1526 -3.9; 1678 -4.7; 1846 -5.2; 2031 -5.8; 2234 -6.8; 2457 -7.2; 2703 -7.1; 2973 -4.8; 3270 -2.2; 3597 -1.3; 3957 -2.9; 4353 -7.6; 4788 -12.7; 5267 -9.7; 5793 -3.4; 6373 -0.5; 7010 -2.5; 7711 -4.7; 8482 -8.2; 9330 -9.4; 10263 -6.6; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A81 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A81 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 942 Hz  | 1.15 | 5.6 dB   |
| Peaking | 3715 Hz | 2.69 | 10.2 dB  |
| Peaking | 4977 Hz | 1.11 | -26.5 dB |
| Peaking | 6039 Hz | 1.05 | 21.6 dB  |
| Peaking | 8969 Hz | 3.41 | -6.4 dB  |
| Peaking | 17 Hz   | 1.16 | 2.2 dB   |
| Peaking | 92 Hz   | 0.75 | -1.9 dB  |
| Peaking | 172 Hz  | 0.79 | -2.5 dB  |
| Peaking | 527 Hz  | 1.72 | 1.5 dB   |
| Peaking | 2557 Hz | 7.61 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A81/Fidue%20A81.png)