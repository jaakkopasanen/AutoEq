# Sennheiser HD 212 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.2; 49 -2.0; 54 -2.9; 60 -3.9; 66 -4.7; 72 -5.3; 79 -5.8; 87 -6.2; 96 -6.0; 106 -5.3; 116 -4.6; 128 -3.7; 141 -2.4; 155 -1.1; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.6; 274 -2.2; 302 -3.9; 332 -5.1; 365 -6.0; 402 -6.6; 442 -6.5; 486 -6.1; 535 -6.4; 588 -6.9; 647 -7.2; 712 -7.3; 783 -7.3; 861 -7.3; 947 -7.0; 1042 -7.0; 1146 -7.5; 1261 -8.2; 1387 -8.6; 1526 -8.9; 1678 -9.2; 1846 -9.6; 2031 -9.6; 2234 -9.6; 2457 -9.8; 2703 -10.3; 2973 -9.6; 3270 -6.9; 3597 -7.7; 3957 -12.1; 4353 -13.9; 4788 -12.5; 5267 -8.0; 5793 -6.0; 6373 -8.4; 7010 -9.4; 7711 -8.2; 8482 -6.5; 9330 -6.5; 10263 -8.1; 11289 -12.9; 12418 -14.9; 13660 -13.8; 15026 -11.2; 16529 -7.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 212 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 212 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.98 | 6.8 dB  |
| Peaking | 200 Hz   | 1.57 | 6.8 dB  |
| Peaking | 2000 Hz  | 1.02 | -3.2 dB |
| Peaking | 4397 Hz  | 5.09 | -7.3 dB |
| Peaking | 12963 Hz | 1.95 | -9.1 dB |
| Peaking | 88 Hz    | 4.12 | -1.6 dB |
| Peaking | 3425 Hz  | 9.04 | 3.4 dB  |
| Peaking | 5693 Hz  | 5.25 | 4.6 dB  |
| Peaking | 7658 Hz  | 0.9  | -4.2 dB |
| Peaking | 8926 Hz  | 2.29 | 5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 5.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -5.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20212%20PRO/Sennheiser%20HD%20212%20PRO.png)