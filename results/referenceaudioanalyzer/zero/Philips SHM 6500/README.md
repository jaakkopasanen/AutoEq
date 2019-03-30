# Philips SHM 6500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -6.3; 25 -7.6; 28 -9.3; 31 -10.7; 34 -11.8; 37 -12.6; 41 -13.3; 45 -13.6; 49 -13.7; 54 -13.4; 60 -13.1; 66 -12.7; 72 -12.4; 79 -11.9; 87 -11.2; 96 -10.3; 106 -9.2; 116 -8.4; 128 -7.6; 141 -7.1; 155 -6.7; 170 -6.6; 187 -6.4; 206 -6.1; 227 -5.7; 249 -5.5; 274 -5.3; 302 -5.3; 332 -5.0; 365 -4.9; 402 -5.0; 442 -5.0; 486 -5.0; 535 -5.0; 588 -5.0; 647 -5.0; 712 -5.2; 783 -5.2; 861 -5.0; 947 -5.0; 1042 -5.3; 1146 -6.5; 1261 -8.8; 1387 -10.7; 1526 -11.1; 1678 -10.2; 1846 -8.1; 2031 -5.3; 2234 -2.7; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -4.7; 5267 -8.7; 5793 -11.8; 6373 -16.2; 7010 -18.9; 7711 -18.4; 8482 -15.2; 9330 -12.4; 10263 -10.7; 11289 -7.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHM 6500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHM 6500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 2.64 | 4.1 dB   |
| Peaking | 51 Hz    | 0.81 | -7.7 dB  |
| Peaking | 1592 Hz  | 0.96 | -17.9 dB |
| Peaking | 2782 Hz  | 0.33 | 18.5 dB  |
| Peaking | 7107 Hz  | 1.27 | -22.9 dB |
| Peaking | 1055 Hz  | 7.05 | 1.2 dB   |
| Peaking | 4314 Hz  | 3.98 | 4.5 dB   |
| Peaking | 4504 Hz  | 1.78 | -2.6 dB  |
| Peaking | 10188 Hz | 2.86 | -2.6 dB  |
| Peaking | 11405 Hz | 2.24 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -7.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 1.1 dB   |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -13.4 dB |
| Peaking | 16000 Hz | 1.41 | 2.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHM%206500/Philips%20SHM%206500.png)