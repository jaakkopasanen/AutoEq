# Shure SE846 Blue Filter Sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.1; 25 -11.2; 28 -11.1; 31 -11.1; 34 -11.1; 37 -11.1; 41 -11.0; 45 -11.0; 49 -11.0; 54 -11.0; 60 -11.0; 66 -11.0; 72 -11.0; 79 -11.1; 87 -11.1; 96 -11.2; 106 -11.1; 116 -10.9; 128 -10.8; 141 -10.7; 155 -10.5; 170 -10.3; 187 -10.0; 206 -9.8; 227 -9.5; 249 -9.3; 274 -9.0; 302 -8.8; 332 -8.6; 365 -8.3; 402 -8.2; 442 -7.9; 486 -7.9; 535 -7.8; 588 -7.3; 647 -7.2; 712 -7.1; 783 -7.0; 861 -7.2; 947 -7.4; 1042 -7.7; 1146 -7.9; 1261 -8.1; 1387 -8.6; 1526 -8.8; 1678 -9.0; 1846 -8.8; 2031 -8.2; 2234 -7.4; 2457 -5.7; 2703 -3.2; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -2.2; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Blue Filter Sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Blue Filter Sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.18 | -4.8 dB |
| Peaking | 1936 Hz | 1.21 | -4.2 dB |
| Peaking | 3245 Hz | 1.6  | 7.6 dB  |
| Peaking | 5713 Hz | 2.9  | 5.5 dB  |
| Peaking | 42 Hz   | 0.38 | -0.8 dB |
| Peaking | 49 Hz   | 0.87 | 1.1 dB  |
| Peaking | 740 Hz  | 3.34 | 0.4 dB  |
| Peaking | 6604 Hz | 7.75 | 2.1 dB  |
| Peaking | 7831 Hz | 2.29 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20Blue%20Filter%20Sample%202/Shure%20SE846%20Blue%20Filter%20Sample%202.png)