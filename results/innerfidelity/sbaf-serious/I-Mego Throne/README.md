# I-Mego Throne
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.9; 25 -10.0; 28 -10.1; 31 -10.1; 34 -10.1; 37 -10.1; 41 -10.2; 45 -10.4; 49 -10.5; 54 -10.7; 60 -10.9; 66 -11.0; 72 -11.2; 79 -11.3; 87 -11.6; 96 -11.8; 106 -11.7; 116 -11.8; 128 -12.0; 141 -12.3; 155 -12.1; 170 -11.6; 187 -11.3; 206 -10.8; 227 -10.0; 249 -9.3; 274 -8.4; 302 -7.6; 332 -7.2; 365 -8.0; 402 -8.2; 442 -8.9; 486 -9.8; 535 -10.0; 588 -9.7; 647 -9.4; 712 -8.9; 783 -8.0; 861 -7.4; 947 -6.7; 1042 -6.2; 1146 -5.8; 1261 -5.0; 1387 -4.6; 1526 -4.2; 1678 -3.5; 1846 -2.4; 2031 -0.8; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`I-Mego Throne GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `I-Mego Throne ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.39 | -3.3 dB |
| Peaking | 98 Hz   | 0.97 | -3.0 dB |
| Peaking | 168 Hz  | 1.58 | -3.5 dB |
| Peaking | 603 Hz  | 1.47 | -3.7 dB |
| Peaking | 3296 Hz | 0.65 | 6.9 dB  |
| Peaking | 327 Hz  | 6.27 | 1.1 dB  |
| Peaking | 2175 Hz | 2.93 | 2.3 dB  |
| Peaking | 2608 Hz | 0.82 | -1.3 dB |
| Peaking | 6119 Hz | 1.98 | 5.6 dB  |
| Peaking | 7605 Hz | 1.44 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/I-Mego%20Throne/I-Mego%20Throne.png)