# Oppo PM1 2014 Alt Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.5; 25 -4.7; 28 -4.9; 31 -5.0; 34 -5.2; 37 -5.2; 41 -5.3; 45 -5.3; 49 -5.3; 54 -5.2; 60 -4.8; 66 -5.2; 72 -6.3; 79 -6.8; 87 -7.2; 96 -7.8; 106 -8.0; 116 -8.3; 128 -8.6; 141 -8.9; 155 -9.0; 170 -9.0; 187 -9.2; 206 -9.2; 227 -9.0; 249 -9.4; 274 -9.8; 302 -10.0; 332 -10.0; 365 -8.5; 402 -7.0; 442 -7.5; 486 -8.1; 535 -8.4; 588 -8.2; 647 -8.6; 712 -9.1; 783 -9.2; 861 -9.4; 947 -7.6; 1042 -7.0; 1146 -7.3; 1261 -7.3; 1387 -7.8; 1526 -8.1; 1678 -8.1; 1846 -7.5; 2031 -6.9; 2234 -6.4; 2457 -5.5; 2703 -4.6; 2973 -3.5; 3270 -3.1; 3597 -3.2; 3957 -2.3; 4353 -2.1; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.7; 9330 -8.9; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 2014 Alt Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 2014 Alt Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.15 | 2.7 dB  |
| Peaking | 150 Hz  | 0.66 | -5.0 dB |
| Peaking | 299 Hz  | 2.9  | -2.9 dB |
| Peaking | 755 Hz  | 0.82 | -3.1 dB |
| Peaking | 4945 Hz | 1.52 | 6.3 dB  |
| Peaking | 1075 Hz | 3.62 | 2.0 dB  |
| Peaking | 3026 Hz | 1.56 | 4.5 dB  |
| Peaking | 3097 Hz | 0.54 | -3.1 dB |
| Peaking | 6206 Hz | 4.1  | 3.4 dB  |
| Peaking | 8989 Hz | 4.59 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1%202014%20Alt%20Pads/Oppo%20PM1%202014%20Alt%20Pads.png)