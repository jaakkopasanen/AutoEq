# Philips SHE 9005a
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -10.5; 25 -11.2; 28 -12.0; 31 -12.7; 34 -13.2; 37 -13.6; 41 -14.0; 45 -14.4; 49 -14.6; 54 -14.8; 60 -15.0; 66 -15.2; 72 -15.2; 79 -15.2; 87 -15.2; 96 -15.2; 106 -15.2; 116 -15.2; 128 -15.1; 141 -14.9; 155 -14.8; 170 -14.6; 187 -14.3; 206 -14.1; 227 -13.8; 249 -13.5; 274 -13.1; 302 -12.6; 332 -12.1; 365 -11.5; 402 -10.6; 442 -10.0; 486 -10.1; 535 -9.9; 588 -9.2; 647 -8.2; 712 -7.3; 783 -6.4; 861 -5.5; 947 -4.5; 1042 -3.6; 1146 -2.6; 1261 -1.2; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -1.8; 3270 -3.0; 3597 -3.5; 3957 -3.2; 4353 -3.3; 4788 -3.9; 5267 -4.7; 5793 -4.8; 6373 -3.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHE 9005a GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE 9005a ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 100 Hz  | 0.23 | -8.9 dB |
| Peaking | 1418 Hz | 1.12 | 6.1 dB  |
| Peaking | 2510 Hz | 1.73 | 3.9 dB  |
| Peaking | 5010 Hz | 1.21 | 1.8 dB  |
| Peaking | 18 Hz   | 2.42 | 1.1 dB  |
| Peaking | 419 Hz  | 8.11 | 0.6 dB  |
| Peaking | 5538 Hz | 6.91 | -0.8 dB |
| Peaking | 6743 Hz | 6.85 | 2.6 dB  |
| Peaking | 7991 Hz | 2.16 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHE%209005a/Philips%20SHE%209005a.png)