# Pioneer SE-A1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -2.0; 72 -3.6; 79 -5.0; 87 -6.2; 96 -7.1; 106 -7.6; 116 -7.9; 128 -8.3; 141 -8.4; 155 -8.4; 170 -8.2; 187 -8.2; 206 -8.0; 227 -7.7; 249 -7.5; 274 -7.2; 302 -7.2; 332 -7.1; 365 -6.6; 402 -6.5; 442 -6.2; 486 -5.7; 535 -5.3; 588 -5.4; 647 -5.6; 712 -5.9; 783 -5.8; 861 -6.3; 947 -6.4; 1042 -6.7; 1146 -6.8; 1261 -6.6; 1387 -6.4; 1526 -6.2; 1678 -5.7; 1846 -4.8; 2031 -3.8; 2234 -3.6; 2457 -3.5; 2703 -4.5; 2973 -5.2; 3270 -4.9; 3597 -4.2; 3957 -10.0; 4353 -14.7; 4788 -13.4; 5267 -10.2; 5793 -8.3; 6373 -6.4; 7010 -5.0; 7711 -8.3; 8482 -10.8; 9330 -12.0; 10263 -11.3; 11289 -7.6; 12418 -6.5; 13660 -6.8; 15026 -7.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE-A1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-A1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 35 Hz   | 1.03 | 7.3 dB   |
| Peaking | 3646 Hz | 1.07 | 6.9 dB   |
| Peaking | 4447 Hz | 2.59 | -14.1 dB |
| Peaking | 6810 Hz | 7.4  | 3.9 dB   |
| Peaking | 9327 Hz | 2.61 | -6.2 dB  |
| Peaking | 61 Hz   | 2.51 | 4.2 dB   |
| Peaking | 125 Hz  | 0.61 | -2.6 dB  |
| Peaking | 572 Hz  | 1.59 | 1.6 dB   |
| Peaking | 1641 Hz | 0.78 | -1.1 dB  |
| Peaking | 2066 Hz | 3.27 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE-A1000/Pioneer%20SE-A1000.png)