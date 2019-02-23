# AKG K601 2007
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.9; 54 -1.3; 60 -0.9; 66 -0.5; 72 -1.5; 79 -2.5; 87 -2.9; 96 -3.7; 106 -4.3; 116 -4.6; 128 -5.1; 141 -5.5; 155 -5.8; 170 -5.9; 187 -6.1; 206 -6.3; 227 -6.3; 249 -6.3; 274 -6.3; 302 -6.1; 332 -6.0; 365 -5.9; 402 -5.7; 442 -5.5; 486 -5.4; 535 -5.2; 588 -4.8; 647 -4.8; 712 -4.7; 783 -5.0; 861 -5.4; 947 -5.4; 1042 -5.3; 1146 -5.2; 1261 -5.1; 1387 -5.4; 1526 -6.2; 1678 -6.8; 1846 -8.1; 2031 -9.0; 2234 -8.7; 2457 -8.5; 2703 -8.2; 2973 -7.4; 3270 -5.5; 3597 -6.3; 3957 -7.0; 4353 -7.7; 4788 -8.3; 5267 -6.6; 5793 -9.1; 6373 -10.3; 7010 -7.3; 7711 -7.7; 8482 -9.7; 9330 -9.8; 10263 -8.3; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 2007 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 2007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.53 | 6.6 dB  |
| Peaking | 2147 Hz  | 1.53 | -5.4 dB |
| Peaking | 2269 Hz  | 0.37 | 3.4 dB  |
| Peaking | 6578 Hz  | 0.79 | -3.9 dB |
| Peaking | 22050 Hz | 2.21 | -1.2 dB |
| Peaking | 71 Hz    | 1.91 | 2.0 dB  |
| Peaking | 83 Hz    | 0.46 | -0.9 dB |
| Peaking | 7396 Hz  | 5.41 | 3.6 dB  |
| Peaking | 9064 Hz  | 1.44 | -3.3 dB |
| Peaking | 11227 Hz | 1.4  | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K601%202007/AKG%20K601%202007.png)