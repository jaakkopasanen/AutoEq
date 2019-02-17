# Sony DR-Z7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.6; 128 -1.4; 141 -2.3; 155 -2.4; 170 -2.2; 187 -2.9; 206 -3.4; 227 -3.4; 249 -3.4; 274 -3.4; 302 -3.4; 332 -3.3; 365 -3.2; 402 -3.2; 442 -3.0; 486 -3.5; 535 -3.7; 588 -3.4; 647 -4.0; 712 -4.8; 783 -5.1; 861 -5.7; 947 -6.2; 1042 -6.7; 1146 -7.3; 1261 -8.0; 1387 -9.3; 1526 -10.4; 1678 -11.8; 1846 -12.6; 2031 -12.6; 2234 -11.7; 2457 -9.5; 2703 -7.5; 2973 -5.4; 3270 -4.2; 3597 -3.9; 3957 -3.9; 4353 -5.2; 4788 -4.5; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony DR-Z7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony DR-Z7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.23 | 6.3 dB  |
| Peaking | 526 Hz  | 0.95 | 2.6 dB  |
| Peaking | 1970 Hz | 1.48 | -7.4 dB |
| Peaking | 3324 Hz | 2.19 | 4.1 dB  |
| Peaking | 5799 Hz | 3.28 | 6.7 dB  |
| Peaking | 18 Hz   | 1.55 | 0.8 dB  |
| Peaking | 86 Hz   | 0.48 | -0.5 dB |
| Peaking | 105 Hz  | 2.4  | 1.2 dB  |
| Peaking | 6643 Hz | 7.2  | 2.4 dB  |
| Peaking | 7330 Hz | 2.03 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 4.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20DR-Z7/Sony%20DR-Z7.png)