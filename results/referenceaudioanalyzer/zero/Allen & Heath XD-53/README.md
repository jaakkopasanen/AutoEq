# Allen & Heath XD-53
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.4; 28 -3.3; 31 -5.6; 34 -7.6; 37 -9.2; 41 -11.0; 45 -12.2; 49 -12.8; 54 -13.1; 60 -13.0; 66 -12.8; 72 -12.9; 79 -13.0; 87 -13.0; 96 -12.8; 106 -12.7; 116 -12.5; 128 -12.4; 141 -12.3; 155 -12.1; 170 -11.9; 187 -11.7; 206 -11.4; 227 -11.0; 249 -10.6; 274 -10.0; 302 -9.3; 332 -8.4; 365 -7.7; 402 -7.3; 442 -6.8; 486 -6.1; 535 -5.3; 588 -4.6; 647 -4.4; 712 -4.9; 783 -6.1; 861 -7.3; 947 -7.9; 1042 -8.1; 1146 -8.2; 1261 -8.5; 1387 -8.6; 1526 -8.5; 1678 -8.0; 1846 -6.8; 2031 -5.1; 2234 -3.3; 2457 -2.3; 2703 -2.4; 2973 -2.3; 3270 -2.0; 3597 -3.1; 3957 -5.0; 4353 -5.5; 4788 -3.8; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.7; 12418 -8.3; 13660 -7.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Allen & Heath XD-53 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Allen & Heath XD-53 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.42 | 10.7 dB |
| Peaking | 65 Hz    | 0.35 | -7.8 dB |
| Peaking | 1494 Hz  | 2.23 | -3.4 dB |
| Peaking | 2694 Hz  | 1.6  | 4.9 dB  |
| Peaking | 5814 Hz  | 3.49 | 6.4 dB  |
| Peaking | 230 Hz   | 1.92 | -1.4 dB |
| Peaking | 656 Hz   | 1.52 | 3.8 dB  |
| Peaking | 915 Hz   | 1.93 | -2.5 dB |
| Peaking | 3381 Hz  | 9.25 | 1.0 dB  |
| Peaking | 12734 Hz | 3.42 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -7.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Allen%20&%20Heath%20XD-53/Allen%20&%20Heath%20XD-53.png)