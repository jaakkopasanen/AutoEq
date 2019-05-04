# Plantronics BackBeat Fit
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.1; 25 -1.7; 28 -2.8; 31 -3.8; 34 -4.7; 37 -5.5; 41 -6.5; 45 -7.3; 49 -8.0; 54 -8.9; 60 -9.7; 66 -10.3; 72 -10.8; 79 -11.3; 87 -11.7; 96 -12.0; 106 -12.2; 116 -12.3; 128 -12.4; 141 -12.4; 155 -12.4; 170 -12.3; 187 -12.2; 206 -12.0; 227 -11.9; 249 -11.7; 274 -11.5; 302 -11.2; 332 -11.0; 365 -10.7; 402 -10.4; 442 -10.0; 486 -9.7; 535 -9.4; 588 -8.8; 647 -8.0; 712 -6.9; 783 -5.5; 861 -3.9; 947 -2.8; 1042 -2.4; 1146 -2.0; 1261 -1.6; 1387 -0.8; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -1.5; 2234 -2.4; 2457 -3.2; 2703 -4.2; 2973 -4.3; 3270 -3.8; 3597 -4.1; 3957 -5.0; 4353 -6.3; 4788 -7.9; 5267 -5.9; 5793 -3.5; 6373 -3.2; 7010 -5.3; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Fit GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Fit ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.87 | 6.7 dB  |
| Peaking | 94 Hz   | 0.57 | -4.6 dB |
| Peaking | 363 Hz  | 0.41 | -4.4 dB |
| Peaking | 1387 Hz | 0.8  | 7.6 dB  |
| Peaking | 6194 Hz | 7.17 | 3.5 dB  |
| Peaking | 919 Hz  | 3.72 | 1.8 dB  |
| Peaking | 1466 Hz | 0.74 | -1.4 dB |
| Peaking | 1832 Hz | 2.27 | 1.9 dB  |
| Peaking | 3474 Hz | 5.07 | 1.3 dB  |
| Peaking | 4747 Hz | 8.25 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20BackBeat%20Fit/Plantronics%20BackBeat%20Fit.png)