# I-Mego Throne
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.5; 25 -12.6; 28 -12.7; 31 -12.7; 34 -12.7; 37 -12.8; 41 -12.8; 45 -13.0; 49 -13.1; 54 -13.3; 60 -13.5; 66 -13.6; 72 -13.8; 79 -14.0; 87 -14.2; 96 -14.4; 106 -14.4; 116 -14.4; 128 -14.6; 141 -14.9; 155 -14.8; 170 -14.3; 187 -14.0; 206 -13.4; 227 -12.6; 249 -11.9; 274 -11.0; 302 -10.2; 332 -9.8; 365 -10.6; 402 -10.8; 442 -11.5; 486 -12.4; 535 -12.6; 588 -12.3; 647 -12.0; 712 -11.5; 783 -10.6; 861 -10.0; 947 -9.3; 1042 -8.8; 1146 -8.4; 1261 -7.7; 1387 -7.2; 1526 -6.8; 1678 -6.1; 1846 -5.0; 2031 -3.3; 2234 -2.6; 2457 -1.7; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -1.5; 4788 -1.4; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`I-Mego Throne GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `I-Mego Throne ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.28 | -6.3 dB |
| Peaking | 152 Hz  | 0.95 | -4.8 dB |
| Peaking | 628 Hz  | 0.96 | -5.3 dB |
| Peaking | 3158 Hz | 1.14 | 6.6 dB  |
| Peaking | 5812 Hz | 3.35 | 4.7 dB  |
| Peaking | 327 Hz  | 6.54 | 1.0 dB  |
| Peaking | 499 Hz  | 5.59 | -0.9 dB |
| Peaking | 1456 Hz | 2.55 | -0.9 dB |
| Peaking | 2189 Hz | 0.3  | 0.3 dB  |
| Peaking | 8424 Hz | 2.86 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -4.6 dB |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/I-Mego%20Throne/I-Mego%20Throne.png)