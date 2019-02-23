# Shure SRH440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -0.8; 72 -0.5; 79 -1.2; 87 -3.1; 96 -4.3; 106 -5.1; 116 -5.3; 128 -5.6; 141 -5.7; 155 -6.0; 170 -5.5; 187 -5.6; 206 -5.5; 227 -5.4; 249 -5.6; 274 -6.1; 302 -6.5; 332 -6.8; 365 -7.7; 402 -7.7; 442 -7.6; 486 -7.5; 535 -7.5; 588 -7.5; 647 -7.5; 712 -7.5; 783 -7.4; 861 -7.5; 947 -7.4; 1042 -6.4; 1146 -7.0; 1261 -7.4; 1387 -8.1; 1526 -9.2; 1678 -9.8; 1846 -9.6; 2031 -8.4; 2234 -7.2; 2457 -5.8; 2703 -5.3; 2973 -4.9; 3270 -5.2; 3597 -5.9; 3957 -5.4; 4353 -6.5; 4788 -5.6; 5267 -1.5; 5793 -4.9; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -8.8; 9330 -13.1; 10263 -13.5; 11289 -7.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.57 | 6.9 dB  |
| Peaking | 2004 Hz | 1.18 | -5.4 dB |
| Peaking | 2573 Hz | 1.64 | 5.0 dB  |
| Peaking | 6318 Hz | 2.41 | 5.0 dB  |
| Peaking | 9723 Hz | 3.63 | -8.8 dB |
| Peaking | 39 Hz   | 3.15 | -1.0 dB |
| Peaking | 74 Hz   | 3.58 | 2.4 dB  |
| Peaking | 107 Hz  | 2.39 | -1.2 dB |
| Peaking | 487 Hz  | 1.48 | -1.2 dB |
| Peaking | 1109 Hz | 5.67 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH440/Shure%20SRH440.png)