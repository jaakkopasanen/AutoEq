# ZMF Eikon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.5; 25 -8.6; 28 -8.6; 31 -8.6; 34 -8.6; 37 -8.6; 41 -8.5; 45 -8.5; 49 -8.7; 54 -8.5; 60 -8.3; 66 -8.8; 72 -9.7; 79 -10.3; 87 -10.8; 96 -11.2; 106 -11.3; 116 -11.3; 128 -11.3; 141 -11.1; 155 -10.3; 170 -10.2; 187 -10.0; 206 -9.6; 227 -9.2; 249 -9.1; 274 -8.9; 302 -8.9; 332 -8.8; 365 -8.4; 402 -7.9; 442 -7.2; 486 -7.1; 535 -6.6; 588 -5.7; 647 -5.5; 712 -5.4; 783 -5.4; 861 -5.6; 947 -5.3; 1042 -4.8; 1146 -4.7; 1261 -4.8; 1387 -4.7; 1526 -0.5; 1678 -1.1; 1846 -3.6; 2031 -4.9; 2234 -4.5; 2457 -3.6; 2703 -4.3; 2973 -4.3; 3270 -4.0; 3597 -3.7; 3957 -6.1; 4353 -5.9; 4788 -4.9; 5267 -4.7; 5793 -8.5; 6373 -1.3; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.9; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ZMF Eikon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ZMF Eikon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.42 | -2.0 dB |
| Peaking | 129 Hz   | 0.48 | -5.0 dB |
| Peaking | 1604 Hz  | 7.09 | 4.9 dB  |
| Peaking | 2115 Hz  | 0.37 | 1.6 dB  |
| Peaking | 22050 Hz | 2.21 | 0.5 dB  |
| Peaking | 356 Hz   | 4.44 | -0.8 dB |
| Peaking | 640 Hz   | 4.53 | 0.7 dB  |
| Peaking | 5908 Hz  | 9.6  | -5.4 dB |
| Peaking | 6501 Hz  | 6.26 | 5.7 dB  |
| Peaking | 8847 Hz  | 2.39 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ZMF%20Eikon/ZMF%20Eikon.png)