# Fidue A65
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.5; 25 -2.1; 28 -2.9; 31 -3.5; 34 -4.2; 37 -4.7; 41 -5.3; 45 -5.9; 49 -6.4; 54 -6.9; 60 -7.5; 66 -8.0; 72 -8.5; 79 -8.9; 87 -9.5; 96 -10.0; 106 -10.3; 116 -10.5; 128 -10.7; 141 -11.0; 155 -11.0; 170 -11.0; 187 -10.8; 206 -10.7; 227 -10.4; 249 -10.1; 274 -9.7; 302 -9.3; 332 -8.9; 365 -8.3; 402 -7.8; 442 -7.1; 486 -6.7; 535 -6.1; 588 -5.4; 647 -4.9; 712 -4.9; 783 -4.4; 861 -3.9; 947 -3.8; 1042 -4.1; 1146 -4.3; 1261 -4.8; 1387 -6.0; 1526 -7.6; 1678 -8.3; 1846 -8.3; 2031 -8.1; 2234 -7.9; 2457 -6.8; 2703 -6.2; 2973 -4.1; 3270 -2.0; 3597 -0.5; 3957 -0.7; 4353 -2.3; 4788 -2.7; 5267 -1.9; 5793 -1.5; 6373 -2.2; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A65 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A65 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.71 | 6.3 dB  |
| Peaking | 151 Hz   | 0.52 | -5.1 dB |
| Peaking | 807 Hz   | 1.81 | 3.0 dB  |
| Peaking | 4550 Hz  | 1.46 | 5.2 dB  |
| Peaking | 22050 Hz | 2.36 | 2.7 dB  |
| Peaking | 1221 Hz  | 2.06 | 2.8 dB  |
| Peaking | 1735 Hz  | 1.36 | -3.3 dB |
| Peaking | 3566 Hz  | 2.71 | 6.1 dB  |
| Peaking | 4809 Hz  | 0.9  | -4.9 dB |
| Peaking | 6026 Hz  | 2.43 | 5.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A65/Fidue%20A65.png)