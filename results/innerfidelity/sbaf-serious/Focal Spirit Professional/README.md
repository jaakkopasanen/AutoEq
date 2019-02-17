# Focal Spirit Professional
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.4; 25 -9.5; 28 -9.6; 31 -9.6; 34 -9.6; 37 -9.6; 41 -9.6; 45 -9.6; 49 -9.6; 54 -9.6; 60 -9.6; 66 -9.6; 72 -9.6; 79 -9.6; 87 -9.6; 96 -10.0; 106 -10.4; 116 -10.1; 128 -9.8; 141 -9.9; 155 -9.9; 170 -9.3; 187 -9.4; 206 -9.0; 227 -8.5; 249 -8.3; 274 -7.9; 302 -7.5; 332 -7.3; 365 -6.8; 402 -6.8; 442 -7.1; 486 -7.8; 535 -7.8; 588 -7.3; 647 -7.2; 712 -7.2; 783 -6.7; 861 -6.6; 947 -6.3; 1042 -6.5; 1146 -6.4; 1261 -6.3; 1387 -6.5; 1526 -6.9; 1678 -6.9; 1846 -6.4; 2031 -6.0; 2234 -5.4; 2457 -4.7; 2703 -4.6; 2973 -4.7; 3270 -6.0; 3597 -7.0; 3957 -6.3; 4353 -5.0; 4788 -3.5; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit Professional GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit Professional ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.44 | -2.8 dB |
| Peaking | 132 Hz  | 0.67 | -3.0 dB |
| Peaking | 2651 Hz | 2.46 | 3.1 dB  |
| Peaking | 4983 Hz | 0.63 | -3.0 dB |
| Peaking | 5748 Hz | 2.07 | 9.2 dB  |
| Peaking | 406 Hz  | 2.52 | 1.5 dB  |
| Peaking | 486 Hz  | 2.06 | -1.6 dB |
| Peaking | 940 Hz  | 4.26 | 0.4 dB  |
| Peaking | 1215 Hz | 5.62 | 0.4 dB  |
| Peaking | 3609 Hz | 7.62 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20Professional/Focal%20Spirit%20Professional.png)