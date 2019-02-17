# ZMF Eikon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -8.7; 25 -8.7; 28 -8.7; 31 -8.8; 34 -8.8; 37 -8.8; 41 -8.7; 45 -8.7; 49 -8.8; 54 -8.6; 60 -8.4; 66 -9.0; 72 -9.8; 79 -10.5; 87 -10.9; 96 -11.4; 106 -11.5; 116 -11.4; 128 -11.4; 141 -11.3; 155 -10.5; 170 -10.3; 187 -10.2; 206 -9.8; 227 -9.4; 249 -9.2; 274 -9.0; 302 -9.1; 332 -8.9; 365 -8.6; 402 -8.0; 442 -7.4; 486 -7.3; 535 -6.8; 588 -5.9; 647 -5.7; 712 -5.5; 783 -5.5; 861 -5.8; 947 -5.5; 1042 -4.9; 1146 -4.8; 1261 -4.9; 1387 -4.8; 1526 -0.5; 1678 -1.2; 1846 -3.8; 2031 -5.0; 2234 -4.6; 2457 -3.8; 2703 -4.5; 2973 -4.5; 3270 -4.1; 3597 -3.8; 3957 -6.2; 4353 -6.1; 4788 -5.1; 5267 -4.9; 5793 -8.6; 6373 -0.6; 7010 -2.6; 7711 -4.9; 8482 -5.2; 9330 -7.0; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ZMF Eikon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ZMF Eikon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.22 | -2.7 dB |
| Peaking | 129 Hz  | 0.44 | -6.0 dB |
| Peaking | 1603 Hz | 6.15 | 5.9 dB  |
| Peaking | 5903 Hz | 8.44 | -5.6 dB |
| Peaking | 6487 Hz | 6.9  | 6.6 dB  |
| Peaking | 360 Hz  | 3.86 | -0.9 dB |
| Peaking | 663 Hz  | 3.68 | 0.7 dB  |
| Peaking | 3751 Hz | 2.16 | 2.5 dB  |
| Peaking | 4079 Hz | 4.77 | -3.6 dB |
| Peaking | 9145 Hz | 8.35 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ZMF%20Eikon/ZMF%20Eikon.png)