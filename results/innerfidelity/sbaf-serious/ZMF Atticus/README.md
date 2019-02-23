# ZMF Atticus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -4.0; 25 -4.5; 28 -5.0; 31 -5.4; 34 -5.8; 37 -6.1; 41 -6.6; 45 -7.0; 49 -7.5; 54 -7.7; 60 -7.9; 66 -8.5; 72 -9.4; 79 -10.1; 87 -11.0; 96 -11.8; 106 -12.1; 116 -12.5; 128 -12.8; 141 -12.8; 155 -12.3; 170 -12.0; 187 -11.9; 206 -11.1; 227 -10.2; 249 -9.5; 274 -8.9; 302 -8.6; 332 -8.4; 365 -8.4; 402 -8.1; 442 -7.8; 486 -8.0; 535 -7.8; 588 -7.5; 647 -7.4; 712 -7.4; 783 -6.8; 861 -6.6; 947 -6.1; 1042 -5.6; 1146 -5.3; 1261 -5.1; 1387 -4.9; 1526 -2.5; 1678 -3.5; 1846 -5.5; 2031 -5.2; 2234 -6.3; 2457 -6.0; 2703 -5.5; 2973 -4.7; 3270 -4.6; 3597 -2.7; 3957 -0.8; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.2; 8482 -8.3; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ZMF Atticus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ZMF Atticus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.47 | 4.6 dB  |
| Peaking | 133 Hz   | 0.7  | -6.4 dB |
| Peaking | 1564 Hz  | 5.94 | 4.2 dB  |
| Peaking | 5331 Hz  | 1.2  | 7.3 dB  |
| Peaking | 8440 Hz  | 2.42 | -4.7 dB |
| Peaking | 628 Hz   | 1.92 | -0.6 dB |
| Peaking | 1114 Hz  | 2.68 | 1.1 dB  |
| Peaking | 2748 Hz  | 1.2  | -0.8 dB |
| Peaking | 3836 Hz  | 7.08 | 2.1 dB  |
| Peaking | 13874 Hz | 2.68 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ZMF%20Atticus/ZMF%20Atticus.png)