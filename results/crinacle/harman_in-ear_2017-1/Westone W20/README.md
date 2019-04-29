# Westone W20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.1; 25 -7.2; 28 -7.3; 31 -7.4; 34 -7.5; 37 -7.7; 41 -7.8; 45 -8.0; 49 -8.2; 54 -8.3; 60 -8.6; 66 -8.9; 72 -9.3; 79 -9.7; 87 -10.1; 96 -10.5; 106 -10.9; 116 -11.3; 128 -11.7; 141 -11.9; 155 -12.2; 170 -12.4; 187 -12.5; 206 -12.6; 227 -12.6; 249 -12.6; 274 -12.4; 302 -12.3; 332 -12.0; 365 -11.6; 402 -11.4; 442 -11.1; 486 -10.7; 535 -10.2; 588 -9.8; 647 -9.3; 712 -8.7; 783 -8.1; 861 -7.6; 947 -7.3; 1042 -7.4; 1146 -7.8; 1261 -8.1; 1387 -8.2; 1526 -7.9; 1678 -7.5; 1846 -7.0; 2031 -6.5; 2234 -5.6; 2457 -4.0; 2703 -1.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.8; 15026 -21.8; 16529 -24.4; 18182 -25.6; 20000 -29.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 142 Hz   | 0.55 | -4.0 dB  |
| Peaking | 334 Hz   | 0.64 | -3.8 dB  |
| Peaking | 1439 Hz  | 3    | -2.0 dB  |
| Peaking | 1987 Hz  | 4.02 | -1.8 dB  |
| Peaking | 3899 Hz  | 1.05 | 7.2 dB   |
| Peaking | 908 Hz   | 5.12 | 0.6 dB   |
| Peaking | 6145 Hz  | 2.12 | 4.9 dB   |
| Peaking | 12013 Hz | 1.5  | 12.4 dB  |
| Peaking | 17890 Hz | 0.32 | -11.2 dB |
| Peaking | 20021 Hz | 0.17 | -11.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 16000 Hz | 1.41 | -22.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20W20/Westone%20W20.png)