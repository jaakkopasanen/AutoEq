# Plantronics BackBeat Fit
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.3; 28 -3.4; 31 -4.3; 34 -5.2; 37 -6.0; 41 -7.0; 45 -7.8; 49 -8.5; 54 -9.3; 60 -10.2; 66 -10.9; 72 -11.4; 79 -11.8; 87 -12.3; 96 -12.6; 106 -12.8; 116 -12.9; 128 -13.0; 141 -12.9; 155 -12.9; 170 -12.9; 187 -12.7; 206 -12.5; 227 -12.3; 249 -12.1; 274 -11.9; 302 -11.7; 332 -11.4; 365 -11.1; 402 -10.8; 442 -10.4; 486 -10.0; 535 -9.7; 588 -9.1; 647 -8.3; 712 -7.2; 783 -5.8; 861 -4.2; 947 -3.1; 1042 -2.6; 1146 -2.3; 1261 -1.8; 1387 -1.0; 1526 -0.9; 1678 -0.9; 1846 -0.9; 2031 -1.4; 2234 -1.9; 2457 -2.6; 2703 -4.0; 2973 -4.5; 3270 -4.4; 3597 -4.7; 3957 -5.7; 4353 -6.9; 4788 -8.0; 5267 -6.0; 5793 -3.9; 6373 -4.4; 7010 -5.5; 7711 -6.6; 8482 -6.8; 9330 -6.9; 10263 -6.9; 11289 -6.9; 12418 -6.9; 13660 -6.9; 15026 -6.9; 16529 -6.9; 18182 -6.9; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics BackBeat Fit GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics BackBeat Fit ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.82 | 7.6 dB  |
| Peaking | 89 Hz   | 0.61 | -4.3 dB |
| Peaking | 321 Hz  | 0.38 | -4.7 dB |
| Peaking | 1419 Hz | 0.77 | 7.7 dB  |
| Peaking | 6101 Hz | 6.7  | 2.6 dB  |
| Peaking | 351 Hz  | 1.85 | 0.4 dB  |
| Peaking | 815 Hz  | 1.18 | -1.2 dB |
| Peaking | 884 Hz  | 3.27 | 2.2 dB  |
| Peaking | 4690 Hz | 4.8  | -3.9 dB |
| Peaking | 4850 Hz | 1.83 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20BackBeat%20Fit/Plantronics%20BackBeat%20Fit.png)