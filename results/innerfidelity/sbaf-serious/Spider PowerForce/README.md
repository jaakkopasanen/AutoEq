# Spider PowerForce
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.4; 25 -8.1; 28 -8.9; 31 -9.7; 34 -10.3; 37 -10.8; 41 -11.5; 45 -12.0; 49 -12.4; 54 -12.9; 60 -13.3; 66 -13.6; 72 -13.8; 79 -14.1; 87 -14.2; 96 -14.4; 106 -14.3; 116 -14.3; 128 -14.4; 141 -14.4; 155 -14.2; 170 -13.4; 187 -12.9; 206 -11.8; 227 -10.8; 249 -8.5; 274 -7.2; 302 -7.7; 332 -8.1; 365 -8.2; 402 -8.4; 442 -8.6; 486 -8.5; 535 -8.2; 588 -7.5; 647 -6.9; 712 -5.5; 783 -5.6; 861 -5.6; 947 -5.5; 1042 -5.3; 1146 -5.1; 1261 -5.1; 1387 -5.5; 1526 -5.7; 1678 -6.2; 1846 -6.3; 2031 -6.4; 2234 -6.5; 2457 -6.0; 2703 -5.4; 2973 -4.4; 3270 -3.6; 3597 -1.4; 3957 -0.5; 4353 -0.5; 4788 -6.8; 5267 -3.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spider PowerForce GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider PowerForce ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 71 Hz    | 0.67 | -6.9 dB |
| Peaking | 153 Hz   | 1.48 | -5.0 dB |
| Peaking | 468 Hz   | 4.66 | -1.7 dB |
| Peaking | 3881 Hz  | 3.21 | 6.3 dB  |
| Peaking | 6088 Hz  | 4.82 | 6.1 dB  |
| Peaking | 268 Hz   | 1.62 | -1.9 dB |
| Peaking | 274 Hz   | 4.09 | 3.6 dB  |
| Peaking | 1086 Hz  | 1.28 | 1.5 dB  |
| Peaking | 2066 Hz  | 2.96 | -0.7 dB |
| Peaking | 22050 Hz | 1.77 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -7.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Spider%20PowerForce/Spider%20PowerForce.png)