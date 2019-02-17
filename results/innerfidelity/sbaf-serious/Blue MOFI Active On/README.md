# Blue MOFI Active On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.1; 25 -4.4; 28 -4.6; 31 -4.9; 34 -5.0; 37 -5.2; 41 -5.3; 45 -5.4; 49 -5.5; 54 -5.7; 60 -5.9; 66 -6.1; 72 -6.3; 79 -6.6; 87 -6.9; 96 -7.4; 106 -7.5; 116 -7.4; 128 -7.6; 141 -8.3; 155 -8.7; 170 -7.8; 187 -8.4; 206 -8.4; 227 -7.9; 249 -7.3; 274 -6.3; 302 -5.4; 332 -5.2; 365 -5.3; 402 -5.3; 442 -3.4; 486 -3.1; 535 -3.5; 588 -3.7; 647 -4.1; 712 -4.7; 783 -5.0; 861 -5.6; 947 -6.2; 1042 -6.5; 1146 -6.7; 1261 -6.6; 1387 -6.8; 1526 -7.1; 1678 -7.0; 1846 -6.4; 2031 -5.2; 2234 -4.3; 2457 -4.1; 2703 -3.0; 2973 -2.4; 3270 -2.1; 3597 -1.1; 3957 -3.1; 4353 -6.7; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue MOFI Active On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Active On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.41 | 2.9 dB  |
| Peaking | 166 Hz  | 1.11 | -2.3 dB |
| Peaking | 502 Hz  | 1.58 | 3.6 dB  |
| Peaking | 3199 Hz | 2.41 | 4.7 dB  |
| Peaking | 5730 Hz | 3.13 | 6.4 dB  |
| Peaking | 713 Hz  | 4.53 | 0.4 dB  |
| Peaking | 1468 Hz | 2.55 | -1.2 dB |
| Peaking | 4213 Hz | 2.85 | 3.4 dB  |
| Peaking | 4244 Hz | 8.95 | -7.6 dB |
| Peaking | 8263 Hz | 3.69 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Active%20On/Blue%20MOFI%20Active%20On.png)