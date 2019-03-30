# Philips SHL 5905 BK
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.5; 25 -5.2; 28 -5.8; 31 -6.2; 34 -6.3; 37 -6.2; 41 -5.9; 45 -5.4; 49 -4.9; 54 -4.7; 60 -5.4; 66 -6.5; 72 -7.4; 79 -7.9; 87 -8.2; 96 -8.2; 106 -8.2; 116 -8.1; 128 -7.7; 141 -7.1; 155 -6.2; 170 -4.9; 187 -3.9; 206 -3.7; 227 -5.0; 249 -7.3; 274 -9.7; 302 -11.0; 332 -11.7; 365 -12.2; 402 -12.4; 442 -11.8; 486 -11.0; 535 -10.3; 588 -9.8; 647 -9.4; 712 -9.2; 783 -8.6; 861 -7.9; 947 -7.4; 1042 -6.9; 1146 -6.3; 1261 -5.6; 1387 -4.9; 1526 -4.0; 1678 -3.2; 1846 -2.4; 2031 -1.9; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.2; 5267 -4.4; 5793 -7.0; 6373 -10.0; 7010 -12.1; 7711 -13.2; 8482 -12.8; 9330 -11.3; 10263 -10.2; 11289 -10.1; 12418 -9.6; 13660 -8.2; 15026 -7.3; 16529 -7.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHL 5905 BK GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHL 5905 BK ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.28 | 2.0 dB   |
| Peaking | 202 Hz  | 1.46 | 12.1 dB  |
| Peaking | 264 Hz  | 0.48 | -10.2 dB |
| Peaking | 4432 Hz | 0.5  | 13.3 dB  |
| Peaking | 7340 Hz | 0.81 | -15.7 dB |
| Peaking | 33 Hz   | 2.43 | -1.4 dB  |
| Peaking | 54 Hz   | 2.63 | 1.9 dB   |
| Peaking | 81 Hz   | 2.53 | -1.0 dB  |
| Peaking | 557 Hz  | 5.86 | 0.7 dB   |
| Peaking | 4484 Hz | 8.22 | 0.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | -6.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHL%205905%20BK/Philips%20SHL%205905%20BK.png)