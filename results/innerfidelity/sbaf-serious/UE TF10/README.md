# UE TF10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.5; 25 -7.6; 28 -7.7; 31 -7.8; 34 -7.9; 37 -8.0; 41 -8.2; 45 -8.3; 49 -8.4; 54 -8.7; 60 -8.9; 66 -9.3; 72 -9.6; 79 -10.0; 87 -10.3; 96 -10.6; 106 -10.9; 116 -11.0; 128 -11.2; 141 -11.4; 155 -11.5; 170 -11.5; 187 -11.4; 206 -11.3; 227 -11.1; 249 -10.9; 274 -10.6; 302 -10.3; 332 -10.1; 365 -9.9; 402 -9.5; 442 -9.0; 486 -8.8; 535 -8.5; 588 -7.9; 647 -7.7; 712 -7.5; 783 -7.2; 861 -7.3; 947 -7.5; 1042 -7.6; 1146 -7.6; 1261 -7.6; 1387 -7.8; 1526 -7.8; 1678 -7.5; 1846 -6.7; 2031 -5.8; 2234 -5.0; 2457 -3.6; 2703 -1.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`UE TF10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `UE TF10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.25 | -0.8 dB |
| Peaking | 102 Hz  | 0.91 | -1.2 dB |
| Peaking | 210 Hz  | 0.53 | -4.1 dB |
| Peaking | 1604 Hz | 1.56 | -2.7 dB |
| Peaking | 3835 Hz | 0.92 | 7.1 dB  |
| Peaking | 2913 Hz | 4.94 | 1.8 dB  |
| Peaking | 3963 Hz | 1.34 | -1.4 dB |
| Peaking | 5929 Hz | 1.99 | 3.8 dB  |
| Peaking | 7718 Hz | 1.42 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/UE%20TF10/UE%20TF10.png)