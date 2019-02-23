# Focal Spirit One S 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.9; 25 -10.1; 28 -10.2; 31 -10.3; 34 -10.4; 37 -10.5; 41 -10.5; 45 -10.5; 49 -10.5; 54 -10.7; 60 -10.7; 66 -10.7; 72 -10.7; 79 -10.7; 87 -11.3; 96 -12.1; 106 -12.4; 116 -12.2; 128 -12.2; 141 -12.5; 155 -12.4; 170 -11.9; 187 -11.9; 206 -11.1; 227 -10.1; 249 -8.9; 274 -7.7; 302 -6.4; 332 -5.8; 365 -6.1; 402 -6.7; 442 -7.5; 486 -8.1; 535 -8.1; 588 -7.7; 647 -7.7; 712 -7.5; 783 -6.8; 861 -6.7; 947 -6.6; 1042 -6.6; 1146 -6.3; 1261 -6.0; 1387 -6.1; 1526 -6.0; 1678 -5.7; 1846 -5.3; 2031 -4.5; 2234 -4.0; 2457 -3.0; 2703 -2.5; 2973 -2.6; 3270 -3.5; 3597 -4.6; 3957 -5.1; 4353 -5.2; 4788 -6.1; 5267 -3.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One S 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One S 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.43 | -3.8 dB |
| Peaking | 121 Hz  | 1.25 | -4.3 dB |
| Peaking | 188 Hz  | 2.7  | -3.0 dB |
| Peaking | 2722 Hz | 2.18 | 4.2 dB  |
| Peaking | 6002 Hz | 4.26 | 6.5 dB  |
| Peaking | 242 Hz  | 3.26 | -1.0 dB |
| Peaking | 333 Hz  | 2.14 | 2.4 dB  |
| Peaking | 513 Hz  | 1.74 | -1.9 dB |
| Peaking | 6747 Hz | 8.5  | 1.6 dB  |
| Peaking | 8503 Hz | 1.22 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One%20S%202014/Focal%20Spirit%20One%20S%202014.png)