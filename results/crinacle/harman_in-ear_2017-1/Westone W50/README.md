# Westone W50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.8; 25 -10.1; 28 -10.5; 31 -10.8; 34 -11.1; 37 -11.3; 41 -11.6; 45 -11.8; 49 -12.0; 54 -12.2; 60 -12.5; 66 -12.9; 72 -13.2; 79 -13.6; 87 -13.9; 96 -14.4; 106 -14.8; 116 -15.1; 128 -15.3; 141 -15.6; 155 -15.8; 170 -15.8; 187 -15.9; 206 -15.7; 227 -15.6; 249 -15.5; 274 -15.2; 302 -14.8; 332 -14.3; 365 -13.7; 402 -13.3; 442 -12.7; 486 -12.1; 535 -11.4; 588 -10.7; 647 -10.0; 712 -9.1; 783 -8.2; 861 -7.5; 947 -7.0; 1042 -7.0; 1146 -7.5; 1261 -7.9; 1387 -8.0; 1526 -7.5; 1678 -6.4; 1846 -4.6; 2031 -1.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.0; 15026 -24.7; 16529 -25.6; 18182 -24.0; 20000 -23.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.27 | -3.4 dB  |
| Peaking | 207 Hz   | 0.7  | -3.0 dB  |
| Peaking | 400 Hz   | 0.18 | -5.5 dB  |
| Peaking | 8036 Hz  | 0.2  | 16.2 dB  |
| Peaking | 16692 Hz | 0.37 | -30.7 dB |
| Peaking | 1504 Hz  | 1.96 | -7.6 dB  |
| Peaking | 1603 Hz  | 0.88 | 4.6 dB   |
| Peaking | 7917 Hz  | 4.02 | -3.6 dB  |
| Peaking | 12334 Hz | 4.98 | 6.1 dB   |
| Peaking | 19978 Hz | 1.64 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -7.2 dB  |
| Peaking | 250 Hz   | 1.41 | -7.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 16000 Hz | 1.41 | -24.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20W50/Westone%20W50.png)