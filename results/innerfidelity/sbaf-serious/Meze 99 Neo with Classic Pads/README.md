# Meze 99 Neo with Classic Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.9; 54 -1.6; 60 -2.1; 66 -2.3; 72 -2.3; 79 -2.7; 87 -3.3; 96 -3.8; 106 -4.1; 116 -4.3; 128 -4.7; 141 -5.1; 155 -5.4; 170 -5.1; 187 -5.3; 206 -5.3; 227 -5.2; 249 -4.4; 274 -3.7; 302 -3.2; 332 -2.5; 365 -2.0; 402 -2.2; 442 -2.9; 486 -4.3; 535 -5.3; 588 -5.9; 647 -6.3; 712 -6.7; 783 -6.4; 861 -6.3; 947 -6.4; 1042 -6.7; 1146 -6.6; 1261 -6.3; 1387 -6.5; 1526 -6.7; 1678 -6.9; 1846 -6.9; 2031 -6.5; 2234 -6.7; 2457 -6.4; 2703 -5.2; 2973 -5.0; 3270 -4.1; 3597 -2.5; 3957 -2.2; 4353 -5.0; 4788 -4.5; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 99 Neo with Classic Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Neo with Classic Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.43 | 6.3 dB  |
| Peaking | 366 Hz  | 2.12 | 4.6 dB  |
| Peaking | 3668 Hz | 4.7  | 4.0 dB  |
| Peaking | 5936 Hz | 2.68 | 7.0 dB  |
| Peaking | 7867 Hz | 1.89 | -1.4 dB |
| Peaking | 450 Hz  | 6.8  | 0.8 dB  |
| Peaking | 675 Hz  | 1.91 | -0.6 dB |
| Peaking | 1700 Hz | 4.68 | -0.5 dB |
| Peaking | 2529 Hz | 2.19 | -1.1 dB |
| Peaking | 2740 Hz | 3.84 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2099%20Neo%20with%20Classic%20Pads/Meze%2099%20Neo%20with%20Classic%20Pads.png)