# Sennheiser IE8 (max)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.0; 23 -15.4; 25 -15.6; 28 -16.0; 31 -16.2; 34 -16.3; 37 -16.4; 41 -16.5; 45 -16.4; 49 -16.4; 54 -16.4; 60 -16.3; 66 -16.2; 72 -16.0; 79 -15.8; 87 -15.6; 96 -15.3; 106 -14.9; 116 -14.5; 128 -14.0; 141 -13.5; 155 -13.3; 170 -13.5; 187 -13.4; 206 -12.9; 227 -12.2; 249 -11.5; 274 -10.9; 302 -10.4; 332 -9.9; 365 -9.3; 402 -8.6; 442 -7.8; 486 -7.0; 535 -6.2; 588 -5.4; 647 -4.6; 712 -3.8; 783 -3.0; 861 -2.3; 947 -1.6; 1042 -0.9; 1146 -0.5; 1261 -0.5; 1387 -0.8; 1526 -1.3; 1678 -1.9; 1846 -2.4; 2031 -2.8; 2234 -3.3; 2457 -3.9; 2703 -4.6; 2973 -5.0; 3270 -5.1; 3597 -5.1; 3957 -5.3; 4353 -6.1; 4788 -8.2; 5267 -11.7; 5793 -12.9; 6373 -10.1; 7010 -4.4; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE8 (max) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE8 (max) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 1.18 | -8.1 dB |
| Peaking | 39 Hz   | 0.4  | -8.4 dB |
| Peaking | 182 Hz  | 0.37 | -5.0 dB |
| Peaking | 1143 Hz | 0.68 | 6.5 dB  |
| Peaking | 5627 Hz | 4.68 | -8.0 dB |
| Peaking | 144 Hz  | 4.51 | 0.7 dB  |
| Peaking | 187 Hz  | 5.03 | -0.6 dB |
| Peaking | 3965 Hz | 7.42 | 0.6 dB  |
| Peaking | 6296 Hz | 7.99 | -2.7 dB |
| Peaking | 6940 Hz | 6.91 | 3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.9 dB |
| Peaking | 62 Hz    | 1.41 | -7.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20IE8%20(max)/Sennheiser%20IE8%20(max).png)