# Spider realvoice
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.2; 25 -11.1; 28 -11.0; 31 -10.9; 34 -10.9; 37 -10.8; 41 -10.7; 45 -10.6; 49 -10.5; 54 -10.5; 60 -10.4; 66 -10.3; 72 -10.4; 79 -10.4; 87 -10.4; 96 -10.4; 106 -10.3; 116 -10.1; 128 -10.0; 141 -9.9; 155 -9.7; 170 -9.4; 187 -9.2; 206 -8.9; 227 -8.5; 249 -8.4; 274 -8.1; 302 -7.8; 332 -7.5; 365 -7.2; 402 -7.0; 442 -6.7; 486 -6.6; 535 -6.4; 588 -6.0; 647 -5.9; 712 -5.4; 783 -5.8; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.8; 1526 -8.4; 1678 -8.6; 1846 -8.3; 2031 -7.5; 2234 -6.3; 2457 -4.2; 2703 -2.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spider realvoice GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider realvoice ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.21 | -4.5 dB |
| Peaking | 140 Hz  | 0.84 | -2.1 dB |
| Peaking | 1840 Hz | 1.93 | -4.2 dB |
| Peaking | 3295 Hz | 1.28 | 6.8 dB  |
| Peaking | 5799 Hz | 3.34 | 4.8 dB  |
| Peaking | 709 Hz  | 2.57 | 1.2 dB  |
| Peaking | 1397 Hz | 5.04 | -0.6 dB |
| Peaking | 8349 Hz | 3.8  | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Spider%20realvoice/Spider%20realvoice.png)