# Sennheiser IE80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.4; 23 -14.5; 25 -14.6; 28 -14.7; 31 -14.8; 34 -14.8; 37 -14.9; 41 -14.9; 45 -14.8; 49 -14.7; 54 -14.7; 60 -14.6; 66 -14.4; 72 -14.2; 79 -14.0; 87 -13.7; 96 -13.4; 106 -13.1; 116 -12.7; 128 -12.4; 141 -12.0; 155 -11.5; 170 -11.1; 187 -10.4; 206 -9.7; 227 -9.5; 249 -9.4; 274 -9.0; 302 -8.5; 332 -8.0; 365 -7.5; 402 -6.8; 442 -6.2; 486 -5.6; 535 -5.0; 588 -4.4; 647 -3.8; 712 -3.1; 783 -2.6; 861 -2.1; 947 -1.7; 1042 -1.3; 1146 -0.9; 1261 -0.5; 1387 -0.5; 1526 -0.8; 1678 -1.1; 1846 -1.6; 2031 -2.1; 2234 -2.8; 2457 -3.5; 2703 -4.3; 2973 -4.9; 3270 -4.9; 3597 -4.6; 3957 -4.7; 4353 -5.3; 4788 -6.3; 5267 -8.4; 5793 -10.3; 6373 -9.5; 7010 -4.7; 7711 -4.9; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.15 | -9.6 dB |
| Peaking | 1307 Hz | 0.66 | 5.0 dB  |
| Peaking | 2831 Hz | 2.89 | -1.5 dB |
| Peaking | 5988 Hz | 3.06 | -6.4 dB |
| Peaking | 7207 Hz | 5.37 | 3.0 dB  |
| Peaking | 204 Hz  | 3.35 | 0.7 dB  |
| Peaking | 297 Hz  | 1.45 | -0.4 dB |
| Peaking | 647 Hz  | 2.81 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.9 dB |
| Peaking | 62 Hz    | 1.41 | -7.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20IE80/Sennheiser%20IE80.png)