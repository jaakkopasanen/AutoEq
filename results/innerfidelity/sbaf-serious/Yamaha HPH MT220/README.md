# Yamaha HPH MT220
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.5; 25 -5.0; 28 -5.5; 31 -5.8; 34 -6.0; 37 -6.1; 41 -6.2; 45 -6.2; 49 -6.2; 54 -6.1; 60 -6.1; 66 -6.2; 72 -6.2; 79 -6.1; 87 -6.1; 96 -6.1; 106 -5.7; 116 -5.0; 128 -4.4; 141 -4.6; 155 -5.5; 170 -3.8; 187 -4.4; 206 -4.5; 227 -4.2; 249 -3.6; 274 -3.0; 302 -2.5; 332 -2.7; 365 -2.6; 402 -2.6; 442 -2.9; 486 -3.7; 535 -4.3; 588 -4.7; 647 -5.4; 712 -6.0; 783 -6.2; 861 -6.5; 947 -6.5; 1042 -6.4; 1146 -6.1; 1261 -5.5; 1387 -5.7; 1526 -5.4; 1678 -4.3; 1846 -2.6; 2031 -0.8; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.8; 4353 -3.2; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HPH MT220 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HPH MT220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.83 | 2.6 dB  |
| Peaking | 160 Hz  | 1.16 | 1.5 dB  |
| Peaking | 353 Hz  | 1.46 | 4.0 dB  |
| Peaking | 2764 Hz | 1.26 | 6.5 dB  |
| Peaking | 5594 Hz | 2.61 | 5.4 dB  |
| Peaking | 1120 Hz | 1.37 | -1.0 dB |
| Peaking | 2062 Hz | 5.31 | 2.0 dB  |
| Peaking | 2771 Hz | 4.17 | -1.0 dB |
| Peaking | 3749 Hz | 7.48 | 1.5 dB  |
| Peaking | 8350 Hz | 3.83 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HPH%20MT220/Yamaha%20HPH%20MT220.png)