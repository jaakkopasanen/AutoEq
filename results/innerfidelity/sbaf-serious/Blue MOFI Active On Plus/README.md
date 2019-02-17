# Blue MOFI Active On Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.8; 25 -6.0; 28 -6.5; 31 -6.9; 34 -7.4; 37 -7.8; 41 -8.4; 45 -9.0; 49 -9.5; 54 -10.1; 60 -10.7; 66 -11.1; 72 -11.3; 79 -11.3; 87 -11.1; 96 -11.0; 106 -10.7; 116 -10.1; 128 -9.9; 141 -10.1; 155 -10.1; 170 -9.1; 187 -9.5; 206 -9.2; 227 -8.6; 249 -7.8; 274 -6.6; 302 -5.7; 332 -5.4; 365 -5.4; 402 -5.4; 442 -3.8; 486 -3.1; 535 -3.7; 588 -3.9; 647 -4.2; 712 -4.8; 783 -5.1; 861 -5.7; 947 -6.4; 1042 -6.5; 1146 -6.4; 1261 -6.4; 1387 -6.6; 1526 -6.9; 1678 -6.8; 1846 -6.3; 2031 -5.2; 2234 -4.3; 2457 -4.1; 2703 -3.0; 2973 -2.5; 3270 -2.3; 3597 -1.4; 3957 -3.1; 4353 -6.5; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue MOFI Active On Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Active On Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 76 Hz   | 1.01 | -4.8 dB |
| Peaking | 173 Hz  | 1.38 | -2.4 dB |
| Peaking | 500 Hz  | 1.55 | 3.4 dB  |
| Peaking | 3173 Hz | 2.25 | 4.3 dB  |
| Peaking | 5721 Hz | 3.09 | 6.4 dB  |
| Peaking | 21 Hz   | 1.99 | 1.5 dB  |
| Peaking | 707 Hz  | 4.16 | 0.5 dB  |
| Peaking | 1786 Hz | 1.35 | -1.4 dB |
| Peaking | 2197 Hz | 2.91 | 1.9 dB  |
| Peaking | 7497 Hz | 2.69 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Active%20On%20Plus/Blue%20MOFI%20Active%20On%20Plus.png)