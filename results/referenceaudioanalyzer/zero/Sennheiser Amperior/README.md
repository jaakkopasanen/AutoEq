# Sennheiser Amperior
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.8; 116 -1.2; 128 -1.4; 141 -1.7; 155 -1.7; 170 -1.7; 187 -1.5; 206 -1.4; 227 -1.4; 249 -1.4; 274 -1.4; 302 -1.4; 332 -1.6; 365 -2.2; 402 -3.4; 442 -4.8; 486 -6.1; 535 -7.0; 588 -7.3; 647 -7.2; 712 -7.2; 783 -7.2; 861 -7.4; 947 -7.6; 1042 -7.6; 1146 -7.5; 1261 -7.4; 1387 -7.6; 1526 -8.0; 1678 -8.8; 1846 -9.7; 2031 -10.2; 2234 -10.1; 2457 -9.4; 2703 -8.8; 2973 -8.8; 3270 -9.5; 3597 -10.3; 3957 -10.3; 4353 -8.9; 4788 -7.4; 5267 -6.8; 5793 -6.2; 6373 -7.3; 7010 -10.2; 7711 -13.5; 8482 -15.3; 9330 -15.0; 10263 -13.8; 11289 -13.7; 12418 -13.8; 13660 -9.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Amperior GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Amperior ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.17 | 6.1 dB  |
| Peaking | 340 Hz   | 1.11 | 4.4 dB  |
| Peaking | 528 Hz   | 1.18 | -3.3 dB |
| Peaking | 2273 Hz  | 1.1  | -3.2 dB |
| Peaking | 9923 Hz  | 1.33 | -9.0 dB |
| Peaking | 3848 Hz  | 4.12 | -3.1 dB |
| Peaking | 6005 Hz  | 2.99 | 2.5 dB  |
| Peaking | 8166 Hz  | 2.3  | -6.2 dB |
| Peaking | 10670 Hz | 0.65 | 5.0 dB  |
| Peaking | 12424 Hz | 2.8  | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | 3.5 dB  |
| Peaking | 250 Hz   | 1.41 | 5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -7.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20Amperior/Sennheiser%20Amperior.png)