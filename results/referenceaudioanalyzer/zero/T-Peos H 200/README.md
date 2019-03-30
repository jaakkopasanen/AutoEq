# T-Peos H 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -11.3; 25 -11.7; 28 -12.2; 31 -12.5; 34 -12.7; 37 -12.8; 41 -12.9; 45 -12.9; 49 -12.9; 54 -12.9; 60 -12.7; 66 -12.5; 72 -12.4; 79 -12.1; 87 -11.8; 96 -11.4; 106 -11.0; 116 -10.5; 128 -10.0; 141 -9.5; 155 -9.0; 170 -8.8; 187 -8.6; 206 -8.6; 227 -8.3; 249 -7.9; 274 -7.5; 302 -7.0; 332 -6.6; 365 -6.1; 402 -5.8; 442 -5.4; 486 -5.1; 535 -4.8; 588 -4.6; 647 -4.3; 712 -4.1; 783 -3.9; 861 -3.8; 947 -3.6; 1042 -3.5; 1146 -3.7; 1261 -3.8; 1387 -4.2; 1526 -4.9; 1678 -5.9; 1846 -7.1; 2031 -8.7; 2234 -10.1; 2457 -11.1; 2703 -11.7; 2973 -12.8; 3270 -13.5; 3597 -13.0; 3957 -12.2; 4353 -9.6; 4788 -5.3; 5267 -1.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.5; 9330 -11.5; 10263 -15.7; 11289 -14.5; 12418 -8.2; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos H 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos H 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.59 | -6.1 dB  |
| Peaking | 95 Hz    | 0.97 | -2.8 dB  |
| Peaking | 3448 Hz  | 1.85 | -9.0 dB  |
| Peaking | 5790 Hz  | 2.2  | 8.8 dB   |
| Peaking | 10519 Hz | 3.23 | -10.9 dB |
| Peaking | 226 Hz   | 2.06 | -1.2 dB  |
| Peaking | 1056 Hz  | 0.63 | 3.5 dB   |
| Peaking | 2300 Hz  | 2.21 | -3.3 dB  |
| Peaking | 11718 Hz | 6.58 | -2.6 dB  |
| Peaking | 12930 Hz | 2.98 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/T-Peos%20H%20200/T-Peos%20H%20200.png)