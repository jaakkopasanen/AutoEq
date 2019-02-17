# Plantronics BackBeat Fit
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -2.2; 25 -3.0; 28 -4.1; 31 -5.1; 34 -6.0; 37 -6.8; 41 -7.7; 45 -8.6; 49 -9.3; 54 -10.1; 60 -11.0; 66 -11.6; 72 -12.1; 79 -12.6; 87 -13.1; 96 -13.4; 106 -13.6; 116 -13.7; 128 -13.7; 141 -13.7; 155 -13.7; 170 -13.6; 187 -13.5; 206 -13.3; 227 -13.1; 249 -12.9; 274 -12.7; 302 -12.4; 332 -12.2; 365 -11.9; 402 -11.6; 442 -11.1; 486 -10.8; 535 -10.5; 588 -9.9; 647 -9.1; 712 -8.0; 783 -6.6; 861 -5.0; 947 -3.9; 1042 -3.3; 1146 -3.0; 1261 -2.6; 1387 -1.8; 1526 -0.9; 1678 -0.5; 1846 -1.1; 2031 -2.2; 2234 -2.7; 2457 -3.3; 2703 -4.8; 2973 -5.3; 3270 -5.2; 3597 -5.5; 3957 -6.5; 4353 -7.6; 4788 -8.8; 5267 -6.7; 5793 -4.7; 6373 -5.2; 7010 -6.3; 7711 -6.6; 8482 -3.7; 9330 -3.5; 10263 -3.5; 11289 -4.6; 12418 -6.3; 13660 -5.7; 15026 -4.9; 16529 -5.1; 18182 -6.0; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Fit GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Fit ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 86 Hz    | 0.72 | -5.3 dB |
| Peaking | 316 Hz   | 0.29 | -8.7 dB |
| Peaking | 1366 Hz  | 0.8  | 6.2 dB  |
| Peaking | 4440 Hz  | 1.32 | -4.4 dB |
| Peaking | 20671 Hz | 0.18 | -3.3 dB |
| Peaking | 21 Hz    | 2.5  | 3.6 dB  |
| Peaking | 5904 Hz  | 8.11 | 1.7 dB  |
| Peaking | 7512 Hz  | 4.64 | -2.9 dB |
| Peaking | 9383 Hz  | 1.82 | 1.8 dB  |
| Peaking | 12389 Hz | 4.12 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -6.9 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -7.2 dB |
| Peaking | 500 Hz   | 1.41 | -6.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.3 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20BackBeat%20Fit/Plantronics%20BackBeat%20Fit.png)