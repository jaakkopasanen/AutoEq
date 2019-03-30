# Sennheiser HD 558
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.8; 34 -2.4; 37 -2.9; 41 -3.6; 45 -4.1; 49 -4.5; 54 -5.0; 60 -5.3; 66 -5.5; 72 -5.7; 79 -5.9; 87 -6.2; 96 -6.4; 106 -6.4; 116 -6.4; 128 -6.4; 141 -6.4; 155 -6.4; 170 -6.2; 187 -6.1; 206 -6.1; 227 -6.1; 249 -6.1; 274 -6.1; 302 -5.9; 332 -5.7; 365 -5.8; 402 -5.8; 442 -5.5; 486 -5.4; 535 -5.2; 588 -5.0; 647 -4.8; 712 -4.5; 783 -4.5; 861 -4.4; 947 -4.1; 1042 -3.8; 1146 -3.8; 1261 -3.8; 1387 -3.8; 1526 -3.8; 1678 -3.9; 1846 -4.3; 2031 -5.2; 2234 -6.4; 2457 -7.6; 2703 -8.5; 2973 -9.6; 3270 -10.9; 3597 -11.7; 3957 -12.3; 4353 -12.6; 4788 -12.5; 5267 -12.6; 5793 -13.0; 6373 -12.8; 7010 -10.6; 7711 -6.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 558 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 558 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.21 | 5.6 dB  |
| Peaking | 36 Hz   | 1.49 | 1.6 dB  |
| Peaking | 980 Hz  | 0.75 | 2.5 dB  |
| Peaking | 1703 Hz | 2.09 | 2.3 dB  |
| Peaking | 4557 Hz | 1.1  | -7.2 dB |
| Peaking | 105 Hz  | 3.16 | -0.3 dB |
| Peaking | 3309 Hz | 3.56 | -0.8 dB |
| Peaking | 4633 Hz | 3.27 | 1.1 dB  |
| Peaking | 6494 Hz | 2.91 | -5.3 dB |
| Peaking | 7670 Hz | 1.79 | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20558/Sennheiser%20HD%20558.png)