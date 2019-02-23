# Meze 99 Neo with Classic Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.6; 45 -2.3; 49 -2.9; 54 -3.5; 60 -4.0; 66 -4.2; 72 -4.3; 79 -4.6; 87 -5.3; 96 -5.8; 106 -6.0; 116 -6.3; 128 -6.7; 141 -7.0; 155 -7.3; 170 -7.1; 187 -7.3; 206 -7.2; 227 -7.1; 249 -6.4; 274 -5.6; 302 -5.2; 332 -4.4; 365 -3.9; 402 -4.2; 442 -4.8; 486 -6.3; 535 -7.3; 588 -7.8; 647 -8.2; 712 -8.6; 783 -8.4; 861 -8.3; 947 -8.4; 1042 -8.6; 1146 -8.5; 1261 -8.3; 1387 -8.5; 1526 -8.7; 1678 -8.9; 1846 -8.8; 2031 -8.5; 2234 -8.6; 2457 -8.3; 2703 -7.1; 2973 -7.0; 3270 -6.0; 3597 -4.5; 3957 -4.1; 4353 -7.0; 4788 -6.4; 5267 -2.2; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.7; 10263 -7.8; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 99 Neo with Classic Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Neo with Classic Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.5  | 6.3 dB  |
| Peaking | 367 Hz   | 1.75 | 4.9 dB  |
| Peaking | 1100 Hz  | 0.1  | -2.4 dB |
| Peaking | 3654 Hz  | 3.91 | 4.1 dB  |
| Peaking | 6018 Hz  | 2.91 | 7.8 dB  |
| Peaking | 1288 Hz  | 7.52 | 0.4 dB  |
| Peaking | 2721 Hz  | 8.39 | 0.8 dB  |
| Peaking | 4490 Hz  | 9.8  | -1.5 dB |
| Peaking | 9805 Hz  | 3.41 | -1.8 dB |
| Peaking | 11022 Hz | 1.06 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2099%20Neo%20with%20Classic%20Pads/Meze%2099%20Neo%20with%20Classic%20Pads.png)