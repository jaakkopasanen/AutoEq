# Focal Spirit One S 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.7; 25 -9.9; 28 -10.0; 31 -10.1; 34 -10.2; 37 -10.3; 41 -10.3; 45 -10.3; 49 -10.4; 54 -10.5; 60 -10.5; 66 -10.5; 72 -10.5; 79 -10.5; 87 -11.1; 96 -11.9; 106 -12.2; 116 -12.1; 128 -12.0; 141 -12.3; 155 -12.2; 170 -11.7; 187 -11.7; 206 -10.9; 227 -9.9; 249 -8.7; 274 -7.5; 302 -6.2; 332 -5.6; 365 -5.9; 402 -6.5; 442 -7.3; 486 -7.9; 535 -7.9; 588 -7.5; 647 -7.5; 712 -7.3; 783 -6.6; 861 -6.5; 947 -6.5; 1042 -6.4; 1146 -6.1; 1261 -5.8; 1387 -5.9; 1526 -5.8; 1678 -5.5; 1846 -5.1; 2031 -4.4; 2234 -3.8; 2457 -2.8; 2703 -2.3; 2973 -2.4; 3270 -3.3; 3597 -4.4; 3957 -4.9; 4353 -5.0; 4788 -5.9; 5267 -2.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One S 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One S 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.46 | -3.7 dB |
| Peaking | 120 Hz  | 1.32 | -4.2 dB |
| Peaking | 186 Hz  | 2.69 | -3.2 dB |
| Peaking | 2715 Hz | 1.99 | 4.3 dB  |
| Peaking | 5992 Hz | 4.19 | 6.5 dB  |
| Peaking | 243 Hz  | 3.42 | -1.2 dB |
| Peaking | 333 Hz  | 1.95 | 2.4 dB  |
| Peaking | 507 Hz  | 1.96 | -1.8 dB |
| Peaking | 6681 Hz | 8.16 | 1.7 dB  |
| Peaking | 8076 Hz | 1.38 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One%20S%202014/Focal%20Spirit%20One%20S%202014.png)