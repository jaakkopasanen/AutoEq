# Sennheiser PX 200 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.7; 206 -1.0; 227 -1.3; 249 -1.4; 274 -1.5; 302 -1.7; 332 -1.5; 365 -1.4; 402 -1.4; 442 -1.4; 486 -1.5; 535 -2.1; 588 -3.1; 647 -5.0; 712 -7.6; 783 -9.9; 861 -11.8; 947 -12.8; 1042 -13.3; 1146 -13.5; 1261 -13.7; 1387 -14.0; 1526 -13.8; 1678 -13.2; 1846 -13.1; 2031 -13.4; 2234 -13.1; 2457 -12.5; 2703 -11.6; 2973 -10.2; 3270 -8.2; 3597 -6.1; 3957 -4.7; 4353 -5.6; 4788 -7.3; 5267 -8.2; 5793 -8.9; 6373 -9.5; 7010 -8.8; 7711 -7.6; 8482 -7.8; 9330 -9.7; 10263 -11.9; 11289 -12.4; 12418 -9.8; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 200 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.1  | 6.2 dB  |
| Peaking | 529 Hz   | 1.47 | 4.7 dB  |
| Peaking | 1052 Hz  | 0.89 | -9.4 dB |
| Peaking | 2163 Hz  | 2.12 | -4.5 dB |
| Peaking | 10825 Hz | 2.43 | -6.3 dB |
| Peaking | 2862 Hz  | 4.4  | -1.6 dB |
| Peaking | 3990 Hz  | 3.34 | 3.7 dB  |
| Peaking | 5475 Hz  | 3.58 | -1.4 dB |
| Peaking | 6382 Hz  | 5.47 | -2.1 dB |
| Peaking | 13899 Hz | 4.14 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.8 dB  |
| Peaking | 250 Hz   | 1.41 | 3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 6.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -7.3 dB |
| Peaking | 2000 Hz  | 1.41 | -7.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20PX%20200%20II/Sennheiser%20PX%20200%20II.png)