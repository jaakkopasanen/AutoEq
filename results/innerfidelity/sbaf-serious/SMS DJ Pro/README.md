# SMS DJ Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.5; 25 -11.7; 28 -11.8; 31 -11.8; 34 -11.7; 37 -11.6; 41 -11.4; 45 -11.1; 49 -10.8; 54 -10.4; 60 -9.9; 66 -9.2; 72 -8.9; 79 -9.1; 87 -10.5; 96 -12.3; 106 -12.0; 116 -10.6; 128 -9.5; 141 -9.1; 155 -8.0; 170 -7.8; 187 -8.1; 206 -8.3; 227 -8.3; 249 -8.7; 274 -9.0; 302 -9.2; 332 -9.3; 365 -10.6; 402 -11.4; 442 -10.6; 486 -10.5; 535 -9.9; 588 -9.1; 647 -8.5; 712 -7.5; 783 -6.5; 861 -7.4; 947 -7.0; 1042 -6.9; 1146 -6.6; 1261 -6.7; 1387 -7.2; 1526 -7.9; 1678 -8.2; 1846 -7.8; 2031 -6.6; 2234 -5.6; 2457 -4.4; 2703 -3.3; 2973 -2.4; 3270 -2.4; 3597 -2.6; 3957 -3.8; 4353 -3.3; 4788 -5.0; 5267 -2.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SMS DJ Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS DJ Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.64 | -5.5 dB |
| Peaking | 103 Hz  | 2.88 | -4.7 dB |
| Peaking | 417 Hz  | 1.21 | -4.4 dB |
| Peaking | 3225 Hz | 2.51 | 4.5 dB  |
| Peaking | 5970 Hz | 3.78 | 6.3 dB  |
| Peaking | 47 Hz   | 3.47 | -0.4 dB |
| Peaking | 1448 Hz | 0.89 | 0.9 dB  |
| Peaking | 1680 Hz | 2.35 | -2.8 dB |
| Peaking | 2540 Hz | 5.2  | 0.9 dB  |
| Peaking | 8182 Hz | 4.72 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -4.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SMS%20DJ%20Pro/SMS%20DJ%20Pro.png)