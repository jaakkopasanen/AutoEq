# Westone ADV Alpha
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.2; 25 -12.3; 28 -12.3; 31 -12.4; 34 -12.4; 37 -12.5; 41 -12.5; 45 -12.6; 49 -12.7; 54 -12.9; 60 -13.0; 66 -13.2; 72 -13.4; 79 -13.7; 87 -13.9; 96 -14.1; 106 -14.2; 116 -14.1; 128 -14.2; 141 -14.1; 155 -14.0; 170 -13.8; 187 -13.5; 206 -13.2; 227 -12.7; 249 -12.3; 274 -11.7; 302 -11.1; 332 -10.6; 365 -9.9; 402 -9.3; 442 -8.5; 486 -8.0; 535 -7.4; 588 -6.5; 647 -6.0; 712 -5.6; 783 -5.0; 861 -4.8; 947 -4.8; 1042 -5.0; 1146 -5.0; 1261 -5.0; 1387 -5.4; 1526 -5.5; 1678 -4.8; 1846 -4.2; 2031 -3.5; 2234 -2.7; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -6.5; 4788 -8.9; 5267 -5.6; 5793 -1.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone ADV Alpha GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone ADV Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.29 | -5.6 dB |
| Peaking | 131 Hz  | 0.85 | -4.9 dB |
| Peaking | 257 Hz  | 1.49 | -3.1 dB |
| Peaking | 2843 Hz | 1.53 | 6.5 dB  |
| Peaking | 6255 Hz | 6.79 | 5.7 dB  |
| Peaking | 402 Hz  | 2.78 | -0.9 dB |
| Peaking | 841 Hz  | 1.65 | 1.9 dB  |
| Peaking | 3840 Hz | 4.62 | 4.9 dB  |
| Peaking | 4734 Hz | 2.54 | -6.3 dB |
| Peaking | 5612 Hz | 4.24 | 4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20ADV%20Alpha/Westone%20ADV%20Alpha.png)