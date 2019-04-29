# Simgot EM2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.2; 25 -5.5; 28 -6.0; 31 -6.3; 34 -6.6; 37 -6.9; 41 -7.2; 45 -7.5; 49 -7.7; 54 -8.0; 60 -8.3; 66 -8.6; 72 -9.0; 79 -9.4; 87 -9.7; 96 -10.2; 106 -10.6; 116 -10.9; 128 -11.1; 141 -11.4; 155 -11.7; 170 -11.8; 187 -11.8; 206 -11.7; 227 -11.6; 249 -11.4; 274 -11.1; 302 -10.8; 332 -10.5; 365 -10.1; 402 -9.6; 442 -9.2; 486 -8.7; 535 -8.1; 588 -7.5; 647 -7.0; 712 -6.3; 783 -5.7; 861 -5.2; 947 -4.9; 1042 -5.0; 1146 -5.4; 1261 -5.7; 1387 -5.6; 1526 -5.2; 1678 -4.8; 1846 -4.3; 2031 -3.7; 2234 -3.0; 2457 -2.3; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -1.5; 4788 -2.1; 5267 -3.2; 5793 -4.2; 6373 -6.4; 7010 -5.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.2; 15026 -19.6; 16529 -23.3; 18182 -13.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Simgot EM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Simgot EM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 1.77 | 2.0 dB   |
| Peaking | 147 Hz   | 0.66 | -4.8 dB  |
| Peaking | 311 Hz   | 1.32 | -2.3 dB  |
| Peaking | 3362 Hz  | 0.91 | 6.3 dB   |
| Peaking | 16326 Hz | 2.18 | -19.5 dB |
| Peaking | 476 Hz   | 3.52 | -0.6 dB  |
| Peaking | 888 Hz   | 3.2  | 1.6 dB   |
| Peaking | 6504 Hz  | 7.16 | -2.1 dB  |
| Peaking | 13322 Hz | 2.39 | 4.9 dB   |
| Peaking | 15004 Hz | 3.78 | -5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -15.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Simgot%20EM2/Simgot%20EM2.png)